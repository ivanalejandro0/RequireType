#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from requiretype import require


@require(a=(tuple, list))
def tuple_or_list(a):
    pass


@require(a=str, b=(int, bool))
def str_int_or_bool(a, b):
    pass


@require(name=str, age=(int, float, long))
def str_tuple(name, age):
    pass


class TestArgsOnFunctions(unittest.TestCase):
    def test_tuple_or_list(self):
        tuple_or_list((1, 2, 3))
        tuple_or_list(['a', 2, 4.5])

    def test_tuple_or_list_fails(self):
        with self.assertRaises(TypeError):
            tuple_or_list(set('a', 2, 4.5))

        with self.assertRaises(TypeError):
            tuple_or_list(2)

    def test_str_int_or_bool(self):
        str_int_or_bool('hello', 35)
        str_int_or_bool('world', False)

    def test_str_int_or_bool_fails(self):
        with self.assertRaises(TypeError):
            str_int_or_bool(25, False)

        with self.assertRaises(TypeError):
            str_int_or_bool('test', 0.2)

    def test_str_tuple(self):
        str_tuple("John Doe", 42)
        str_tuple(age=42, name="John Doe")
        str_tuple("Juan Perez", age=33.33)
        str_tuple("Some star", 128374619283741)

    def test_str_tuple_fails(self):
        with self.assertRaises(TypeError):
            str_tuple('John', 'Doe')

        with self.assertRaises(TypeError):
            str_tuple('John', age='Doe')
