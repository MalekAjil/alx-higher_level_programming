#!/usr/bin/python3
"""Unittest for Base Class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase, Base):
    """test methods of Base"""
    def test_common(self):
        self.assertEqual(self.common(), "This is a common method of Base")

    def test_specific(self):
        self.assertEqual(self.specific(), "This is a specific method of Base")


if __name__ == '__main__':
    unittest.main()
