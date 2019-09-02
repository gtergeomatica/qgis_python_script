root = QgsProject.instance().layerTreeRoot()
#print(root.children())
#child0 = root.children()
#group_names = []
#for ch in child0:
#    #grs = ch.findGroups()
#    if isinstance(ch, QgsLayerTreeGroup):
#        print (type(ch))
#        group_names.append(ch.name())
#    else:
#        print('no')
        
sel_gr = 'Piano degli Interventi'

subgr_name = []
lyr_names = []
for c in root.children():
    #print(c)
    if isinstance(c, QgsLayerTreeGroup):
        if c.name() == sel_gr:
            for subc in c.children():
                if isinstance(c, QgsLayerTreeGroup):
                    subgr_name.append(subc.name())
                    lyrs = subc.findLayers()
            #            print(lyrs)
                for lyr in lyrs:
#                    print(lyr.name())
#                    print(lyr.layerId())
                    lyr_names.append(lyr.name())
        
print(group_names)
print(subgr_name)
print(lyr_names)
