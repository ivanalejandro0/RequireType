#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from requiretype import require


@require(a=str)
def a_str(a):
    pass


@require(a=int, b=float)
def int_float(a, b):
    pass


class TestArgsOnFunctions(unittest.TestCase):
    def test_str(self):
        a_str(a='asdf')

    def test_str_fails(self):
        with self.assertRaises(TypeError):
            a_str(a=42)

    def test_int_float(self):
        int_float(1, b=2.0)

    def test_int_float_fails(self):
        with self.assertRaises(TypeError):
            int_float(a=1.0, b=2)
