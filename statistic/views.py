# -*- coding: utf-8 -*-
from statistic.forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from statistic.models import UserProfile, Post
import math
import datetime
from django import template
# import feedparser
register = template.Library()


def index(request):
    context_dict = {}
    posts = Post.objects.all()
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    current_user = request.user
    context_dict['current'] = current_user
    context_dict['posts'] = posts
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)


def post(request, post_id):
    context_dict = {}
    context = RequestContext(request)
    curr_post = Post.objects.get(pk=post_id)
    current_user = request.user
    context_dict['current'] = current_user
    context_dict['post'] = curr_post

    return render_to_response('post.html', context_dict, context)


@register.inclusion_tag("right.html")
def right_sidebar(request):
    context = RequestContext(request)
    context_dict = {}
    current_user = request.user
    pro = UserProfile.objects.get(pk=current_user)
    context_dict['profile'] = pro

    return render_to_response('right.html', context_dict, context)


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.is_active = False
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response('register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
                              context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    context_dict = {}
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                context_dict['status'] = 'К сожалению Ваш аккаунт еще неактивен.'
                return render_to_response('login.html', context_dict, context)
        else:
            # Bad login details were provided. So we can't log the user in.
            status = "Неверные данные: {0}, {1}".format(username, password)
            context_dict['status'] = status
            return render_to_response('login.html', context_dict, context)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


@login_required
def users_list(request):
    context = RequestContext(request)
    profiles = UserProfile.objects.all()
    current_user = request.user

    return render_to_response('users.html', {'profiles': profiles, 'current': current_user}, context)


@login_required
def profile(request, user_id):
    context = RequestContext(request)
    context_dict = {}
    u = User.objects.get(pk=user_id)
    try:
        up = UserProfile.objects.get(user=u)
        #if user profile exist lets check indexes
        now_date = datetime.date.today()
        cur_year = now_date.year
        age = cur_year - up.year
        #Индекс Кердо
        vik = 100 * (1 - (float(up.dat) / float(up.css)))
        #коэффициент экономизации кровообращения
        economisation = (up.sat - up.dat) * up.css

        diabet_type = up.type

        #Двойное произведение. Этот показатель отражает нагрузку сердца
        # по преодолению потока крови в артериальном русле.
        w = (up.sat * up.css) / 100

        #Ударный объем
        k = 101  # для взрослых
        adp = up.sat - up.dat  # Пульсовое давление
        uo = k + 0.5 * adp - 0.6 * (up.dat + age)
        context_dict['kerdo'] = round(vik, 2)
        context_dict['economisation'] = economisation
        context_dict['w'] = w
        context_dict['uo'] = uo
        context_dict['age'] = age
        context_dict['diabet_type'] = diabet_type
        context_dict['pict'] = up.picture
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    context_dict['current'] = request.user

    return render_to_response('profile.html', context_dict,  context)


def stats(request):
    statistic = {}
    # Add variables
    vik_one_all = int()
    vik_two_all = int()
    w_one_all = int()
    w_two_all = int()
    uo_one_all = int()
    uo_two_all = int()
    eco_one_all = int()
    eco_two_all = int()

    vik_one = int()
    vik_two = int()
    w_one = int()
    w_two = int()
    uo_one = int()
    uo_two = int()
    eco_one = int()
    eco_two = int()

    skf_one = int()
    hslpvp_one = int()
    hslpnp_one = int()
    moch_one = int()
    kreat_one = int()
    bilirubin_one = int()
    ast_one = int()
    alt_one = int()
    glukosa_one = int()
    #2
    skf_two = int()
    hslpvp_two = int()
    hslpnp_two = int()
    moch_two = int()
    kreat_two = int()
    bilirubin_two = int()
    ast_two = int()
    alt_two = int()
    glukosa_two = int()

    skf_onew = int()
    hslpvp_onew = int()
    hslpnp_onew = int()
    moch_onew = int()
    kreat_onew = int()
    bilirubin_onew = int()
    ast_onew = int()
    alt_onew = int()
    glukosa_onew = int()
    #2
    skf_twow = int()
    hslpvp_twow = int()
    hslpnp_twow = int()
    moch_twow = int()
    kreat_twow = int()
    bilirubin_twow = int()
    ast_twow = int()
    alt_twow = int()
    glukosa_twow = int()

    vik_onew = int()
    vik_twow = int()
    w_onew = int()
    w_twow = int()
    uo_onew = int()
    uo_twow = int()
    eco_onew = int()
    eco_twow = int()

    vik_sigma_man_sum = int()
    w_sigma_man_sum = int()
    uo_sigma_man_sum = int()
    eco_sigma_man_sum = int()
    skf_sigma_man_sum = int()
    hslpvp_sigma_man_sum = int()
    hslpnp_sigma_man_sum = int()
    moch_sigma_man_sum = int()
    kreat_sigma_man_sum = int()
    bilirubin_sigma_man_sum = int()
    ast_sigma_man_sum = int()
    alt_sigma_man_sum = int()
    glukosa_sigma_man_sum = int()

    vik_sigma_wom_sum = int()
    w_sigma_wom_sum = int()
    uo_sigma_wom_sum = int()
    eco_sigma_wom_sum = int()
    skf_sigma_wom_sum = int()
    hslpvp_sigma_wom_sum = int()
    hslpnp_sigma_wom_sum = int()
    moch_sigma_wom_sum = int()
    kreat_sigma_wom_sum = int()
    bilirubin_sigma_wom_sum = int()
    ast_sigma_wom_sum = int()
    alt_sigma_wom_sum = int()
    glukosa_sigma_wom_sum = int()

    vik_sigma_man2_sum = int()
    w_sigma_man2_sum = int()
    uo_sigma_man2_sum = int()
    eco_sigma_man2_sum = int()
    skf_sigma_man2_sum = int()
    hslpvp_sigma_man2_sum = int()
    hslpnp_sigma_man2_sum = int()
    moch_sigma_man2_sum = int()
    kreat_sigma_man2_sum = int()
    bilirubin_sigma_man2_sum = int()
    ast_sigma_man2_sum = int()
    alt_sigma_man2_sum = int()
    glukosa_sigma_man2_sum = int()

    vik_sigma_wom2_sum = int()
    w_sigma_wom2_sum = int()
    uo_sigma_wom2_sum = int()
    eco_sigma_wom2_sum = int()
    skf_sigma_wom2_sum = int()
    hslpvp_sigma_wom2_sum = int()
    hslpnp_sigma_wom2_sum = int()
    moch_sigma_wom2_sum = int()
    kreat_sigma_wom2_sum = int()
    bilirubin_sigma_wom2_sum = int()
    ast_sigma_wom2_sum = int()
    alt_sigma_wom2_sum = int()
    glukosa_sigma_wom2_sum = int()

    index_type_one_all = 0
    index_type_two_all = 0
    index_type_one = 0
    index_type_two = 0
    index_type_one_w = 0
    index_type_two_w = 0
    sex_index_m = 0
    sex_index_w = 0
    sex_index_m2 = 0
    sex_index_w2 = 0

    context = RequestContext(request)

    profiles = UserProfile.objects.all()
    users = User.objects.all()
    for value in profiles:
        if value.user.is_active:
            now_date = datetime.date.today()
            cur_year = now_date.year
            sat = value.sat
            dat = value.dat
            css = value.css
            year = value.year
            sex = value.gender
            diabet_type = value.type
            skf = value.skf
            hslpvp = value.hslpvp
            hslpnp = value.hslpnp
            moch = value.moch
            kreat = value.kreat
            bilirubin = value.bilirubin
            ast = value.ast
            alt = value.alt
            glukosa = value.glukosa

            age = cur_year - year
            #Индекс Кердо
            vik = 100 * (1 - (float(dat) / float(css)))

            #коэффициент экономизации кровообращения
            economisation = (sat - dat) * css

            #Двойное произведение. Этот показатель отражает нагрузку сердца
            # по преодолению потока крови в артериальном русле.
            w = (sat * css) / 100

            #Ударный объем
            k = 101  # для взрослых
            adp = sat - dat  # Пульсовое давление
            uo = k + 0.5 * adp - 0.6 * (dat + age)
            #Считаем среднее по типам диабета
            #Тип 1

            if int(diabet_type) == 1:
                #For all
                index_type_one_all += 1
                vik_one_all += vik
                w_one_all += w
                uo_one_all += uo
                eco_one_all += economisation

                if sex == "M":
                    vik_one += vik
                    w_one += w
                    uo_one += uo
                    eco_one += economisation
                    sex_index_m += 1
                    index_type_one += 1

                    #biochem
                    skf_one += skf
                    hslpvp_one += hslpvp
                    hslpnp_one += hslpnp
                    moch_one += moch
                    kreat_one += kreat
                    bilirubin_one += bilirubin
                    ast_one += ast
                    alt_one += alt
                    glukosa_one += glukosa

                    #vik sigma
                    vik_sigma_man_sum += (abs(vik) - abs(vik_one/sex_index_m))**2
                    #W sigma
                    w_sigma_man_sum += (abs(w) - abs(w_one/sex_index_m))**2
                    #uo sigma
                    uo_sigma_man_sum += (abs(uo) - abs(uo_one/sex_index_m))**2
                    #eco sigma
                    eco_sigma_man_sum += (abs(economisation) - abs(eco_one/sex_index_m))**2

                    #skf,hslpvp,hslpnp,moch,kreat,bilirubin,ast,alt,glukosa
                    skf_sigma_man_sum += (abs(skf) - abs(skf_one/sex_index_m))**2
                    hslpvp_sigma_man_sum += (abs(hslpvp) - abs(hslpvp_one/sex_index_m))**2
                    hslpnp_sigma_man_sum += (abs(hslpnp) - abs(hslpnp_one/sex_index_m))**2
                    moch_sigma_man_sum += (abs(moch) - abs(moch_one/sex_index_m))**2
                    kreat_sigma_man_sum += (abs(kreat) - abs(kreat_one/sex_index_m))**2
                    bilirubin_sigma_man_sum += (abs(bilirubin) - abs(bilirubin_one/sex_index_m))**2
                    ast_sigma_man_sum += (abs(ast) - abs(ast_one/sex_index_m))**2
                    alt_sigma_man_sum += (abs(alt) - abs(alt_one/sex_index_m))**2
                    glukosa_sigma_man_sum += (abs(glukosa) - abs(glukosa_one/sex_index_m))**2

                if sex == "F":
                    vik_onew += vik
                    w_onew += w
                    uo_onew += uo
                    eco_onew += economisation
                    sex_index_w += 1
                    index_type_one_w += 1

                    #biochem
                    skf_onew += skf
                    hslpvp_onew += hslpvp
                    hslpnp_onew += hslpnp
                    moch_onew += moch
                    kreat_onew += kreat
                    bilirubin_onew += bilirubin
                    ast_onew += ast
                    alt_onew += alt
                    glukosa_onew += glukosa

                    #vik sigma
                    vik_sigma_wom_sum += (abs(vik) - abs(vik_onew/sex_index_w))**2
                    #W sigma
                    w_sigma_wom_sum += (abs(w) - abs(w_onew/sex_index_w))**2
                    #uo sigma
                    uo_sigma_wom_sum += (abs(uo) - abs(uo_onew/sex_index_w))**2
                    #eco sigma
                    eco_sigma_wom_sum += (abs(economisation) - abs(eco_onew/sex_index_w))**2

                    #skf,hslpvp,hslpnp,moch,kreat,bilirubin,ast,alt,glukosa
                    skf_sigma_wom_sum += (abs(skf) - abs(skf_onew/sex_index_w))**2
                    hslpvp_sigma_wom_sum += (abs(hslpvp) - abs(hslpvp_onew/sex_index_w))**2
                    hslpnp_sigma_wom_sum += (abs(hslpnp) - abs(hslpnp_onew/sex_index_w))**2
                    moch_sigma_wom_sum += (abs(moch) - abs(moch_onew/sex_index_w))**2
                    kreat_sigma_wom_sum += (abs(kreat) - abs(kreat_onew/sex_index_w))**2
                    bilirubin_sigma_wom_sum += (abs(bilirubin) - abs(bilirubin_onew/sex_index_w))**2
                    ast_sigma_wom_sum += (abs(ast) - abs(ast_onew/sex_index_w))**2
                    alt_sigma_wom_sum += (abs(alt) - abs(alt_onew/sex_index_w))**2
                    glukosa_sigma_wom_sum += (abs(glukosa) - abs(glukosa_onew/sex_index_w))**2

            #Тип 2
            if int(diabet_type) == 2:
                #For All
                index_type_two_all += 1
                vik_two_all += vik
                w_two_all += w
                uo_two_all += uo
                eco_two_all += economisation
                if sex == "M":
                    vik_two += vik
                    w_two += w
                    uo_two += uo
                    eco_two += economisation
                    sex_index_m2 += 1
                    index_type_two += 1

                    #biochem
                    skf_two += skf
                    hslpvp_two += hslpvp
                    hslpnp_two += hslpnp
                    moch_two += moch
                    kreat_two += kreat
                    bilirubin_two += bilirubin
                    ast_two += ast
                    alt_two += alt
                    glukosa_two += glukosa

                    #vik sigma
                    vik_sigma_man2_sum += (abs(vik) - abs(vik_two/sex_index_m2))**2
                    #W sigma
                    w_sigma_man2_sum += (abs(w) - abs(w_two/sex_index_m2))**2
                    #uo sigma
                    uo_sigma_man2_sum += (abs(uo) - abs(uo_two/sex_index_m2))**2
                    #eco sigma
                    eco_sigma_man2_sum += (abs(economisation) - abs(eco_two/sex_index_m2))**2

                    #skf,hslpvp,hslpnp,moch,kreat,bilirubin,ast,alt,glukosa
                    skf_sigma_man2_sum += (abs(skf) - abs(skf_two/sex_index_m2))**2
                    hslpvp_sigma_man2_sum += (abs(hslpvp) - abs(hslpvp_two/sex_index_m2))**2
                    hslpnp_sigma_man2_sum += (abs(hslpnp) - abs(hslpnp_two/sex_index_m2))**2
                    moch_sigma_man2_sum += (abs(moch) - abs(moch_two/sex_index_m2))**2
                    kreat_sigma_man2_sum += (abs(kreat) - abs(kreat_two/sex_index_m2))**2
                    bilirubin_sigma_man2_sum += (abs(bilirubin) - abs(bilirubin_two/sex_index_m2))**2
                    ast_sigma_man2_sum += (abs(ast) - abs(ast_two/sex_index_m2))**2
                    alt_sigma_man2_sum += (abs(alt) - abs(alt_two/sex_index_m2))**2
                    glukosa_sigma_man2_sum += (abs(glukosa) - abs(glukosa_two/sex_index_m2))**2

                if sex == "F":
                    vik_twow += vik
                    w_twow += w
                    uo_twow += uo
                    eco_twow += economisation
                    sex_index_w2 += 1
                    index_type_two_w += 1

                    #biochem
                    skf_twow += skf
                    hslpvp_twow += hslpvp
                    hslpnp_twow += hslpnp
                    moch_twow += moch
                    kreat_twow += kreat
                    bilirubin_twow += bilirubin
                    ast_twow += ast
                    alt_twow += alt
                    glukosa_twow += glukosa

                    #vik sigma
                    vik_sigma_wom2_sum += (abs(vik) - abs(vik_twow/sex_index_w2))**2
                    #W sigma
                    w_sigma_wom2_sum += (abs(w) - abs(w_twow/sex_index_w2))**2
                    #uo sigma
                    uo_sigma_wom2_sum += (abs(uo) - abs(uo_twow/sex_index_w2))**2
                    #eco sigma
                    eco_sigma_wom2_sum += (abs(economisation) - abs(eco_twow/sex_index_w2))**2

                    #skf,hslpvp,hslpnp,moch,kreat,bilirubin,ast,alt,glukosa
                    skf_sigma_wom2_sum += (abs(skf) - abs(skf_twow/sex_index_w2))**2
                    hslpvp_sigma_wom2_sum += (abs(hslpvp) - abs(hslpvp_twow/sex_index_w2))**2
                    hslpnp_sigma_wom2_sum += (abs(hslpnp) - abs(hslpnp_twow/sex_index_w2))**2
                    moch_sigma_wom2_sum += (abs(moch) - abs(moch_twow/sex_index_w2))**2
                    kreat_sigma_wom2_sum += (abs(kreat) - abs(kreat_twow/sex_index_w2))**2
                    bilirubin_sigma_wom2_sum += (abs(bilirubin) - abs(bilirubin_twow/sex_index_w2))**2
                    ast_sigma_wom2_sum += (abs(ast) - abs(ast_twow/sex_index_w2))**2
                    alt_sigma_wom2_sum += (abs(alt) - abs(alt_twow/sex_index_w2))**2
                    glukosa_sigma_wom2_sum += (abs(glukosa) - abs(glukosa_twow/sex_index_w2))**2

    """
    Man type 1
    """
    #vik man 1
    sigma = math.sqrt(vik_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(vik_one/sex_index_m))
    middle = vik_one/sex_index_m

    statistic['m_one_sex'] = sex_index_m
    statistic['m_one_vik_sigma'] = round(sigma, 4)
    statistic['m_one_vik_sx'] = round(sx, 4)
    statistic['m_one_vik_cv'] = round(cv, 4)
    statistic['m_one_vik_middle'] = round(middle, 4)

    #w man 1
    sigma = math.sqrt(w_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(w_one/sex_index_m))
    middle = w_one/sex_index_m

    statistic['m_one_w_sigma'] = round(sigma, 4)
    statistic['m_one_w_sx'] = round(sx, 4)
    statistic['m_one_w_cv'] = round(cv, 4)
    statistic['m_one_w_middle'] = round(middle, 4)

    #uo man 1
    sigma = math.sqrt(uo_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(uo_one/sex_index_m))
    middle = uo_one/sex_index_m

    statistic['m_one_uo_sigma'] = round(sigma, 4)
    statistic['m_one_uo_sx'] = round(sx, 4)
    statistic['m_one_uo_cv'] = round(cv, 4)
    statistic['m_one_uo_middle'] = round(middle, 4)

    #economisation man 1
    sigma = math.sqrt(eco_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(eco_one/sex_index_m))
    middle = eco_one/sex_index_m

    statistic['m_one_eco_sigma'] = round(sigma, 4)
    statistic['m_one_eco_sx'] = round(sx, 4)
    statistic['m_one_eco_cv'] = round(cv, 4)
    statistic['m_one_eco_middle'] = round(middle, 4)

    #SKF
    sigma = math.sqrt(skf_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(skf_one/sex_index_m))
    middle = skf_one/sex_index_m

    statistic['m_one_skf_sigma'] = round(sigma, 4)
    statistic['m_one_skf_sx'] = round(sx, 4)
    statistic['m_one_skf_cv'] = round(cv, 4)
    statistic['m_one_skf_middle'] = round(middle, 4)

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(hslpvp_one/sex_index_m))
    middle = hslpvp_one/sex_index_m

    statistic['m_one_vp_sigma'] = round(sigma, 4)
    statistic['m_one_vp_sx'] = round(sx, 4)
    statistic['m_one_vp_cv'] = round(cv, 4)
    statistic['m_one_vp_middle'] = round(middle, 4)

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(hslpnp_one/sex_index_m))
    middle = hslpnp_one/sex_index_m

    statistic['m_one_np_sigma'] = round(sigma, 4)
    statistic['m_one_np_sx'] = round(sx, 4)
    statistic['m_one_np_cv'] = round(cv, 4)
    statistic['m_one_np_middle'] = round(middle, 4)

    #MOCH
    sigma = math.sqrt(moch_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(moch_one/sex_index_m))
    middle = moch_one/sex_index_m

    statistic['m_one_moch_sigma'] = round(sigma, 4)
    statistic['m_one_moch_sx'] = round(sx, 4)
    statistic['m_one_moch_cv'] = round(cv, 4)
    statistic['m_one_moch_middle'] = round(middle, 4)

    #KREAT
    sigma = math.sqrt(kreat_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(kreat_one/sex_index_m))
    middle = kreat_one/sex_index_m

    statistic['m_one_kr_sigma'] = round(sigma, 4)
    statistic['m_one_kr_sx'] = round(sx, 4)
    statistic['m_one_kr_cv'] = round(cv, 4)
    statistic['m_one_kr_middle'] = round(middle, 4)

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(bilirubin_one/sex_index_m))
    middle = bilirubin_one/sex_index_m

    statistic['m_one_bil_sigma'] = round(sigma, 4)
    statistic['m_one_bil_sx'] = round(sx, 4)
    statistic['m_one_bil_cv'] = round(cv, 4)
    statistic['m_one_bil_middle'] = round(middle, 4)

    #AST
    sigma = math.sqrt(ast_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(ast_one/sex_index_m))
    middle = ast_one/sex_index_m

    statistic['m_one_ast_sigma'] = round(sigma, 4)
    statistic['m_one_ast_sx'] = round(sx, 4)
    statistic['m_one_ast_cv'] = round(cv, 4)
    statistic['m_one_ast_middle'] = round(middle, 4)

    #ALT
    sigma = math.sqrt(alt_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(alt_one/sex_index_m))
    middle = alt_one/sex_index_m

    statistic['m_one_alt_sigma'] = round(sigma, 4)
    statistic['m_one_alt_sx'] = round(sx, 4)
    statistic['m_one_alt_cv'] = round(cv, 4)
    statistic['m_one_alt_middle'] = round(middle, 4)

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(glukosa_one/sex_index_m))
    middle = glukosa_one/sex_index_m

    statistic['m_one_gl_sigma'] = round(sigma, 4)
    statistic['m_one_gl_sx'] = round(sx, 4)
    statistic['m_one_gl_cv'] = round(cv, 4)
    statistic['m_one_gl_middle'] = round(middle, 4)

    """
    Woman type 1
    """
    #vik wom 1
    sigma = math.sqrt(vik_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(vik_onew/sex_index_w))
    middle = vik_onew/sex_index_w

    statistic['w_one_sex'] = sex_index_w
    statistic['w_one_vik_sigma'] = round(sigma, 4)
    statistic['w_one_vik_sx'] = round(sx, 4)
    statistic['w_one_vik_cv'] = round(cv, 4)
    statistic['w_one_vik_middle'] = round(middle, 4)

    #w wom 1
    sigma = math.sqrt(w_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(w_onew/sex_index_w))
    middle = w_onew/sex_index_w

    statistic['w_one_w_sigma'] = round(sigma, 4)
    statistic['w_one_w_sx'] = round(sx, 4)
    statistic['w_one_w_cv'] = round(cv, 4)
    statistic['w_one_w_middle'] = round(middle, 4)

    #uo wom 1
    sigma = math.sqrt(uo_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(uo_onew/sex_index_w))
    middle = uo_onew/sex_index_w

    statistic['w_one_uo_sigma'] = round(sigma, 4)
    statistic['w_one_uo_sx'] = round(sx, 4)
    statistic['w_one_uo_cv'] = round(cv, 4)
    statistic['w_one_uo_middle'] = round(middle, 4)

    #economisation wom 1
    sigma = math.sqrt(eco_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(eco_onew/sex_index_w))
    middle = eco_onew/sex_index_w

    statistic['w_one_eco_sigma'] = round(sigma, 4)
    statistic['w_one_eco_sx'] = round(sx, 4)
    statistic['w_one_eco_cv'] = round(cv, 4)
    statistic['w_one_eco_middle'] = round(middle, 4)

    #SKF
    sigma = math.sqrt(skf_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(skf_onew/sex_index_w))
    middle = skf_onew/sex_index_w

    statistic['w_one_skf_sigma'] = round(sigma, 4)
    statistic['w_one_skf_sx'] = round(sx, 4)
    statistic['w_one_skf_cv'] = round(cv, 4)
    statistic['w_one_skf_middle'] = round(middle, 4)

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(hslpvp_onew/sex_index_w))
    middle = hslpvp_onew/sex_index_w

    statistic['w_one_vp_sigma'] = round(sigma, 4)
    statistic['w_one_vp_sx'] = round(sx, 4)
    statistic['w_one_vp_cv'] = round(cv, 4)
    statistic['w_one_vp_middle'] = round(middle, 4)

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(hslpnp_onew/sex_index_w))
    middle = hslpnp_onew/sex_index_w

    statistic['w_one_np_sigma'] = round(sigma, 4)
    statistic['w_one_np_sx'] = round(sx, 4)
    statistic['w_one_np_cv'] = round(cv, 4)
    statistic['w_one_np_middle'] = round(middle, 4)

    #MOCH
    sigma = math.sqrt(moch_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(moch_onew/sex_index_w))
    middle = moch_onew/sex_index_w

    statistic['w_one_moch_sigma'] = round(sigma, 4)
    statistic['w_one_moch_sx'] = round(sx, 4)
    statistic['w_one_moch_cv'] = round(cv, 4)
    statistic['w_one_moch_middle'] = round(middle, 4)

    #KREAT
    sigma = math.sqrt(kreat_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(kreat_onew/sex_index_w))
    middle = kreat_onew/sex_index_w

    statistic['w_one_kr_sigma'] = round(sigma, 4)
    statistic['w_one_kr_sx'] = round(sx, 4)
    statistic['w_one_kr_cv'] = round(cv, 4)
    statistic['w_one_kr_middle'] = round(middle, 4)

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(bilirubin_onew/sex_index_w))
    middle = bilirubin_onew/sex_index_w

    statistic['w_one_bil_sigma'] = round(sigma, 4)
    statistic['w_one_bil_sx'] = round(sx, 4)
    statistic['w_one_bil_cv'] = round(cv, 4)
    statistic['w_one_bil_middle'] = round(middle, 4)

    #AST
    sigma = math.sqrt(ast_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(ast_onew/sex_index_w))
    middle = ast_onew/sex_index_w

    statistic['w_one_ast_sigma'] = round(sigma, 4)
    statistic['w_one_ast_sx'] = round(sx, 4)
    statistic['w_one_ast_cv'] = round(cv, 4)
    statistic['w_one_ast_middle'] = round(middle, 4)

    #ALT
    sigma = math.sqrt(alt_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(alt_onew/sex_index_w))
    middle = alt_onew/sex_index_w

    statistic['w_one_alt_sigma'] = round(sigma, 4)
    statistic['w_one_alt_sx'] = round(sx, 4)
    statistic['w_one_alt_cv'] = round(cv, 4)
    statistic['w_one_alt_middle'] = round(middle, 4)

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(glukosa_onew/sex_index_w))
    middle = glukosa_onew/sex_index_w

    statistic['w_one_gl_sigma'] = round(sigma, 4)
    statistic['w_one_gl_sx'] = round(sx, 4)
    statistic['w_one_gl_cv'] = round(cv, 4)
    statistic['w_one_gl_middle'] = round(middle, 4)

    """
    Man type 2
    """

    #vik man 2
    sigma = math.sqrt(vik_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(vik_two/sex_index_m2))
    middle = vik_two/sex_index_m2

    statistic['m_two_sex'] = sex_index_m2
    statistic['m_two_vik_sigma'] = round(sigma, 4)
    statistic['m_two_vik_sx'] = round(sx, 4)
    statistic['m_two_vik_cv'] = round(cv, 4)
    statistic['m_two_vik_middle'] = round(middle, 4)

    #w man 2
    sigma = math.sqrt(w_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(w_two/sex_index_m2))
    middle = w_two/sex_index_m2

    statistic['m_two_w_sigma'] = round(sigma, 4)
    statistic['m_two_w_sx'] = round(sx, 4)
    statistic['m_two_w_cv'] = round(cv, 4)
    statistic['m_two_w_middle'] = round(middle, 4)

    #uo man 2
    sigma = math.sqrt(uo_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(uo_two/sex_index_m2))
    middle = uo_two/sex_index_m2

    statistic['m_two_uo_sigma'] = round(sigma, 4)
    statistic['m_two_uo_sx'] = round(sx, 4)
    statistic['m_two_uo_cv'] = round(cv, 4)
    statistic['m_two_uo_middle'] = round(middle, 4)

    #economisation man 2
    sigma = math.sqrt(eco_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(eco_two/sex_index_m2))
    middle = eco_two/sex_index_m2

    statistic['m_two_eco_sigma'] = round(sigma, 4)
    statistic['m_two_eco_sx'] = round(sx, 4)
    statistic['m_two_eco_cv'] = round(cv, 4)
    statistic['m_two_eco_middle'] = round(middle, 4)

    #SKF
    sigma = math.sqrt(skf_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(skf_two/sex_index_m2))
    middle = skf_two/sex_index_m2

    statistic['m_two_skf_sigma'] = round(sigma, 4)
    statistic['m_two_skf_sx'] = round(sx, 4)
    statistic['m_two_skf_cv'] = round(cv, 4)
    statistic['m_two_skf_middle'] = round(middle, 4)

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(hslpvp_two/sex_index_m2))
    middle = hslpvp_two/sex_index_m2

    statistic['m_two_vp_sigma'] = round(sigma, 4)
    statistic['m_two_vp_sx'] = round(sx, 4)
    statistic['m_two_vp_cv'] = round(cv, 4)
    statistic['m_two_vp_middle'] = round(middle, 4)

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(hslpnp_two/sex_index_m2))
    middle = hslpnp_two/sex_index_m2

    statistic['m_two_np_sigma'] = round(sigma, 4)
    statistic['m_two_np_sx'] = round(sx, 4)
    statistic['m_two_np_cv'] = round(cv, 4)
    statistic['m_two_np_middle'] = round(middle, 4)

    #MOCH
    sigma = math.sqrt(moch_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(moch_two/sex_index_m2))
    middle = moch_two/sex_index_m2

    statistic['m_two_moch_sigma'] = round(sigma, 4)
    statistic['m_two_moch_sx'] = round(sx, 4)
    statistic['m_two_moch_cv'] = round(cv, 4)
    statistic['m_two_moch_middle'] = round(middle, 4)

    #KREAT
    sigma = math.sqrt(kreat_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(kreat_two/sex_index_m2))
    middle = kreat_two/sex_index_m2

    statistic['m_two_kr_sigma'] = round(sigma, 4)
    statistic['m_two_kr_sx'] = round(sx, 4)
    statistic['m_two_kr_cv'] = round(cv, 4)
    statistic['m_two_kr_middle'] = round(middle, 4)

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(bilirubin_two/sex_index_m2))
    middle = bilirubin_two/sex_index_m2

    statistic['m_two_bil_sigma'] = round(sigma, 4)
    statistic['m_two_bil_sx'] = round(sx, 4)
    statistic['m_two_bil_cv'] = round(cv, 4)
    statistic['m_two_bil_middle'] = round(middle, 4)

    #AST
    sigma = math.sqrt(ast_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(ast_two/sex_index_m2))
    middle = ast_two/sex_index_m2

    statistic['m_two_ast_sigma'] = round(sigma, 4)
    statistic['m_two_ast_sx'] = round(sx, 4)
    statistic['m_two_ast_cv'] = round(cv, 4)
    statistic['m_two_ast_middle'] = round(middle, 4)

    #ALT
    sigma = math.sqrt(alt_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(alt_two/sex_index_m2))
    middle = alt_two/sex_index_m2

    statistic['m_two_alt_sigma'] = round(sigma, 4)
    statistic['m_two_alt_sx'] = round(sx, 4)
    statistic['m_two_alt_cv'] = round(cv, 4)
    statistic['m_two_alt_middle'] = round(middle, 4)

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_man_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(glukosa_two/sex_index_m2))
    middle = glukosa_two/sex_index_m2

    statistic['m_two_gl_sigma'] = round(sigma, 4)
    statistic['m_two_gl_sx'] = round(sx, 4)
    statistic['m_two_gl_cv'] = round(cv, 4)
    statistic['m_two_gl_middle'] = round(middle, 4)

    """
    Woman type 2
    """

    #vik
    sigma = math.sqrt(vik_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(vik_twow/sex_index_w2))
    middle = vik_twow/sex_index_w2

    statistic['w_two_sex'] = sex_index_w2
    statistic['w_two_vik_sigma'] = round(sigma, 4)
    statistic['w_two_vik_sx'] = round(sx, 4)
    statistic['w_two_vik_cv'] = round(cv, 4)
    statistic['w_two_vik_middle'] = round(middle, 4)

    #w man
    sigma = math.sqrt(w_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(w_twow/sex_index_w2))
    middle = w_twow/sex_index_w2

    statistic['w_two_w_sigma'] = round(sigma, 4)
    statistic['w_two_w_sx'] = round(sx, 4)
    statistic['w_two_w_cv'] = round(cv, 4)
    statistic['w_two_w_middle'] = round(middle, 4)

    #uo man
    sigma = math.sqrt(uo_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(uo_one/sex_index_w2))
    middle = uo_one/sex_index_w2

    statistic['w_two_uo_sigma'] = round(sigma, 4)
    statistic['w_two_uo_sx'] = round(sx, 4)
    statistic['w_two_uo_cv'] = round(cv, 4)
    statistic['w_two_uo_middle'] = round(middle, 4)

    #economisation
    sigma = math.sqrt(eco_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(eco_twow/sex_index_w2))
    middle = eco_twow/sex_index_w2

    statistic['w_two_eco_sigma'] = round(sigma, 4)
    statistic['w_two_eco_sx'] = round(sx, 4)
    statistic['w_two_eco_cv'] = round(cv, 4)
    statistic['w_two_eco_middle'] = round(middle, 4)

    #SKF
    sigma = math.sqrt(skf_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(skf_twow/sex_index_w2))
    middle = skf_twow/sex_index_w2

    statistic['w_two_skf_sigma'] = round(sigma, 4)
    statistic['w_two_skf_sx'] = round(sx, 4)
    statistic['w_two_skf_cv'] = round(cv, 4)
    statistic['w_two_skf_middle'] = round(middle, 4)

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(hslpvp_twow/sex_index_w2))
    middle = hslpvp_twow/sex_index_w2

    statistic['w_two_vp_sigma'] = round(sigma, 4)
    statistic['w_two_vp_sx'] = round(sx, 4)
    statistic['w_two_vp_cv'] = round(cv, 4)
    statistic['w_two_vp_middle'] = round(middle, 4)

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(hslpnp_twow/sex_index_w2))
    middle = hslpnp_twow/sex_index_w2

    statistic['w_two_np_sigma'] = round(sigma, 4)
    statistic['w_two_np_sx'] = round(sx, 4)
    statistic['w_two_np_cv'] = round(cv, 4)
    statistic['w_two_np_middle'] = round(middle, 4)

    #MOCH
    sigma = math.sqrt(moch_sigma_wom_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(moch_twow/sex_index_w2))
    middle = moch_twow/sex_index_w2

    statistic['w_two_moch_sigma'] = round(sigma, 4)
    statistic['w_two_moch_sx'] = round(sx, 4)
    statistic['w_two_moch_cv'] = round(cv, 4)
    statistic['w_two_moch_middle'] = round(middle, 4)

    #KREAT
    sigma = math.sqrt(kreat_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(kreat_twow/sex_index_w2))
    middle = kreat_twow/sex_index_w2

    statistic['w_two_kr_sigma'] = round(sigma, 4)
    statistic['w_two_kr_sx'] = round(sx, 4)
    statistic['w_two_kr_cv'] = round(cv, 4)
    statistic['w_two_kr_middle'] = round(middle, 4)

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(bilirubin_twow/sex_index_w2))
    middle = bilirubin_twow/sex_index_w2

    statistic['w_two_bil_sigma'] = round(sigma, 4)
    statistic['w_two_bil_sx'] = round(sx, 4)
    statistic['w_two_bil_cv'] = round(cv, 4)
    statistic['w_two_bil_middle'] = round(middle, 4)

    #AST
    sigma = math.sqrt(ast_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(ast_twow/sex_index_w2))
    middle = ast_twow/sex_index_w2

    statistic['w_two_ast_sigma'] = round(sigma, 4)
    statistic['w_two_ast_sx'] = round(sx, 4)
    statistic['w_two_ast_cv'] = round(cv, 4)
    statistic['w_two_ast_middle'] = round(middle, 4)

    #ALT
    sigma = math.sqrt(alt_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(alt_twow/sex_index_w2))
    middle = alt_twow/sex_index_w2

    statistic['w_two_alt_sigma'] = round(sigma, 4)
    statistic['w_two_alt_sx'] = round(sx, 4)
    statistic['w_two_alt_cv'] = round(cv, 4)
    statistic['w_two_alt_middle'] = round(middle, 4)

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(glukosa_twow/sex_index_w2))
    middle = glukosa_twow/sex_index_w2

    statistic['w_two_gl_sigma'] = round(sigma, 4)
    statistic['w_two_gl_sx'] = round(sx, 4)
    statistic['w_two_gl_cv'] = round(cv, 4)
    statistic['w_two_gl_middle'] = round(middle, 4)

    current_user = request.user

    return render_to_response('statistic.html', {'peoples': users, 'profiles': profiles,
                                                 'statistic': statistic, 'current': current_user}, context)