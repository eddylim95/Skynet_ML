import cv2
import numpy as np

folders = [ 
    'BabyBibs',
    'BabyHat',
    'BabyPants',
    'BabyShirt',
    'PackageFart',
    'womanshirtsleeve',
    'womencasualshoes',
    'womenchiffontop',
    'womendollshoes',
    'womenknittedtop',
    'womenlazyshoes',
    'womenlongsleevetop',
    'womenpeashoes',
    'womenplussizedtop',
    'womenpointedflatshoes',
    'womensleevelesstop',
    'womenstripedtop',
    'wrapsnslings'
]

for name in folders:
	i = 1
	while (True):
		try:
			filename = "\\" + name + "\\" + name + "_" + str(i)
			image = cv2.imread(filename, 0)
			resized_image = cv2.resize(image, (150, 150)) 
			cv2.imwrite(filename + "_Grey", resized_image)
			i += 1
		except:
			print(name + ' error')
			break;