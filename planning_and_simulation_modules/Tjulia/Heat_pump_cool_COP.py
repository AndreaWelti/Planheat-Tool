# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:17:20 2018

@author: hrvoj
"""
import numpy as np
import os.path

from ..utility.pvgis.PvgisApi import PvgisApi
from .services.PvgisParamsAdapter import PvgisParamsAdapter

def genera_file_etaHP_cool(val_list=None, input_folder="", output_folder="", item=None):
    max_COP = 10.0

    pvgis_api = PvgisApi()
    pvgis_adapter = PvgisParamsAdapter(pvgis_api)
    pvgis_adapter.update_params(item)
    pvgis_adapter.set_only_ot()
    files = pvgis_api.write_to_files()
    temperature_file = files["ot"]

    if val_list is None:
        return

    ####### Heat pump 1, group 1 COP ########

    #Load meteorological data

    try:
        T_source_1 = np.genfromtxt(input_folder + "\\T_source_HP_cool.csv")
    except OSError:
        T_source_1 = np.genfromtxt(temperature_file)
    T_source_1=T_source_1+273.15
    # Heat sink temperature [°C]
    T_sink1 = val_list[0]
    T_sink_1 = T_sink1 + 273.15
    #Lorenz efficiency
    eta_Lorentz_1= 0.6
    print("eta_Lorentz_1", type(eta_Lorentz_1), eta_Lorentz_1, "T_sink_1", type(T_sink_1), T_sink_1, "T_source_1",
          type(T_source_1), T_source_1)
    eta_HP_1=eta_Lorentz_1*T_sink_1/(T_source_1 - T_sink_1)
    for i in range(len(eta_HP_1)):
        if eta_HP_1[i] > max_COP:
            eta_HP_1[i] = max_COP
    np.savetxt(output_folder + "\\eta_HP_cool.csv", eta_HP_1, delimiter=".")


    ####### Heat pump 2, group 1 COP ########
    #Load meteorological data
    try:
        T_source_2 = np.genfromtxt(input_folder + "\\T_source_HP_cool_2.csv")
    except OSError:
        T_source_2 = np.genfromtxt(temperature_file)
    T_source_2=T_source_2+273.15
    # Heat sink temperature [°C]
    T_sink2 = val_list[2]
    T_sink_2= T_sink2 +273.15
    #Lorenz efficiency
    eta_Lorentz_2= 0.6
    eta_HP_2=eta_Lorentz_2*T_sink_2/(T_source_2 - T_sink_2)
    for i in range(len(eta_HP_2)):
        if eta_HP_2[i] > max_COP:
            eta_HP_2[i] = max_COP

    np.savetxt(output_folder + "\\eta_HP_cool_2.csv", eta_HP_2, delimiter=".")



    ####### Heat pump 3, group 1 COP ########
    #Load meteorological data
    try:
        T_source_3 = np.genfromtxt(input_folder + "\\T_source_HP_cool_3.csv")
    except OSError:
        T_source_3 = np.genfromtxt(temperature_file)
    T_source_3=T_source_3+273.15
    # Heat sink temperature [°C]
    T_sink3 = val_list[4]
    T_sink_3= T_sink3 +273.15
    #Lorenz efficiency
    eta_Lorentz_3= 0.6
    eta_HP_3=eta_Lorentz_3*T_sink_3/(T_source_3 - T_sink_3)
    for i in range(len(eta_HP_3)):
        if eta_HP_3[i] > max_COP:
            eta_HP_3[i] = max_COP

    np.savetxt(output_folder + "\\eta_HP_cool_3.csv", eta_HP_3, delimiter=".")