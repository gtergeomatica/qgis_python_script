import zipfile
import os
from osgeo import gdal

lyr = iface.activeLayer()
check_dsm = 0
for sf in lyr.getSelectedFeatures():
    check_dsm = 0
    if sf['COMPRESSIO'] == 'zip':
        print('è uno zip')
        dsm_path = sf["P_BASE"] + sf["P_CAMPAGNA"] + sf["P_DSM"]
        dsm_name = sf["N_DSM"].split(".")
        dsm_f_name = dsm_name[0] + '.' + dsm_name[1].replace( dsm_name[1], 'zip')
        print(dsm_f_name)
        dsm_pathfile = os.path.join(dsm_path, dsm_f_name)
        if zipfile.is_zipfile(dsm_pathfile):
            extr = zipfile.ZipFile(dsm_pathfile)
            print(len(extr.namelist()))
            if len(extr.namelist()) > 0:
                extr.extractall(dsm_path)
                check_dsm = 1
                unzipped = []
                for name in extr.namelist():
                    unzipped.append(name)
                print(unzipped)
            else:
                #check_dsm = 0
                print('lo zip è vuoto')
        else:
            print('non trovo lo zip')
        #print(check_dsm)
    else:
        print(sf['COMPRESSIO'])
        
    if check_dsm == 1:
        for rname in unzipped:
            dsm_f_path = os.path.join(dsm_path, rname)
            os.remove(dsm_f_path)