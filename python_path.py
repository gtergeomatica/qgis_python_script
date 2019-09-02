import os
import numpy as np
#mypath = 'Z:/2019/01_19_RegioneVeneto/tileMaker_plugin/dataset/fascia_costiera/DTM'
mypath = 'Z:/2019/01_19_RegioneVeneto/tileMaker_plugin/dataset/costa_gallura'
print(os.listdir(mypath))
split = mypath.split('/')
#print(split[-1])

file_name_dsm = []

for file in os.listdir(mypath):
    path = os.path.join(mypath, file)
    if os.path.isfile(path):
        print(path)
        name = file.split('.')
        print(name[0])
        files = [p for p in os.listdir(mypath) if p.startswith(name[0])]
        print(files)
    #    if file.startswith(name[0]):
    #        same_name.append(file)
        size = []
        for p in files:
            final_path = os.path.join(mypath, p)
            stats = os.path.getsize(final_path)
            size.append(stats)
            #print(size)
            #print(stats)
        print(size)
        #print(max(size))
        idx = np.argmax(size)
        max_file = files[idx]
        print(max_file)
        path_max_size = os.path.join(mypath, max_file)
        if file == max_file:
            file_name_dsm.append(max_file)
print(file_name_dsm)
#
#
#
#
#print(os.path.sep)
##final_path = os.path.join(os.path.normcase(mypath), '')
#print(final_path)
#
#
##print(os.path.normcase(mypath))
##print (os.listdir(mypath))
#file = os.path.join(mypath, os.listdir(mypath)[0])
##print(file)
##print(os.path.dirname(file))
##print(os.path.dirname(os.path.dirname(file)))
#test = os.path.join(mypath, '')
#print(test)
#
#a = "/".join(mypath.split('/')[:-2])
#print(a)
#
#b = os.path.dirname(mypath)
#print(b)
#
### once you're at the directory level you want, with the desired directory as the final path node:
#dirname1 = os.path.basename(mypath) 
#print(dirname1)
##dirname2 = os.path.split(dir)[1]