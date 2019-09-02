from osgeo import gdal, osr
import os

#dtm_pathfile = os.path.join(dtm_path, sf["N_DTM"])
datafile = gdal.Open("Z:/2019/01_19_RegioneVeneto/tileMaker_plugin/dataset/fascia_costiera/DTM/427030_22_WGS.ASC")

cols = datafile.RasterXSize
rows = datafile.RasterYSize
bands = datafile.RasterCount

print ("Number of columns: " + str(cols))
print ("Number of rows: " + str(rows))
print ("Number of bands: " + str(bands))

gt = datafile.GetGeoTransform()
print (gt)

pippo = gdal.Info(datafile)
print(pippo)
pluto = pippo.split('\n')
print(pluto)