import cv2
import numpy as np
import os

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

my_path = os.path.abspath(os.path.dirname(__file__))

for name in folders:
	i = 2
	while (True):
		try:
			filename = os.path.join(my_path, (name + "\\" + name + "_" + str(i) + ".jpg"))
			image = cv2.imread(filename, 0)
			resized_image = cv2.resize(image, (150, 150)) 
			filename = os.path.join(my_path, ("grey" + "\\" + name + "\\"))
			if not os.path.exists(filename):
				os.makedirs(filename)
			filename = os.path.join(filename + name + "_" + str(i) + "_grey.jpg")
			cv2.imwrite(filename, resized_image)
			i += 1
		except:
			print(name + ' error')
			break;