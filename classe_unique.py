import os 

path1 = '../datasets/Penguins_data/labels - 3classes/valid/'
path2 = '../datasets/Penguins_data/labels/valid/'

path1 = '/Users/xle/Downloads/out 5/'
path2 = '/Users/xle/Downloads/out 5/C1/'

for filename in os.listdir(path1):
        #print(filename)

	# Using readlines()
	file1 = open(path1 + filename, 'r')
	Lines = file1.readlines()

	
  
	# writing to file
	file2 = open(path2 + filename, 'w')
	
	count = 0
	# Strips the newline character
	for line in Lines:
		count += 1
		#print(line[0].strip())

		if line[0].strip() == '1':
			print('OK', line[0].strip())
			L = line
			file2.writelines(L)
	file2.close()

		


