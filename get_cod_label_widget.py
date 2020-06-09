import os

#the table layer name
table = QgsProject.instance().mapLayersByName('valuemap')[0]
#index of field containing code
idxC = table.fields().indexOf('cod')
#index of field containing label
idxD = table.fields().indexOf('descrizion')
#index of field containing the field name
idxF = table.fields().indexOf('fieldname')
pr = table.dataProvider()
projectInstance = QgsProject.instance()
root = projectInstance.layerTreeRoot()
lista = []
layernames = []
proj_dir = projectInstance.homePath()
#the txt file in which the name of layers with valuemap/valurelation widgets
txt_file = os.path.join(proj_dir,'layer.txt')

for child in root.findLayers():
    #check if layer is vector with geom
    if isinstance(child.layer(), QgsVectorLayer) and child.layer().geometryType() != 4:
        lyr = child.layer()
        #get the name of layer with valuemap/valurelation widgets
        for f in lyr.fields():
            if f.editorWidgetSetup().type() == 'ValueMap':
                layernames.append(lyr.name())
        #iterate over all fields of the layer
        for idx in lyr.fields().allAttributesList():
            if lyr.editorWidgetSetup(idx).type() == 'ValueMap':
                fieldname = lyr.fields().field(idx).name()
                #iterate over cod/label of valuemap/valuerelation widget
                for dicts in lyr.editorWidgetSetup(idx).config().values():
                    for d in dicts:
                        for k, v in d.items():
                            lista.append([v, k, fieldname])

#write values in the table excluding duplicated records
list_set = set(map(tuple,lista))
unique = list(map(list,list_set))
table.startEditing()
for u in unique:
    feat = QgsFeature(table.fields())
    feat.setAttribute(idxC, u[0])
    feat.setAttribute(idxD, u[1])
    feat.setAttribute(idxF, u[2])
    pr.addFeature(feat)
table.commitChanges()

#write layers names in the txt file
name_set = set(layernames)
unique_name = list(name_set)
with open(txt_file, "w") as file:
    for un in unique_name:
        file.write('\'' + un + '\'' + ',\n')
file.close()
print('FINITO')
