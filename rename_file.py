import os 

path1 = '../datasets/Penguins_data/labels - 3classes/valid/'
path2 = '../datasets/Penguins_data/labels/valid/'

path1 = '/Users/xle/Downloads/out 5/'
path2 = '/Users/xle/Downloads/out 5/C1/'

path1 = '/Users/xle/Downloads/out 5/'
path2 = '/Users/xle/Downloads/out 5/C1/'

path1 = '/Users/xle/Desktop/these/yolo/datasets/Penguins_data/label-loc/valid/'
path2 = '/Users/xle/Desktop/these/yolo/datasets/Penguins_data/labels/test/'




for filename in os.listdir(path1):


    print('rename' + filename + ' ' + filename.replace(" ", "", 1) + ' ')


    os.rename(path1 + filename, path1 + filename.replace(" ", "", 1))




