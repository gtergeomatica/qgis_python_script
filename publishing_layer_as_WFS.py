#### vedi https://gis.stackexchange.com/questions/362890/publishing-a-layer-as-wfs-with-pyqgis


vectorLayers = {layer.id(): layer.name() for layer in QgsProject.instance().mapLayers().values() if isinstance(layer, QgsVectorLayer)}
#print(vectorLayers)
wfsLayersConfig = [
  {
    "name": "condotte",
    "published": True,
    "precision": 8,
    "Update": False,
    "Insert": False,
    "Delete": False
   }
]

# To join by name as a key instead of identifier
# Weak but to be generic, more simple to use layer name
# whereas layers identifiers hidden
vectorLayersKeyValReversed = {v: k for k, v in vectorLayers.items()}
print(vectorLayersKeyValReversed)
# To set if published
QgsProject.instance().writeEntry( "WFSLayers" , "/", [vectorLayersKeyValReversed[l['name']] for l in wfsLayersConfig if l["published"] == True]);

QgsProject.instance().write()