# Riproietta i layer vettoriali presenti in un progetto QGIS aperto, li riporietta in un SR di riferimento definito (outputCRSSstr) e salva gli ouput in una cartella
# che sia chiama Reprojectd e che sta sta nella stessa directory del progetto. L'output è poi ri-caricato
# nel progetto QGIS, con il prefisso "reproj". 
# Dovrebbe essere self-explanatory



canvas = qgis.utils.iface.mapCanvas()
allLayers = canvas.layers()

# Pah of the current directory in wihich you are qworking
pathToProject=os.getcwd()

#  Create  directory, 'Reprojected', to store the output
if not os.path.exists('Reprojected'):
    os.makedirs('Reprojected')

# Declare output CRS
outputCRSSstr = 'EPSG:3003'
outputCRS = QgsCoordinateReferenceSystem(outputCRSStr)

for i in allLayers: 
    if i.type() != 0 :
        
        # Print check
        print(i.name() + " skipped as it is not a vector layer")
    
    if ( (i.type() == 0) and i.crs() != outputCRS ):
        
        # Print check
        print (i.name())
        
        outputLayerPathReproj = os.path.join(pathToProject, "Reprojected", i.name()+".shp")
        
        # if you want ot store the result in temporary layer
        #parameter = {'INPUT': i, 'TARGET_CRS': 'EPSG:3003', 'OUTPUT': 'memory:Reprojected'}
        #QgsProject.instance().addMapLayer(result['OUTPUT'])
        
        # Store the result in a shp file in the same folder of the .qgs/.qgz project I'm working on 
        # The output crs is epsg 3003, in this case
        parameter = {'INPUT': i, 'TARGET_CRS': outputCRSStr, 'OUTPUT': '{}'.format(outputLayerPathReproj)}
        result = processing.run('native:reprojectlayer', parameter)
        
        # Add the result to the .qgs/.qgz project
        vlayer = QgsVectorLayer(outputLayerPathReproj, "reproj"+ i.name(), "ogr")
        QgsProject.instance().addMapLayer(vlayer)
