#!/usr/bin/env python
# -*-coding: utf-8 -*-
# csv headers:
# nomer sat dat css
# skf,hslpvp,hslpnp,moch,kreat,bilirubin,ast,alt,glukosa
import csv
from bonobo.ui import setup_x_error_handler
import matplotlib.pyplot as plt
import datetime
import pylab
import math
import numpy as np


def main():
    ifile = open('bio.csv', "rb")
    reader = csv.reader(ifile)

    rownum = 0
    inform = []
    x = []
    labels = []
    explode = []
    width = 0.27

    now_date = datetime.date.today()
    cur_year = now_date.year
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

    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                if header[colnum] == "nomer":
                    inform.append(col)
                if header[colnum] == "sat":
                    inform.append(col)
                if header[colnum] == "dat":
                    inform.append(col)
                if header[colnum] == "css":
                    inform.append(col)
                if header[colnum] == "year":
                    inform.append(col)
                if header[colnum] == "sex":
                    inform.append(col)
                if header[colnum] == "type":
                    inform.append(col)
                if header[colnum] == "skf":
                    inform.append(col)
                if header[colnum] == "hslpvp":
                    inform.append(col)
                if header[colnum] == "hslpnp":
                    inform.append(col)
                if header[colnum] == "moch":
                    inform.append(col)
                if header[colnum] == "kreat":
                    inform.append(col)
                if header[colnum] == "bilirubin":
                    inform.append(col)
                if header[colnum] == "ast":
                    inform.append(col)
                if header[colnum] == "alt":
                    inform.append(col)
                if header[colnum] == "glukosa":
                    inform.append(col)

                colnum += 1
                if colnum == len(row):
                    nomer = inform[0]
                    sat = float(inform[1])
                    dat = float(inform[2])
                    css = float(inform[3])
                    year = int(inform[4])
                    sex = str(inform[5])
                    diabet_type = int(inform[6])
                    skf = float(inform[7])
                    hslpvp = float(inform[8])
                    hslpnp = float(inform[9])
                    moch = float(inform[10])
                    kreat = float(inform[11])
                    bilirubin = float(inform[12])
                    ast = float(inform[13])
                    alt = float(inform[14])
                    glukosa = float(inform[15])

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
                    if diabet_type == 1:
                        #For all
                        index_type_one_all += 1
                        vik_one_all += vik
                        w_one_all += w
                        uo_one_all += uo
                        eco_one_all += economisation

                        if sex == "m":
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

                        if sex == "w":
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

                    #Тип 2
                    if diabet_type == 2:
                        #For All
                        index_type_two_all += 1
                        vik_two_all += vik
                        w_two_all += w
                        uo_two_all += uo
                        eco_two_all += economisation

                        if sex == "m":
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

                        if sex == "w":
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

                    hist = "История болезни №" + str(nomer)
                    """
                    print hist
                    print "ВИК: " + str(vik)
                    print "Коэффициент экономизации кровообращения: " + str(economisation)
                    print "Двойное произведение: " + str(w)
                    print "Ударный объем: " + str(uo)
                    print "Boзвраст: " + str(age)
                    print ""
                    """

                    x.append(-1 * float(vik))
                    labels.append(str(nomer))
                    explode.append(0.05)

                    colnum = 0
                    del inform[:]

        rownum += 1

    #Load our cvs again
    ifile = open('bio.csv', "rb")
    reader = csv.reader(ifile)
    rownum = 0

    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                    if header[colnum] == "nomer":
                        inform.append(col)
                    if header[colnum] == "sat":
                        inform.append(col)
                    if header[colnum] == "dat":
                        inform.append(col)
                    if header[colnum] == "css":
                        inform.append(col)
                    if header[colnum] == "year":
                        inform.append(col)
                    if header[colnum] == "sex":
                        inform.append(col)
                    if header[colnum] == "type":
                        inform.append(col)
                    if header[colnum] == "skf":
                        inform.append(col)
                    if header[colnum] == "hslpvp":
                        inform.append(col)
                    if header[colnum] == "hslpnp":
                        inform.append(col)
                    if header[colnum] == "moch":
                        inform.append(col)
                    if header[colnum] == "kreat":
                        inform.append(col)
                    if header[colnum] == "bilirubin":
                        inform.append(col)
                    if header[colnum] == "ast":
                        inform.append(col)
                    if header[colnum] == "alt":
                        inform.append(col)
                    if header[colnum] == "glukosa":
                        inform.append(col)

                    colnum += 1
                    if colnum == len(row):
                        nomer = inform[0]
                        sat = float(inform[1])
                        dat = float(inform[2])
                        css = float(inform[3])
                        year = int(inform[4])
                        sex = str(inform[5])
                        diabet_type = int(inform[6])
                        skf = float(inform[7])
                        hslpvp = float(inform[8])
                        hslpnp = float(inform[9])
                        moch = float(inform[10])
                        kreat = float(inform[11])
                        bilirubin = float(inform[12])
                        ast = float(inform[13])
                        alt = float(inform[14])
                        glukosa = float(inform[15])

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
                        #Тип 1
                        if diabet_type == 1:
                            if sex == "m":
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

                            if sex == "w":
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
                        if diabet_type == 2:
                            if sex == "m":
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

                            if sex == "w":
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

                        colnum = 0
                        del inform[:]

        rownum += 1

    """
    Man type 1
    """
    #vik man 1
    sigmas_vik = math.sqrt(vik_sigma_man_sum/(sex_index_m-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((sex_index_m-1))
    cv_vik_m_one = (sigmas_vik/(vik_one/sex_index_m))

    print "SIGMA VIK TYPE 1 MAN: " + str(sigmas_vik)
    print "VIK TYPE 1 MAN Sx: " + str(sx_vik_m_one)
    print "VIK TYPE 1 MAN Cv: " + str(cv_vik_m_one)
    print "SA VIK: " + str(vik_one/sex_index_m)

    #w man 1
    sigmas_w = math.sqrt(w_sigma_man_sum/(sex_index_m-1))
    sx_w_m_one = sigmas_w/math.sqrt((sex_index_m-1))
    cv_w_m_one = (sigmas_w/(w_one/sex_index_m))

    print "SIGMA W TYPE 1 MAN: " + str(sigmas_w)
    print "W TYPE 1 MAN Sx: " + str(sx_w_m_one)
    print "W TYPE 1 MAN Cv: " + str(cv_w_m_one)
    print "SA W :" + str(w_one/sex_index_m)

    #uo man 1
    sigmas_uo = math.sqrt(uo_sigma_man_sum/(sex_index_m-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((sex_index_m-1))
    cv_uo_m_one = (sigmas_uo/(uo_one/sex_index_m))

    print "SIGMA UO TYPE 1 MAN: " + str(sigmas_uo)
    print "UO TYPE 1 MAN Sx: " + str(sx_uo_m_one)
    print "UO TYPE 1 MAN Cv: " + str(cv_uo_m_one)
    print "SA UO :" + str(uo_one/sex_index_m)

    #economisation man 1
    sigmas_eco = math.sqrt(eco_sigma_man_sum/(sex_index_m-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((sex_index_m-1))
    cv_eco_m_one = (sigmas_eco/(eco_one/sex_index_m))

    print "SIGMA ECO TYPE 1 MAN: " + str(sigmas_eco)
    print "ECO TYPE 1 MAN Sx: " + str(sx_eco_m_one)
    print "ECO TYPE 1 MAN Cv: " + str(cv_eco_m_one)
    print "SA ECO: "

    #SKF
    sigmas_skf = math.sqrt(skf_sigma_man_sum/(sex_index_m-1))
    sx_skf_m_one = sigmas_skf/math.sqrt((sex_index_m-1))
    cv_skf_m_one = (sigmas_skf/(skf_one/sex_index_m))

    print "SIGMA SKF TYPE 1 MAN: " + str(sigmas_skf)
    print "SKF TYPE 1 MAN Sx: " + str(sx_skf_m_one)
    print "SKF TYPE 1 MAN Cv: " + str(cv_skf_m_one)
    print skf_one/sex_index_m

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(hslpvp_one/sex_index_m))

    print "SIGMA HSLPV TYPE 1 MAN: " + str(sigma)
    print "HSLPV TYPE 1 MAN Sx: " + str(sx)
    print "HSLPV TYPE 1 MAN Cv: " + str(cv)
    print hslpvp_one/sex_index_m

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(hslpnp_one/sex_index_m))

    print "SIGMA HSLNV TYPE 1 MAN: " + str(sigma)
    print "HSLPNV TYPE 1 MAN Sx: " + str(sx)
    print "HSLPNV TYPE 1 MAN Cv: " + str(cv)
    print hslpnp_one/sex_index_m

    #MOCH
    sigma = math.sqrt(moch_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(moch_one/sex_index_m))

    print "SIGMA MOCH TYPE 1 MAN: " + str(sigma)
    print "MOCH TYPE 1 MAN Sx: " + str(sx)
    print "MOCH TYPE 1 MAN Cv: " + str(cv)
    print moch_one/sex_index_m

    #KREAT
    sigma = math.sqrt(kreat_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(kreat_one/sex_index_m))

    print "SIGMA KREAT TYPE 1 MAN: " + str(sigma)
    print "KREAT TYPE 1 MAN Sx: " + str(sx)
    print "KREAT TYPE 1 MAN Cv: " + str(cv)
    print kreat_one/sex_index_m

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(bilirubin_one/sex_index_m))

    print "SIGMA BILIRUBIN TYPE 1 MAN: " + str(sigma)
    print "BILIRUBIN TYPE 1 MAN Sx: " + str(sx)
    print "BILIRUBIN TYPE 1 MAN Cv: " + str(cv)
    print bilirubin_one/sex_index_m

    #AST
    sigma = math.sqrt(ast_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(ast_one/sex_index_m))

    print "SIGMA AST TYPE 1 MAN: " + str(sigma)
    print "AST TYPE 1 MAN Sx: " + str(sx)
    print "AST TYPE 1 MAN Cv: " + str(cv)
    print ast_one/sex_index_m

    #ALT
    sigma = math.sqrt(alt_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(alt_one/sex_index_m))

    print "SIGMA ALT TYPE 1 MAN: " + str(sigma)
    print "ALT TYPE 1 MAN Sx: " + str(sx)
    print "ALT TYPE 1 MAN Cv: " + str(cv)
    print alt_one/sex_index_m

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_man_sum/(sex_index_m-1))
    sx = sigma/math.sqrt((sex_index_m-1))
    cv = (sigma/(glukosa_one/sex_index_m))

    print "SIGMA GLUCOSA TYPE 1 MAN: " + str(sigma)
    print "GLUCOSA TYPE 1 MAN Sx: " + str(sx)
    print "GLUCOSA TYPE 1 MAN Cv: " + str(cv)
    print glukosa_one/sex_index_m

    """
    Woman type 1
    """
    #vik wom 1
    sigmas_vikw = math.sqrt(vik_sigma_wom_sum/(sex_index_w-1))
    sx_vik_m_onew = sigmas_vikw/math.sqrt((sex_index_w-1))
    cv_vik_m_onew = (sigmas_vikw/(vik_onew/sex_index_w))

    print "Wom 1"
    print ""
    print "SIGMA VIK TYPE 1 WOM: " + str(sigmas_vikw)
    print "VIK TYPE 1 WOM Sx: " + str(sx_vik_m_onew)
    print "VIK TYPE 1 WOM Cv: " + str(cv_vik_m_onew)
    print vik_onew/sex_index_w

    #w wom 1
    sigmas_w_w = math.sqrt(w_sigma_wom_sum/(sex_index_w-1))
    sx_w_m_one_w = sigmas_w_w/math.sqrt((sex_index_w-1))
    cv_w_m_one_w = (sigmas_w_w/(w_onew/sex_index_w))

    print "SIGMA W TYPE 1 MAN: " + str(sigmas_w_w)
    print "W TYPE 1 WOM: " + str(sx_w_m_one_w)
    print "W TYPE 1 WOM Cv: " + str(cv_w_m_one_w)
    print w_onew/sex_index_w

    #uo wom 1
    sigmas_uo_w = math.sqrt(uo_sigma_wom_sum/(sex_index_w-1))
    sx_uo_m_one_w = sigmas_uo_w/math.sqrt((sex_index_w-1))
    cv_uo_m_one_w = (sigmas_uo_w/(uo_onew/sex_index_w))

    print "SIGMA UO TYPE 1 WOM: " + str(sigmas_uo_w)
    print "UO TYPE 1 WOM Sx: " + str(sx_uo_m_one_w)
    print "UO TYPE 1 WOM Cv: " + str(cv_uo_m_one_w)
    print uo_onew/sex_index_w

    #economisation wom 1
    sigmas_eco_w = math.sqrt(eco_sigma_wom_sum/(sex_index_w-1))
    sx_eco_m_one_w = sigmas_eco_w/math.sqrt((sex_index_w-1))
    cv_eco_m_one_w = (sigmas_eco_w/(eco_onew/sex_index_w))

    print "SIGMA ECO TYPE 1 WOM: " + str(sigmas_eco_w)
    print "ECO TYPE 1 WOM Sx: " + str(sx_eco_m_one_w)
    print "ECO TYPE 1 WOM Cv: " + str(cv_eco_m_one_w)
    print eco_onew/sex_index_w

    #SKF
    sigmas_skf = math.sqrt(skf_sigma_wom_sum/(sex_index_w-1))
    sx_skf_m_one = sigmas_skf/math.sqrt((sex_index_w-1))
    cv_skf_m_one = (sigmas_skf/(skf_onew/sex_index_w))

    print "SIGMA SKF TYPE 1 WOM: " + str(sigmas_skf)
    print "SKF TYPE 1 WOM Sx: " + str(sx_skf_m_one)
    print "SKF TYPE 1 WOM Cv: " + str(cv_skf_m_one)
    print skf_onew/sex_index_w

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(hslpvp_onew/sex_index_w))

    print "SIGMA HSLPV TYPE 1 WOM: " + str(sigma)
    print "HSLPV TYPE 1 WOM Sx: " + str(sx)
    print "HSLPV TYPE 1 WOM Cv: " + str(cv)
    print hslpvp_onew/sex_index_w

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(hslpnp_onew/sex_index_w))

    print "SIGMA HSLNV TYPE 1 WOM: " + str(sigma)
    print "HSLPNV TYPE 1 WOM Sx: " + str(sx)
    print "HSLPNV TYPE 1 WOM Cv: " + str(cv)
    print hslpnp_onew/sex_index_w

    #MOCH
    sigma = math.sqrt(moch_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(moch_onew/sex_index_w))

    print "SIGMA MOCH TYPE 1 WOM: " + str(sigma)
    print "MOCH TYPE 1 MAN Sx: " + str(sx)
    print "MOCH TYPE 1 MAN Cv: " + str(cv)
    print moch_onew/sex_index_w

    #KREAT
    sigma = math.sqrt(kreat_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(kreat_onew/sex_index_w))

    print "SIGMA KREAT TYPE 1 WOM: " + str(sigma)
    print "KREAT TYPE 1 WOM Sx: " + str(sx)
    print "KREAT TYPE 1 WOM Cv: " + str(cv)
    print kreat_onew/sex_index_w

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(bilirubin_onew/sex_index_w))

    print "SIGMA BILIRUBIN TYPE 1 WOM: " + str(sigma)
    print "BILIRUBIN TYPE 1 WOM Sx: " + str(sx)
    print "BILIRUBIN TYPE 1 WOM Cv: " + str(cv)
    print bilirubin_onew/sex_index_w

    #AST
    sigma = math.sqrt(ast_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(ast_onew/sex_index_w))

    print "SIGMA AST TYPE 1 WOM: " + str(sigma)
    print "AST TYPE 1 WOM Sx: " + str(sx)
    print "AST TYPE 1 WOM Cv: " + str(cv)
    print ast_onew/sex_index_w

    #ALT
    sigma = math.sqrt(alt_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(alt_onew/sex_index_w))

    print "SIGMA ALT TYPE 1 WOM: " + str(sigma)
    print "ALT TYPE 1 WOM Sx: " + str(sx)
    print "ALT TYPE 1 WOM Cv: " + str(cv)
    print alt_onew/sex_index_w

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_wom_sum/(sex_index_w-1))
    sx = sigma/math.sqrt((sex_index_w-1))
    cv = (sigma/(glukosa_onew/sex_index_w))

    print "SIGMA GLUCOSA TYPE 1 WOM: " + str(sigma)
    print "GLUCOSA TYPE 1 WOM Sx: " + str(sx)
    print "GLUCOSA TYPE 1 WOM Cv: " + str(cv)
    print glukosa_onew/sex_index_w

    """
    Man type 2
    """
    #vik man 1
    sigmas_vik = math.sqrt(vik_sigma_man2_sum/(sex_index_m2-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((sex_index_m2-1))
    cv_vik_m_one = (sigmas_vik/(vik_two/sex_index_m2))

    print "SIGMA VIK TYPE 2 MAN: " + str(sigmas_vik)
    print "VIK TYPE 2 MAN Sx: " + str(sx_vik_m_one)
    print "VIK TYPE 2 MAN Cv: " + str(cv_vik_m_one)
    print vik_two/sex_index_m2

    #w man 1
    sigmas_w = math.sqrt(w_sigma_man2_sum/(sex_index_m2-1))
    sx_w_m_one = sigmas_w/math.sqrt((sex_index_m2-1))
    cv_w_m_one = (sigmas_w/(w_two/sex_index_m2))

    print "SIGMA W TYPE 2 MAN: " + str(sigmas_w)
    print "W TYPE 2 MAN Sx: " + str(sx_w_m_one)
    print "W TYPE 2 MAN Cv: " + str(cv_w_m_one)
    print w_two/sex_index_m2

    #uo man 1
    sigmas_uo = math.sqrt(uo_sigma_man2_sum/(sex_index_m2-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((sex_index_m2-1))
    cv_uo_m_one = (sigmas_uo/(uo_two/sex_index_m2))

    print "SIGMA UO TYPE 2 MAN: " + str(sigmas_uo)
    print "UO TYPE 2 MAN Sx: " + str(sx_uo_m_one)
    print "UO TYPE 2 MAN Cv: " + str(cv_uo_m_one)
    print uo_two/sex_index_m2

    #economisation man 1
    sigmas_eco = math.sqrt(eco_sigma_man2_sum/(sex_index_m2-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((sex_index_m2-1))
    cv_eco_m_one = (sigmas_eco/(eco_two/sex_index_m2))

    print "SIGMA ECO TYPE 2 MAN: " + str(sigmas_eco)
    print "ECO TYPE 2 MAN Sx: " + str(sx_eco_m_one)
    print "ECO TYPE 2 MAN Cv: " + str(cv_eco_m_one)
    print eco_two/sex_index_m2

    #SKF
    sigmas_skf = math.sqrt(skf_sigma_man2_sum/(sex_index_m2-1))
    sx = sigmas_skf/math.sqrt((sex_index_m2-1))
    cv = (sigmas_skf/(skf_two/sex_index_m2))

    print "SIGMA SKF TYPE 2 MAN: " + str(sigmas_skf)
    print "SKF TYPE 2 MAN Sx: " + str(sx)
    print "SKF TYPE 2 MAN Cv: " + str(cv)
    print skf_two/sex_index_m2

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(hslpvp_two/sex_index_m2))

    print "SIGMA HSLPV TYPE 2 MAN: " + str(sigma)
    print "HSLPV TYPE 2 MAN Sx: " + str(sx)
    print "HSLPV TYPE 2 MAN Cv: " + str(cv)
    print hslpvp_two/sex_index_m2

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(hslpnp_two/sex_index_m2))

    print "SIGMA HSLNV TYPE 2 MAN: " + str(sigma)
    print "HSLPNV TYPE 2 MAN Sx: " + str(sx)
    print "HSLPNV TYPE 2 MAN Cv: " + str(cv)
    print hslpnp_two/sex_index_m2

    #MOCH
    sigma = math.sqrt(moch_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(moch_two/sex_index_m2))

    print "SIGMA MOCH TYPE 2 MAN: " + str(sigma)
    print "MOCH TYPE 2 MAN Sx: " + str(sx)
    print "MOCH TYPE 2 MAN Cv: " + str(cv)
    print moch_two/sex_index_m2

    #KREAT
    sigma = math.sqrt(kreat_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(kreat_two/sex_index_m2))

    print "SIGMA KREAT TYPE 2 MAN: " + str(sigma)
    print "KREAT TYPE 2 MAN Sx: " + str(sx)
    print "KREAT TYPE 2 MAN Cv: " + str(cv)
    print kreat_two/sex_index_m2

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(bilirubin_two/sex_index_m2))

    print "SIGMA BILIRUBIN TYPE 2 MAN: " + str(sigma)
    print "BILIRUBIN TYPE 2 MAN Sx: " + str(sx)
    print "BILIRUBIN TYPE 2 MAN Cv: " + str(cv)
    print bilirubin_two/sex_index_m2

    #AST
    sigma = math.sqrt(ast_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(ast_two/sex_index_m2))

    print "SIGMA AST TYPE 1 MAN: " + str(sigma)
    print "AST TYPE 1 MAN Sx: " + str(sx)
    print "AST TYPE 1 MAN Cv: " + str(cv)
    print ast_two/sex_index_m2

    #ALT
    sigma = math.sqrt(alt_sigma_man2_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(alt_two/sex_index_m2))

    print "SIGMA ALT TYPE 2 MAN: " + str(sigma)
    print "ALT TYPE 2 MAN Sx: " + str(sx)
    print "ALT TYPE 2 MAN Cv: " + str(cv)
    print alt_two/sex_index_m2

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_man_sum/(sex_index_m2-1))
    sx = sigma/math.sqrt((sex_index_m2-1))
    cv = (sigma/(glukosa_two/sex_index_m2))

    print "SIGMA GLUCOSA TYPE 2 MAN: " + str(sigma)
    print "GLUCOSA TYPE 2 MAN Sx: " + str(sx)
    print "GLUCOSA TYPE 2 MAN Cv: " + str(cv)
    print glukosa_two/sex_index_m2

    """
    Woman type 2
    """
    #vik
    sigmas_vik = math.sqrt(vik_sigma_wom2_sum/(sex_index_w2-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((sex_index_w2-1))
    cv_vik_m_one = (sigmas_vik/(vik_twow/sex_index_w2))

    print "SIGMA VIK TYPE 2 WOM: " + str(sigmas_vik)
    print "VIK TYPE 2 WOM Sx: " + str(sx_vik_m_one)
    print "VIK TYPE 2 WOM Cv: " + str(cv_vik_m_one)
    print vik_twow/sex_index_w2

    #w man
    sigmas_w = math.sqrt(w_sigma_wom2_sum/(sex_index_w2-1))
    sx_w_m_one = sigmas_w/math.sqrt((sex_index_w2-1))
    cv_w_m_one = (sigmas_w/(w_twow/sex_index_w2))

    print "SIGMA W TYPE 2 WOM: " + str(sigmas_w)
    print "W TYPE 2 WOM Sx: " + str(sx_w_m_one)
    print "W TYPE 2 WOM Cv: " + str(cv_w_m_one)
    print w_twow/sex_index_w2

    #uo man
    sigmas_uo = math.sqrt(uo_sigma_wom2_sum/(sex_index_w2-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((sex_index_w2-1))
    cv_uo_m_one = (sigmas_uo/(uo_one/sex_index_w2))

    print "SIGMA UO TYPE 2 WOM: " + str(sigmas_uo)
    print "UO TYPE 2 WOM Sx: " + str(sx_uo_m_one)
    print "UO TYPE 2 WOM Cv: " + str(cv_uo_m_one)
    print uo_one/sex_index_w2

    #economisation
    sigmas_eco = math.sqrt(eco_sigma_wom2_sum/(sex_index_w2-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((sex_index_w2-1))
    cv_eco_m_one = (sigmas_eco/(eco_twow/sex_index_w2))

    print "SIGMA ECO TYPE 2 WOM: " + str(sigmas_eco)
    print "ECO TYPE 2 WOM Sx: " + str(sx_eco_m_one)
    print "ECO TYPE 2 WOM Cv: " + str(cv_eco_m_one)
    print eco_twow/sex_index_w2

    #SKF
    sigmas_skf = math.sqrt(skf_sigma_wom2_sum/(sex_index_w2-1))
    sx_skf_m_one = sigmas_skf/math.sqrt((sex_index_w2-1))
    cv_skf_m_one = (sigmas_skf/(skf_twow/sex_index_w2))

    print "SIGMA SKF TYPE 2 WOM: " + str(sigmas_skf)
    print "SKF TYPE 2 WOM Sx: " + str(sx_skf_m_one)
    print "SKF TYPE 2 WOM Cv: " + str(cv_skf_m_one)
    print skf_twow/sex_index_w2

    #HSLPVP
    sigma = math.sqrt(hslpvp_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(hslpvp_twow/sex_index_w2))

    print "SIGMA HSLPV TYPE 2 WOM: " + str(sigma)
    print "HSLPV TYPE 2 WOM Sx: " + str(sx)
    print "HSLPV TYPE 2 WOM Cv: " + str(cv)
    print hslpvp_twow/sex_index_w2

    #HSLPNP
    sigma = math.sqrt(hslpnp_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(hslpnp_twow/sex_index_w2))

    print "SIGMA HSLNV TYPE 2 WOM: " + str(sigma)
    print "HSLPNV TYPE 2 WOM Sx: " + str(sx)
    print "HSLPNV TYPE 2 WOM Cv: " + str(cv)
    print hslpnp_twow/sex_index_w2

    #MOCH
    sigma = math.sqrt(moch_sigma_wom_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(moch_twow/sex_index_w2))

    print "SIGMA MOCH TYPE 2 WOM: " + str(sigma)
    print "MOCH TYPE 2 MAN Sx: " + str(sx)
    print "MOCH TYPE 2 MAN Cv: " + str(cv)
    print moch_twow/sex_index_w2

    #KREAT
    sigma = math.sqrt(kreat_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(kreat_twow/sex_index_w2))

    print "SIGMA KREAT TYPE 2 WOM: " + str(sigma)
    print "KREAT TYPE 2 WOM Sx: " + str(sx)
    print "KREAT TYPE 2 WOM Cv: " + str(cv)
    print kreat_twow/sex_index_w2

    #BILIRUBIN
    sigma = math.sqrt(bilirubin_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(bilirubin_twow/sex_index_w2))

    print "SIGMA BILIRUBIN TYPE 2 WOM: " + str(sigma)
    print "BILIRUBIN TYPE 2 WOM Sx: " + str(sx)
    print "BILIRUBIN TYPE 2 WOM Cv: " + str(cv)
    print bilirubin_twow/sex_index_w2

    #AST
    sigma = math.sqrt(ast_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(ast_twow/sex_index_w2))

    print "SIGMA AST TYPE 2 WOM: " + str(sigma)
    print "AST TYPE 2 WOM Sx: " + str(sx)
    print "AST TYPE 2 WOM Cv: " + str(cv)
    print ast_twow/sex_index_w2

    #ALT
    sigma = math.sqrt(alt_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(alt_twow/sex_index_w2))

    print "SIGMA ALT TYPE 2 WOM: " + str(sigma)
    print "ALT TYPE 2 WOM Sx: " + str(sx)
    print "ALT TYPE 2 WOM Cv: " + str(cv)
    print alt_twow/sex_index_w2

    #GLUCOSA
    sigma = math.sqrt(glukosa_sigma_wom2_sum/(sex_index_w2-1))
    sx = sigma/math.sqrt((sex_index_w2-1))
    cv = (sigma/(glukosa_twow/sex_index_w2))

    print "SIGMA GLUCOSA TYPE 2 WOM: " + str(sigma)
    print "GLUCOSA TYPE 2 WOM Sx: " + str(sx)
    print "GLUCOSA TYPE 2 WOM Cv: " + str(cv)
    print glukosa_twow/sex_index_w2

    """
    print "----------------Среднее арифметическое Тип 1 Мужчины-------------------------"
    print ""
    print "ВИК(индекс Кердо) ср. тип 1: " + str(vik_one / sex_index_m)
    print "Двойное произведение ср. тип 1: " + str(w_one / sex_index_m)
    print "Ударный объем ср. тип 1: " + str(uo_one / sex_index_m)
    print "Коэффициент экономизации кровообращения ср. тип 1: " + str(eco_one / sex_index_m)
    print "Man: " + str(sex_index_m)
    print ""

    print "----------------Среднее арифметическое Тип 1 Женщины-------------------------"
    print ""
    print "ВИК(индекс Кердо) ср. тип 1: " + str(vik_one / sex_index_w)
    print "Двойное произведение ср. тип 1: " + str(w_one / sex_index_w)
    print "Ударный объем ср. тип 1: " + str(uo_one / sex_index_w)
    print "Коэффициент экономизации кровообращения ср. тип 1: " + str(eco_one / sex_index_w)
    print "Woman: " + str(sex_index_w)
    print ""

    print "----------------Среднее арифметическое Тип 2 Мужчины-------------------------"
    print ""
    print "ВИК(индекс Кердо) ср. тип 2: " + str(vik_two / sex_index_m2)
    print "Двойное произведение ср. тип 2: " + str(w_two / sex_index_m2)
    print "Ударный объем ср. тип 2: " + str(uo_two / sex_index_m2)
    print "Коэффициент экономизации кровообращения ср. тип 2: " + str(eco_two / sex_index_m2)
    print "Man: " + str(sex_index_m2)
    print ""

    print "----------------Среднее арифметическое Тип 2 Женщины-------------------------"
    print ""
    print "ВИК(индекс Кердо) ср. тип 2: " + str(vik_two / sex_index_w2)
    print "Двойное произведение ср. тип 2: " + str(w_two / sex_index_w2)
    print "Ударный объем ср. тип 2: " + str(uo_two / sex_index_w2)
    print "Коэффициент экономизации кровообращения ср. тип 2: " + str(eco_two / sex_index_w2)
    print "Woman: " + str(sex_index_w2)
    """
    plt.pie(x, explode=explode, labels=labels, shadow=True)
    #plt.show()

    ifile.close()


if __name__ == '__main__':
    main()