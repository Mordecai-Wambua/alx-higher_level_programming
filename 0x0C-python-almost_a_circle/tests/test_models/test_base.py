#!/usr/bin/python3
"""Unittest for Project
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Base(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_instances(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_ID(self):
        self.assertEqual(self.b4.id, 12)
        self.b4.id = 20
        self.assertEqual(self.b4.id, 20)

    def test_afterID(self):
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)


    def tearDoen(self):
        del self.r1
        del self.r2
        del self.r3

    def test_subclass(self):
        self.assertIsInstance(self.r1, Base)
        self.assertIsInstance(self.r2, Base)
        self.assertIsInstance(self.r3, Base)

        self.assertEqual(self.r3.id, 12)

    def test_private(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__width)

        with self.assertRaises(AttributeError):
            print(self.r3.__width)

        with self.assertRaises(AttributeError):
            print(self.r1.__height)

        with self.assertRaises(AttributeError):
            print(self.r3.__height)


        with self.assertRaises(AttributeError):
            print(self.r3.__x)

        with self.assertRaises(AttributeError):
            print(self.r3.__y)

    def test_getters(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_attributes(self):
        pass
if __name__ == "__main__":
    unittest.main()
