#!/usr/bin/env python3
import optparse
from .steganography import encode, decode

def run():
    parser = optparse.OptionParser('usage : %python3 <prog> -e/-d <target file>')
    parser.add_option('-e', dest='encode', type='string', help='Path of the image you want to encode')
    parser.add_option('-d', dest='decode', type='string', help='Path of the image you want to decode')

    (options, args) = parser.parse_args()

    if options.encode != None:
        message = input('Enter a message to hide in image: ')
        print(encode(message, options.encode))
    elif options.decode != None:
        print(decode(options.decode))
    else:
        print(parser.usage)
        exit(0)
