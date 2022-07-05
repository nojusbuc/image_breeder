from PIL import Image
import numpy as np

img_file = './images/img1.jpg'
image = Image.open(img_file)
newsize = (500, 500)
image = image.resize(newsize)
splices = 50

repeats = 1


def shred_row():

    global image_arr

    split_array = np.vsplit(image_arr, splices)  # (250,2,500,3)

    first_half = np.concatenate(split_array[0::2], axis=0)
    second_half = np.concatenate(split_array[1::2], axis=0)

    # change axis from 0 to 1 to stack pictures horizontally
    image_arr = np.concatenate((first_half, second_half), axis=0)


def shred_col():

    global image_arr

    split_array = np.hsplit(image_arr, splices)  # (250,500,2,3)

    first_half = np.concatenate(split_array[0::2], axis=1)
    second_half = np.concatenate(split_array[1::2], axis=1)

    # change axis from 1 to 0 to stack pictures vertically
    image_arr = np.concatenate((first_half, second_half), axis=0)


for i in range(repeats):

    image_arr = np.array(image)

    shred_row()
    shred_col()

    image = Image.fromarray(image_arr)


image.show()
