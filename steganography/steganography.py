#!/usr/bin/env python3
# import piexif
from PIL import Image
import numpy as np
from .utils import int2bin, str2bin, bin2int, bin2str

END_MARK = '[OVER]'

def preprocess_data(data):
    data_flatten = data.flatten()
    binary_data_flatten = np.array(list(map(int2bin, data_flatten)))
    return binary_data_flatten

def encode(message, image_path):
    try:
        image = Image.open(image_path)
    except Exception as error:
        return image_path+' not found'

    data = np.asarray(image)

    encoded_binary_data_flatten = preprocess_data(data)

    binary_message = str2bin(message+END_MARK)

    for index, char in enumerate(binary_message):
        encoded_binary_data_flatten[index] = encoded_binary_data_flatten[index][:-1]+char

    encoded_data_flatten = np.array(list(map(bin2int, encoded_binary_data_flatten)))

    encoded_data = encoded_data_flatten.reshape(np.shape(data))

    encoded_image = Image.fromarray(encoded_data.astype('uint8'))
    encoded_image_path = '.'.join(image_path.split('.')[:-1]) +'_encoded.png'
    encoded_image.save(encoded_image_path)

    return 'Message succefully encoded'

def decode(image_path):
    try:
        image = Image.open(image_path)
    except Exception as error:
        return image_path+' not found'

    data = np.asarray(image)
    binary_data_flatten = preprocess_data(data)

    char_binary=''
    message=''
    for index, binary in enumerate(binary_data_flatten):
        char_binary += binary[-1]
        if index%8==7:
            try:
                message+=bin2str(char_binary)
            except Exception as error:
                return 'No message found'

            if END_MARK in message: break
            char_binary=''

    return message.split(END_MARK)[0]
