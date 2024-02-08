#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_result(self):
        a = max_integer([1, 2, 3, 4])
        self.assertEqual(a, 4)

    def test_empty(self):
        a = max_integer([])
        self.assertEqual(a, None)

    def test_singleval(self):
        a = max_integer([23])
        self.assertEqual(a, 23)

    def test_float(self):
        a = max_integer([23.5, 3.4, 14.1, 5.2, 23.2])
        self.assertEqual(a, 23.5)

    def test_unsorted(self):
        a = max_integer([3, 4, 1, 2])
        self.assertEqual(a, 4)

    def test_negatives(self):
        a = max_integer([-13, -45, -1, -9])
        self.assertEqual(a, -1)

    def test_mixed(self):
        a = max_integer([3, -4, 1, 2])
        self.assertEqual(a, 3)
