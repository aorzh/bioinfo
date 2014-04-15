#!/usr/bin/env python
# -*-coding: utf-8 -*-
# csv headers:
# nomer sat dat css
import csv
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import math
import datetime


def main():
    root = Tk()

    op = askopenfilename()

    ifile = open(op, "rb")
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

    vik_sigma_wom_sum = int()
    w_sigma_wom_sum = int()
    uo_sigma_wom_sum = int()
    eco_sigma_wom_sum = int()

    vik_sigma_man2_sum = int()
    w_sigma_man2_sum = int()
    uo_sigma_man2_sum = int()
    eco_sigma_man2_sum = int()

    vik_sigma_wom2_sum = int()
    w_sigma_wom2_sum = int()
    uo_sigma_wom2_sum = int()
    eco_sigma_wom2_sum = int()

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

                colnum += 1
                if colnum == len(row):
                    nomer = inform[0]
                    sat = float(inform[1])
                    dat = float(inform[2])
                    css = float(inform[3])
                    year = int(inform[4])
                    sex = str(inform[5])
                    diabet_type = int(inform[6])
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

                        if sex == "w":
                            vik_onew += vik
                            w_onew += w
                            uo_onew += uo
                            eco_onew += economisation
                            sex_index_w += 1
                            index_type_one_w += 1

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

                        if sex == "w":
                            vik_twow += vik
                            w_twow += w
                            uo_twow += uo
                            eco_twow += economisation
                            sex_index_w2 += 1
                            index_type_two_w += 1

                    x.append(-1 * float(vik))
                    labels.append(str(nomer))
                    explode.append(0.05)

                    colnum = 0
                    del inform[:]

        rownum += 1

    #Load our cvs again (I don't know, why)
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

                colnum += 1
                if colnum == len(row):
                    nomer = inform[0]
                    sat = float(inform[1])
                    dat = float(inform[2])
                    css = float(inform[3])
                    year = int(inform[4])
                    sex = str(inform[5])
                    diabet_type = int(inform[6])
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
                            vik_sigma_man_sum += (abs(vik_one) - abs(vik)) ** 2
                            #W sigma
                            w_sigma_man_sum += (abs(w_one) - abs(w)) ** 2
                            #uo sigma
                            uo_sigma_man_sum = (abs(uo_one) - abs(uo)) ** 2
                            #eco sigma
                            eco_sigma_man_sum = (abs(eco_one) - abs(economisation)) ** 2

                        if sex == "w":
                            #vik sigma
                            vik_sigma_wom_sum += (abs(vik_onew) - abs(vik)) ** 2
                            #W sigma
                            w_sigma_wom_sum += (abs(w_onew) - abs(w)) ** 2
                            #uo sigma
                            uo_sigma_wom_sum = (abs(uo_onew) - abs(uo)) ** 2
                            #eco sigma
                            eco_sigma_wom_sum = (abs(eco_onew) - abs(economisation)) ** 2

                    #Тип 2
                    if diabet_type == 2:
                        if sex == "m":
                            #vik sigma
                            vik_sigma_man2_sum += (abs(vik_two) - abs(vik)) ** 2
                            #W sigma
                            w_sigma_man2_sum += (abs(w_two) - abs(w)) ** 2
                            #uo sigma
                            uo_sigma_man2_sum = (abs(uo_two) - abs(uo)) ** 2
                            #eco sigma
                            eco_sigma_man2_sum = (abs(eco_two) - abs(economisation)) ** 2
                        if sex == "w":
                            #vik sigma
                            vik_sigma_wom2_sum += (abs(vik_twow) - abs(vik)) ** 2
                            #W sigma
                            w_sigma_wom2_sum += (abs(w_twow) - abs(w)) ** 2
                            #uo sigma
                            uo_sigma_wom2_sum = (abs(uo_twow) - abs(uo)) ** 2
                            #eco sigma
                            eco_sigma_wom2_sum = (abs(eco_twow) - abs(economisation)) ** 2

                    colnum = 0
                    del inform[:]

        rownum += 1

    txt = Text(root, width=400, height=150, font="11")

    """
    Man type 1
    """
    txt.insert(END, "MAN 1 \n")
    #vik man 1
    sigmas_vik = math.sqrt(vik_sigma_man_sum/(index_type_one-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((index_type_one-1))
    cv_vik_m_one = (sigmas_vik/vik_one)/100

    txt.insert(END, "VIK TYPE 1 MAN Sx: " + str(sx_vik_m_one) + "\n")
    txt.insert(END, "VIK TYPE 1 MAN Sx: " + str(cv_vik_m_one) + "\n")

    #w man 1
    sigmas_w = math.sqrt(w_sigma_man_sum/(index_type_one-1))
    sx_w_m_one = sigmas_w/math.sqrt((index_type_one-1))
    cv_w_m_one = (sigmas_w/w_one)/100

    txt.insert(END, "W TYPE 1 MAN Sx: " + str(sx_w_m_one) + "\n")
    txt.insert(END, "W TYPE 1 MAN Cv: " + str(cv_w_m_one) + "\n")

    #uo man 1
    sigmas_uo = math.sqrt(uo_sigma_man_sum/(index_type_one-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((index_type_one-1))
    cv_uo_m_one = (sigmas_uo/uo_one)/100

    txt.insert(END, "UO TYPE 1 MAN Sx: " + str(sx_uo_m_one) + "\n")
    txt.insert(END, "UO TYPE 1 MAN Cv: " + str(cv_uo_m_one) + "\n")

    #economisation man 1
    sigmas_eco = math.sqrt(eco_sigma_man_sum/(index_type_one-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((index_type_one-1))
    cv_eco_m_one = (sigmas_eco/eco_one)/100

    txt.insert(END, "Eco TYPE 1 MAN Sx: " + str(sx_eco_m_one) + "\n")
    txt.insert(END, "Eco TYPE 1 MAN Cv: " + str(cv_eco_m_one) + "\n")

    """
    Woman type 1
    """
    txt.insert(END, "WOMAN 1 \n")
    #vik wom 1
    sigmas_vikw = math.sqrt(vik_sigma_wom_sum/(index_type_one_w-1))
    sx_vik_m_onew = sigmas_vikw/math.sqrt((index_type_one_w-1))
    cv_vik_m_onew = (sigmas_vikw/vik_onew)/100

    txt.insert(END, "VIK TYPE 1 WOMAN Sx: " + str(sx_vik_m_onew) + "\n")
    txt.insert(END, "VIK TYPE 1 WOMAN Cv: " + str(cv_vik_m_onew) + "\n")

    #w wom 1
    sigmas_w_w = math.sqrt(w_sigma_wom_sum/(index_type_one_w-1))
    sx_w_m_one_w = sigmas_w_w/math.sqrt((index_type_one_w-1))
    cv_w_m_one_w = (sigmas_w_w/w_onew)/100

    txt.insert(END, "W TYPE 1 WOMAN Sx: " + str(sx_w_m_one_w) + "\n")
    txt.insert(END, "W TYPE 1 WOMAN Cv: " + str(cv_w_m_one_w) + "\n")

    #uo wom 1
    sigmas_uo_w = math.sqrt(uo_sigma_wom_sum/(index_type_one_w-1))
    sx_uo_m_one_w = sigmas_uo_w/math.sqrt((index_type_one_w-1))
    cv_uo_m_one_w = (sigmas_uo_w/uo_onew)/100

    txt.insert(END, "UO TYPE 1 WOMAN Sx: " + str(sx_uo_m_one_w) + "\n")
    txt.insert(END, "UO TYPE 1 WOMAN Cv: " + str(cv_uo_m_one_w) + "\n")

    #economisation wom 1
    sigmas_eco_w = math.sqrt(eco_sigma_wom_sum/(index_type_one_w-1))
    sx_eco_m_one_w = sigmas_eco_w/math.sqrt((index_type_one_w-1))
    cv_eco_m_one_w = (sigmas_eco_w/eco_onew)/100

    txt.insert(END, "Eco TYPE 1 WOMAN Sx: " + str(sx_eco_m_one_w) + "\n")
    txt.insert(END, "Eco TYPE 1 WOMAN Cv: " + str(cv_eco_m_one_w) + "\n")

    """
    Man type 2
    """
    txt.insert(END, "MAN TYPE 2 \n")
    sigmas_vik = math.sqrt(vik_sigma_man2_sum/(index_type_two-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((index_type_two-1))
    cv_vik_m_one = (sigmas_vik/vik_two)/100

    txt.insert(END, "VIK TYPE 2 MAN Sx: " + str(sx_vik_m_one) + "\n")
    txt.insert(END, "VIK TYPE 2 MAN Cv: " + str(cv_vik_m_one) + "\n")

    #w man 1
    sigmas_w = math.sqrt(w_sigma_man2_sum/(index_type_two-1))
    sx_w_m_one = sigmas_w/math.sqrt((index_type_two-1))
    cv_w_m_one = (sigmas_w/w_two)/100

    txt.insert(END, "W TYPE 2 MAN Sx: " + str(sx_w_m_one) + "\n")
    txt.insert(END, "W TYPE 2 MAN Cv: " + str(cv_w_m_one) + "\n")

    #uo man 1
    sigmas_uo = math.sqrt(uo_sigma_man2_sum/(index_type_two-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((index_type_two-1))
    cv_uo_m_one = (sigmas_uo/uo_two)/100

    txt.insert(END, "UO TYPE 1 MAN Sx: " + str(sx_uo_m_one) + "\n")
    txt.insert(END, "UO TYPE 1 MAN Cv: " + str(cv_uo_m_one) + "\n")

    #economisation man 1
    sigmas_eco = math.sqrt(eco_sigma_man2_sum/(index_type_two-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((index_type_two-1))
    cv_eco_m_one = (sigmas_eco/eco_two)/100

    txt.insert(END, "Eco TYPE 2 MAN Sx: " + str(sx_eco_m_one) + "\n")
    txt.insert(END, "Eco TYPE 2 MAN Cv: " + str(cv_eco_m_one) + "\n")

    """
    Woman type 2
    """
    txt.insert(END, "WOMAN TYPE 2 \n")
    #vik man 1
    sigmas_vik = math.sqrt(vik_sigma_wom2_sum/(index_type_two-1))
    sx_vik_m_one = sigmas_vik/math.sqrt((index_type_two-1))
    cv_vik_m_one = (sigmas_vik/vik_twow)/100

    txt.insert(END, "VIK TYPE 2 WOMAN Sx: " + str(sx_vik_m_one) + "\n")
    txt.insert(END, "VIK TYPE 2 WoMAN Cv: " + str(cv_vik_m_one) + "\n")

    #w man 1
    sigmas_w = math.sqrt(w_sigma_wom2_sum/(index_type_two-1))
    sx_w_m_one = sigmas_w/math.sqrt((index_type_two-1))
    cv_w_m_one = (sigmas_w/w_twow)/100

    txt.insert(END, "W TYPE 2 WOMAN Sx: " + str(sx_w_m_one) + "\n")
    txt.insert(END, "W TYPE 2 WOMAN Cv: " + str(cv_w_m_one) + "\n")

    #uo man 1
    sigmas_uo = math.sqrt(uo_sigma_wom2_sum/(index_type_two-1))
    sx_uo_m_one = sigmas_uo/math.sqrt((index_type_two-1))
    cv_uo_m_one = (sigmas_uo/uo_twow)/100

    txt.insert(END, "UO TYPE 2 WOMAN Sx: " + str(sx_uo_m_one) + "\n")
    txt.insert(END, "UO TYPE 2 WOMAN Cv: " + str(cv_uo_m_one) + "\n")

    sigmas_eco = math.sqrt(eco_sigma_wom2_sum/(index_type_two-1))
    sx_eco_m_one = sigmas_eco/math.sqrt((index_type_two-1))
    cv_eco_m_one = (sigmas_eco/eco_twow)/100

    txt.insert(END, "Eco TYPE 2 WOMAN Sx: " + str(sx_eco_m_one) + "\n")
    txt.insert(END, "Eco TYPE 2 WOMAN Cv: " + str(cv_eco_m_one) + "\n")

    ifile.close()

    txt.pack()
    root.mainloop()

if __name__ == '__main__':
    main()