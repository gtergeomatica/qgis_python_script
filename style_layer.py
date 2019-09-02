from random import randrange
lyr = iface.activeLayer()
field_index = lyr.dataProvider().fieldNameIndex('P_CAMPAGNA')
unique_values = lyr.uniqueValues(field_index)
print(unique_values)
categories = []
for unique_value in unique_values:
    # initialize the default symbol for this geometry type
    symbol = QgsSymbol.defaultSymbol(lyr.geometryType())

    # configure a symbol layer
    layer_style = {}
    layer_style['color'] = '%d, %d, %d' % (randrange(0, 256), randrange(0, 256), randrange(0, 256))
    layer_style['outline'] = '#000000'
    #layer_style['opacity'] = '0.5'
    symbol_layer = QgsSimpleFillSymbolLayer.create(layer_style)

    # replace default symbol layer with the configured one
    if symbol_layer is not None:
        symbol.changeSymbolLayer(0, symbol_layer)

    # create renderer object
    category = QgsRendererCategory(unique_value, symbol, str(unique_value))
    # entry for the list of category items
    categories.append(category)

# create renderer object
renderer = QgsCategorizedSymbolRenderer('P_CAMPAGNA', categories)

# assign the created renderer to the layer
if renderer is not None:
    lyr.setRenderer(renderer)

lyr.triggerRepaint()