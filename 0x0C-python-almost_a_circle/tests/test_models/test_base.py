#!/usr/bin/python3
"""Unittest for Project
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
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
        self.assertEqual(self.b5.id, 4)

    def test_invalidargs(self):
        with self.assertRaises(TypeError):
            Base(23, 78, 2)

    def test_argtypes(self):
        self.assertEqual(2.3, Base(2.3).id)
        self.assertEqual("Mike", Base("Mike").id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual([3, 6, 7], Base([3, 6, 7]).id)
        self.assertEqual((34, 6, 87, 89), Base((34, 6, 87, 89)).id)

    def test_ID(self):
        self.assertEqual(self.b4.id, 12)
        self.b4.id = 20
        self.assertEqual(self.b4.id, 20)

    def test_afterID(self):
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, self.b3.id + 1)


class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3

    def test_subclass(self):
        self.assertIsInstance(self.r1, Base)
        self.assertIsInstance(self.r2, Base)
        self.assertIsInstance(self.r3, Base)

    def test_rectID(self):
        self.assertEqual(self.r3.id, 12)
        self.r3.id = 23
        self.assertEqual(self.r3.id, 23)

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

    def test_width(self):
        with self.assertRaises(TypeError):
            Rectangle("Now", 7)

        with self.assertRaises(TypeError):
            Rectangle((2, 54, 65), 17)

        with self.assertRaises(TypeError):
            Rectangle([4, 6, 9], 7)

        with self.assertRaises(TypeError):
            Rectangle(True, 7)

        with self.assertRaises(ValueError):
            Rectangle(0, 7)

        with self.assertRaises(ValueError):
            Rectangle(-7, 7)

    def test_height(self):
        with self.assertRaises(TypeError):
            Rectangle(12, "Yoh")

        with self.assertRaises(TypeError):
            Rectangle(17, (2, 54, 65))

        with self.assertRaises(TypeError):
            Rectangle(7, [4, 6, 9])

        with self.assertRaises(TypeError):
            Rectangle(7, True)

        with self.assertRaises(ValueError):
            Rectangle(5, 0)

        with self.assertRaises(ValueError):
            Rectangle(5, -7)

    def test_x(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 12, "Yoh")

        with self.assertRaises(TypeError):
            Rectangle(15, 78, (3, 45, 6))

        with self.assertRaises(TypeError):
            Rectangle(23, 7, [4, 6, 9])

        with self.assertRaises(TypeError):
            Rectangle(67, 7, True)

        with self.assertRaises(ValueError):
            Rectangle(9, 5, -7)

    def test_y(self):
        with self.assertRaises(TypeError):
            Rectangle(23, 6, 12, "Yoh")

        with self.assertRaises(TypeError):
            Rectangle(27, 15, 78, (3, 45, 6))

        with self.assertRaises(TypeError):
            Rectangle(90, 23, 7, [4, 6, 9])

        with self.assertRaises(TypeError):
            Rectangle(11, 67, 7, True)

        with self.assertRaises(ValueError):
            Rectangle(34, 90, 5, -7)


if __name__ == "__main__":
    unittest.main()
