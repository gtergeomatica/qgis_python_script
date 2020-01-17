import os
from xml.etree import ElementTree as et

file_1 = ''
file_2 = []
proj_path = QgsProject.instance().absolutePath()
proj_name = QgsProject.instance().baseName()

#search the .ts file generated from project properties and all .ts file already transleted with QtLinguist (named project_name_*.ts) in the project folder
for ts in os.listdir(proj_path):
    path_ts = os.path.join(proj_path, ts)
    if os.path.isfile(path_ts) and len(ts.split('.')) > 1:
        #print(ts.split('.'))
        if ts == '{}.ts'.format(proj_name.split('.')[0]):
            file_1 = os.path.join(proj_path, ts)
        elif ts.split('.')[1] == 'ts' and ts.split('.')[0].startswith('{}_'.format(proj_name)):
            file_2.append(os.path.join(proj_path, ts))
            #print(ts)

#print(file_1)
#print(file_2[0])
tree_1 = et.parse(file_1)
root_1 = tree_1.getroot()

#Add all tag <name> and all tag <source> values of the .ts file generated from project properties
names1 = []
sources1 = []
for n1 in root_1.findall('context'):
    name1 = n1.find('name').text
    mes1 = n1.find('message')
    #print(name1.text)
    source1 = mes1.find('source')
    names1.append(name1)
    sources1.append(source1.text)
    
#print(len(names1))
#print(len(sources1))

#Iterate over all .ts file already transleted with QtLinguist (named project_name_*.ts)
for fts in file_2:
    print(fts)
    tree_2 = et.parse(fts)
    root_2 = tree_2.getroot()
    #Add all tag <name> and all tag <source> values of the already translated .ts file
    names2 = []
    sources2 = []
    for n2 in root_2.findall('context'):
        name2 = n2.find('name').text
        mes2 = n2.findall('message')
        #print(name2.text)
        for s2 in mes2:
            source2 = s2.find('source')
            names2.append(name2)
            sources2.append(source2.text)
            
    print(len(names2))
    print(len(sources2))
    n_no_found = []
    s_no_found = []
    #Find all tag <name> values which are in the project .ts file and not in the translated one
    for k, i in enumerate(names1):
        if i not in names2 or sources1[k] not in sources2:
            n_no_found.append(i)
    #Find all tag <source> values which are in the project .ts file and not in the translated one
    for k, i in enumerate(sources1):
        if i not in sources2 or names1[k] not in names2:
            s_no_found.append(i)
            
    print(n_no_found)
    print(s_no_found)
    
    #Add all the <context> blocks with <name> and <source> previously identified to the already translated file
    for j, i in enumerate(root_1.findall('context')):
        name = i.find('name')
        mes = i.find('message')
        source = mes.find('source')
        for k, s in enumerate(s_no_found):
            if source.text == s and n_no_found[k] == name.text:
                #print(et.tostring(i))
                new = root_2.insert(j, i)
                
    tree_2.write(fts)