from qgis.gui import QgsProjectionSelectionDialog

lyr = iface.activeLayer()
crs_select = QgsProjectionSelectionDialog()
crs_select.exec_()
selectedcrsdef = crs_select.crs()
selectedcrs = selectedcrsdef.authid()
epsg_code = selectedcrs.split(":")
code = epsg_code[1]
for f in lyr.getFeatures():
    if code != f["SR_EPSG"]:
        print('diverso')
    else:
        print('uguale')