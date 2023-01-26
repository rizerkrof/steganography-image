#!/usr/bin/env python3

import unittest
from steganography import steganography
from steganography.tests.tests import tests_function

MESSAGE = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
TEST_ENCODE_IMAGE_PATH = 'steganography/tests/resources/testImage.jpg'
TEST_DECODE_IMAGE_PATH = 'steganography/tests/resources/testImage_encoded.png'

class TestsSteganography(unittest.TestCase):
    def tests_encode(self):
        testing_samples = [
            ('Integration test', {"message":MESSAGE, "image_path":TEST_ENCODE_IMAGE_PATH}, 'Message succefully encoded')
        ]
        errors, msg = tests_function(steganography.encode, testing_samples)
        assert errors, msg

    def tests_decode(self):
        testing_samples = [
            ('Decode test', {"image_path":TEST_DECODE_IMAGE_PATH}, MESSAGE)
        ]
        errors, msg = tests_function(steganography.decode, testing_samples)
        assert errors, msg
