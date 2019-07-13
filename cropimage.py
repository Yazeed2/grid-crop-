import cv2

#editing the input to mach everything!
photo = input("drag and drop the image here")
photo = photo.lower()
photo = photo.replace('"', '')
photo = photo.replace('.tiff', '.png')
photo = photo.replace('.jpeg', '.png')
photo = photo.replace('.jpg', '.png')

# read image
img = cv2.imread(photo, cv2.IMREAD_UNCHANGED)

# get dimensions of image
dimensions = img.shape

# height, width
height = img.shape[0]
width = img.shape[1]


#check the ratio
ratio = height/width
if ratio != 1 :
    print('this is not 1:1 ratio image')
    print('sorry this is not there yet')

# then it is a 1:1 ratio
else:
    #chosing the option
    print('wich one would you like? ')

    print("""
1-
[][]
[][]
    """)
    print(""""
2- 
[][][]
[][][]
[][][]
    
    """)
    option = input(':')
    # 2 by 2
    if option == '1':

        crop_size = width/2
        crop_size = round(crop_size)
        y = 0
        x = 0
        h = crop_size
        w = crop_size

        #croping the image and saving the parts of the image in order
        part = photo.replace(".png", "1.png")
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "2.png")
        crop_img = img[y:y + h, x + w:width]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "3.png")
        crop_img = img[y + h:width, x:x + w]
        cv2.imwrite(part, crop_img)


        part = photo.replace(".png", "4.png")
        crop_img = img[y + h:width, x + w:width]
        cv2.imwrite(part, crop_img)

        print('done')

    elif option == '2':
       #3 by 3

       #take the measures
        crop_size = width / 3
        crop_size = round(crop_size)
        crop2 = crop_size * 2


        #croping the image and saving the parts of the image in order
        #layer 1
        part = photo.replace(".png", "1.png")
        crop_img = img[0:crop_size, 0:crop_size]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "2.png")
        crop_img = img[0:crop_size, crop_size:crop2]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "3.png")
        crop_img = img[0:crop_size, crop2:width]
        cv2.imwrite(part, crop_img)

        #layer 2

        part = photo.replace(".png", "4.png")
        crop_img = img[crop_size:crop2, 0:crop_size]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "5.png")
        crop_img = img[crop_size:crop2, crop_size:crop2]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "6.png")
        crop_img = img[crop_size:crop2, crop2:width]
        cv2.imwrite(part, crop_img)

        #layer 3
        part = photo.replace(".png", "7.png")
        crop_img = img[crop2:width, 0:crop_size]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "8.png")
        crop_img = img[crop2:width, crop_size:crop2]
        cv2.imwrite(part, crop_img)

        part = photo.replace(".png", "9.png")
        crop_img = img[crop2:width, crop2:width]
        cv2.imwrite(part, crop_img)

        print('done')