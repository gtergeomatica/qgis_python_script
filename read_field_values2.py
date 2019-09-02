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
query = '"P_DTM" ILIKE \'%2008_2010_Lidar_MATTM%\' and "P_DTM" ILIKE \'%Contratto_140%\''
print(query)
selection =lyr.getFeatures(QgsFeatureRequest().setFilterExpression(query))
lyr.select([k.id() for k in selection])

#for f in lyr.getFeatures():
#    print(type(f["P_DTM"]))
#    if '2008_2010_Lidar_MATTM' in f["P_DTM"]:
#        if 'Contratto_140' in f["P_DTM"]:
#            print('trovati')
#            #fids.append(f.id())
##            try:
#            lyr.select(f.id())
#            if f["P_DTM"] is NULL :
#                print('No DTM found')
##            except:
##                print('No DTM found')
#    #else:
#        #print('NO')
##print(fids)
#lyr.select(fids)
#    for p in pippo:
#        print(p[4])
#fields = [field.name() for field in lyr.fields()]
#print (fields)
#for f in lyr.getSelectedFeatures():
    #print (f["tavola"])
    #if f.fields == 'tavola':
        #print ('è una tavola')