#lyr = iface.activeLayer()
#ras_prov = lyr.dataProvider()
#QgsRasterDataProvider.fileRasterFilters(ras_prov)
#
import gdal

#gdal.AllRegister()
#print(gdal.AllRegister())
for i in range(0, gdal.GetDriverCount()):
    drv = gdal.GetDriver(i)
    #print(drv)
    drv_meta = drv.GetMetadata()
    if 'DMD_EXTENSION' in drv_meta:
        #print ("{}: .{}".format(drv_meta['DMD_LONGNAME'], drv_meta['DMD_EXTENSION']))
        print ("{}: .{}".format(drv.LongName, drv_meta['DMD_EXTENSION']))
        
#for i in range(gdal.GetDriverCount()):
#    drv = gdal.GetDriver(i)
#    if drv.GetMetadataItem(gdal.DCAP_RASTER):
#        print(drv.GetMetadataItem(gdal.DMD_LONGNAME), drv.GetMetadataItem(gdal.DMD_EXTENSIONS))