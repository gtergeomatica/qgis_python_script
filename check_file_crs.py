#processing.run("gdal:translate", {'INPUT': 'C:/Users/user/Desktop/test/D46521204_0101_CHM.tif',
##'TARGET_CRS': 'EPSG:4326',
#'NODATA': None,
#'COPY_SUBDATASETS': False,
#'DATA_TYPE': 0,
#'OUTPUT': 'C:/Users/user/Desktop/test/D46521204_0101_CHM_test3.tif'})

#processing.run("gdal:warpreproject", {'INPUT': 'C:/Users/user/Desktop/test/D46521204_0101_CHM.tif',
#    'SOURCE_CRS': None,
#    'TARGET_CRS': 'EPSG:32632',
#    'RESAMPLING': 1,
#    'NODATA': None,
#    'DATA_TYPE': 0,
#    'OUTPUT': 'C:/Users/user/Desktop/test/D46521204_0101_CHM_test3_crs.tif'})
import gdal    
lyr = iface.activeLayer()
input = 'C:/Users/user/Documents/Regione_veneto\dati\dataset_corso_06_19_venezia\dati_lidar\CAMPAGNA_TEST\Contratto_140/D46521204_0101_DTM.asc'
#input = 'C:/Users/user/Desktop/test/D46521208_0101_CHM.tif'

epsg2 = gdal.Info(input, format='json')
print(epsg2)
epsg = gdal.Info(input, format='json')['coordinateSystem']['wkt'].rsplit('"EPSG","', 1)[-1].split('"')[0]
print(epsg)
for f in lyr.getSelectedFeatures():
    if epsg == f["EPSG_CHM"]:
        print('uguale')
    elif epsg == '':
        print('vuoto')
    else:
        print('non uguale')