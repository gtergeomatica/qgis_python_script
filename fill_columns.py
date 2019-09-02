lyr = iface.activeLayer()

#LA COLONNA P_BASE L'HO RIEMPITA DA QGIS CON CALC CAMPI
#SEMPLICEMENTE SCRIVENDO LA STRINGA 
#'\\\\192.168.2.15\\lavori\\2019\\01_19_RegioneVeneto\\dati_lidar_regione'

#RIEMPO COLONNA CAMPAGNA
#for f in lyr.getFeatures():
#    f_id = f.id()
#    pfield_id = f.fields().indexFromName('P_CAMPAGNA')
#    str_values = str(f["P_CAMPAGNA"]).split("\\")
#    if len(str_values) > 1:
#        values = (str_values[1] + '\\' + str_values[2])
#        lyr.changeAttributeValue(f_id, pfield_id, values)

#RIEMPO COLONNA P_DTM O P_DSM
#for f in lyr.getFeatures():
#    f_id = f.id()
#    pfield_id = f.fields().indexFromName('P_DSM')
#    str_values = str(f["P_BASE"]) + str(f["P_CAMPAGNA"])
#    #print (str_values)
#    ok = str(f["P_DSM"]).replace(str_values, '')
#    #print (ok)
#    lyr.changeAttributeValue(f_id, pfield_id, ok)

#cambio valore COLONNA N_DTM O N_DSM per una campagna
#for f in lyr.getSelectedFeatures():
#    f_id = f.id()
#    pfield_id = f.fields().indexFromName('N_DTM')
#    str_values = str(f["N_DTM"]).split(".")
#    #if len(str_values) > 1:
#    values = (str_values[0] + '_GAU' + '.' + str_values[1])
#    lyr.changeAttributeValue(f_id, pfield_id, values)

#cambio valore COLONNA N_DTM O N_DSM per una campagna
for f in lyr.getSelectedFeatures():
    f_id = f.id()
    pfield_id = f.fields().indexFromName('N_DSM')
    str_values = str(f["N_DSM"]).split("__")
    if len(str_values) > 1:
        #print(str_values)
        values = (str_values[0] + '_' + str_values[1])
        #print(values)
        lyr.changeAttributeValue(f_id, pfield_id, values)