lyr = iface.activeLayer()
print (lyr.name())
#idx = lyr.dataProvider().fieldNameIndex('P_DSM')
#values = lyr.uniqueValues(idx)
#print(values)
#for v in values:
#    #print(v.type())
##for uv in values:
#    print (v)
#    pippo = v.split("/")
#    print(pippo[4])
#print(values)

uniquevalues = []
print(uniquevalues)
uniqueprovider = lyr.dataProvider()
fields = uniqueprovider.fields()
id = fields.indexFromName('P_DSM')
uniquevalues = list(uniqueprovider.uniqueValues( id ))
#print(len(uniquevalues))
pluto = []
for uv in uniquevalues:
    #print (uv)
    #pippo = r'{}'.format(uv)
    #print (pippo)
#    pippo = str(uv)
    #print (pippo)
    #pippo2 = str(uv).replace("\", )
    pippo2 = str(uv).split("\\")
    #print (pippo2)
    if len(pippo2) > 4:
        pluto.append(pippo2[5] + '-' + pippo2[6])
print (pluto)
#fids = []
for f in lyr.getFeatures():
    #print(type(f["P_DTM"]))
    if f["P_DTM"] == NULL :
        print('no DTM')
    elif '2008_2010_Lidar_TEST' in f["P_DTM"]:
        if 'Contratto_140' in f["P_DTM"]:
            #print('trovati')
#            #fids.append(f.id())
##            try:
            lyr.select(f.id())
            

lyr.startEditing()
for sf in lyr.getSelectedFeatures():
    print(sf_id)
    print(field_id)
    if sf["P_CHM"] != NULL:
        print(sf["P_CHM"])
        chm_pathfile = sf["P_CHM"] + '\\' + sf["N_CHM"]
        print(chm_pathfile)
        lyr_chm = QgsRasterLayer(chm_pathfile, sf["N_CHM"])
        QgsProject.instance().addMapLayers([lyr_chm])
    else:
        entries = []
        sf_id = sf.id()
        field_id = sf.fields().indexFromName('P_CHM')
        dsm_pathfile = sf["P_DSM"] + '\\' + sf["N_DSM"]
        dtm_pathfile = sf["P_DTM"] + '\\' + sf["N_DTM"]
        lyr_dsm = QgsRasterLayer(dsm_pathfile, sf["N_DSM"])
        lyr_dtm = QgsRasterLayer(dtm_pathfile, sf["N_DTM"])
        #QgsProject.instance().addMapLayers([lyr_dsm])
        #QgsProject.instance().addMapLayers([lyr_dtm])
        chm_name = sf["N_DTM"].split(".")
        print(chm_name[0])
        if 'DTM' in chm_name[0]:
            chm_file = chm_name[0].replace('DTM', 'CHM')
            print(chm_file)
        elif 'dtm' in chm_name[0]:
            chm_file = chm_name[0].replace('dtm', 'chm')
        elif 'ground' in chm_name[0]:
            chm_file = chm_name[0].replace('ground', 'chm')
        else:
            chm_file = chm_name[0] + '_CHM'
            
        lyr.changeAttributeValue(sf_id, field_id, "pippo")
lyr.commitChanges()
        #print(chm_name[0])
#        ras1 = QgsRasterCalculatorEntry()
#        ras1.ref = '{}@1'.format(sf["N_DSM"])
#        ras1.raster = lyr_dsm
#        ras1.bandNumber = 1
#        entries.append(ras1)
#        print(ras1)
#
#        ras2 = QgsRasterCalculatorEntry()
#        ras2.ref = '{}@1'.format(sf["N_DTM"])
#        ras2.raster = lyr_dtm
#        ras2.bandNumber = 1
#        entries.append(ras2)
#
#        print(ras2)
#        print(entries)
#
#        calc = QgsRasterCalculator('{}@1 - {}@1'.format(sf["N_DSM"], sf["N_DTM"]), 'C:/Users/roberta/Desktop/{}_CHM.tif'.format(sf["N_DTM"]), 'GTiff', lyr_dsm.extent(), lyr_dsm.width(), lyr_dsm.height(), entries)
#        calc.processCalculation()


    #else:
        #print('NO')
#print(fids)
#lyr.select(fids)
#    for p in pippo:
#        print(p[4])
#fields = [field.name() for field in lyr.fields()]
#print (fields)
#for f in lyr.getSelectedFeatures():
    #print (f["tavola"])
    #if f.fields == 'tavola':
        #print ('è una tavola')