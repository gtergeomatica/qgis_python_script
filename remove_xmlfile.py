import os
path = 'Z:/2019/01_19_RegioneVeneto/dati_lidar_regione/2008_2010_Lidar_TEST/Contratto_140'
#os.remove('Z:/2019/01_19_RegioneVeneto/dati_lidar_regione/2008_2010_Lidar_TEST/Contratto_140/D46521205_0101_CHM.asc.aux.xml')
#print(os.listdir(path))
for xml in os.listdir(path):
    if xml.endswith('.aux.xml'):
        fullpath = os.path.join(path, xml)
##text_files = [f for f in os.listdir(path) if f.endswith('.aux.xml')]
##print(text_files)
        print(fullpath)
        os.remove(fullpath)
#    else:
#        print('non ce ne sono')