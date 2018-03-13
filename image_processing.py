import cv2
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
    i = 1
    while (True):
        try:
            image_path = os.path.join(my_path, (name + "\\" + name + "_" + str(i) + ".jpg"))
            if (not os.path.isfile(image_path)):
                break
            image = cv2.imread(image_path, 0)
            resized_image = cv2.resize(image, (150, 150)) 
            image_path = os.path.join(my_path, ("grey" + "\\" + name + "\\"))
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            image_path = os.path.join(image_path + name + "_" + str(i) + ".jpg")
            cv2.imwrite(image_path, resized_image)
            i += 1
        except:
            print(name, i, 'error')
            break;