layers = []
layers_name = []
subgr_name = []
layers_id = []
layers_dict = {}
root = QgsProject.instance().layerTreeRoot()
for child in root.children():
    if isinstance(child, QgsLayerTreeGroup):
        grs = child.findGroups()
        for gr in grs:
            #print(gr.name())
            subgr_name.append(gr.name())
            lyrs = gr.findLayers()
#            print(lyrs)
            for lyr in lyrs:
#                print(lyr.name())
#                print(lyr.layerId())
                layers.append(lyr.layer())
                layers_name.append(lyr.name())
                layers_dict[layers[-1]] = (layers_name[-1], subgr_name[-1])
new_dict = {}
for key, value in layers_dict.items():
    layers_id.append(key.id())
    layers_dict[key] = (value[0], value[1], layers_id[-1])
    print(layers_dict[key][0])
    print(layers_dict[key][1])
    print(layers_dict[key][2])
    new_dict[layers_id[-1]] = (layers_dict[key][0], layers_dict[key][1])
#for key, value in layers_dict.items():
#    print(key)
#    print(value[1])
#    #print(value[1])
    
#print(layers_id)
print(layers_dict)
print(new_dict)
