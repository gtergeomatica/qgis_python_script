#( "D46521205_0101_CHM@1" > 0 ) * "D46521205_0101_CHM@1" 
#( "D46521205_0101_CHM@1" < 20 )  * "D46521205_0101_CHM@1"    +  ( "D46521205_0101_CHM@1"  >=  20 ) * 20


processing.run("qgis:rastercalculator", {'EXPRESSION' : '\"D46521205_0101_CHM@1\" > 0',
    'LAYERS' : 'Z:/2019/01_19_RegioneVeneto/dati_lidar_regione/2008_2010_Lidar_TEST/Contratto_140/D46521205_0101_CHM.asc',
    #'TARGET_CRS': self.selectedcrs,
    #'RESAMPLING': 1,
    #'NODATA': None,
    #'DATA_TYPE': 0,
    'OUTPUT': 'C:/Users/roberta/Documents/pippo2.tif'})