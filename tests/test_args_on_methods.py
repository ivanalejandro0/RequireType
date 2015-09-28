#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from requiretype import require


class T():
    @require(a=str, b=int)
    def str_int(self, a, b):
        pass

    @require(a=str)
    def a_str(self, a):
        pass

    @require(a=int, b=float)
    def int_float(self, a, b):
        pass


class TestArgsOnMethods(unittest.TestCase):
    def test_str_int(self):
        t = T()
        t.str_int('Hello', 1234)

    def test_str_int_fails(self):
        t = T()
        with self.assertRaises(TypeError):
            t.str_int('Hello', 'world!')

    def test_str(self):
        t = T()
        t.a_str('asdf')

    def test_str_fails(self):
        t = T()
        with self.assertRaises(TypeError):
            t.a_str(42)

    def test_int_float(self):
        t = T()
        t.int_float(1, 2.0)

    def test_int_float_fails(self):
        t = T()
        with self.assertRaises(TypeError):
            t.int_float(1.0, 2)
