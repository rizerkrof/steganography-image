#!/usr/bin/env python3

import unittest
from steganography import utils
from steganography.tests.tests import tests_function

class TestUtils(unittest.TestCase):
    def tests_str2bin(self):
        testing_samples = [
            ('Simple letter test 1', {"string":"a"}, '01100001'),
            ('Simple letter test 2', {"string":"b"}, '01100010'),
            ('One word test', {"string":"hello"}, '0110100001100101011011000110110001101111')
        ]
        errors, msg = tests_function(utils.str2bin, testing_samples)
        assert errors, msg

    def tests_bin2str(self):
        testing_samples = [
            ('Simple letter test 1', {"binary":"01100001"}, 'a'),
            ('Simple letter test 2', {"binary":"01100010"}, 'b'),
            ('One word test', {"binary":"0110100001100101011011000110110001101111"}, 'hello')
        ]
        errors, msg = tests_function(utils.bin2str, testing_samples)
        assert errors, msg

    def tests_int2bin(self):
        testing_samples = [
            ('Simple digit test 1', {"integer":0}, '00000000'),
            ('Simple digit test 2', {"integer":1}, '00000001'),
            ('max octet value', {"integer":255}, '11111111'),
        ]
        errors, msg = tests_function(utils.int2bin, testing_samples)
        assert errors, msg

    def tests_bin2int(self):
        testing_samples = [
            ('Simple octet test 1', {"binary":"00000000"}, 0),
            ('Simple octet test 2', {"binary":"00000001"}, 1),
            ('max octet value test', {"binary":"11111111"}, 255),
        ]
        errors, msg = tests_function(utils.bin2int, testing_samples)
        assert errors, msg
