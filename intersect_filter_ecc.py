lyr = QgsProject.instance().mapLayersByName('merge_tile_cortina')[0]
processing.run("native:intersection", {'INPUT': lyr,
    'OVERLAY': lyr,
    'OUTPUT': 'C:/Users/user/Documents/intersect.shp'})