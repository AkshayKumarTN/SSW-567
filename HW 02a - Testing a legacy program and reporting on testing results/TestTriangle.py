# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
import unittest
from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    def test_right_triangle(self): 
        self.assertEqual(classify_triangle(9, 12, 15), 'Right')
        self.assertEqual(classify_triangle(8, 15, 17), 'Right')

    def test_equilateral_triangle(self): 
        self.assertEqual(classify_triangle(2, 2, 2), 'Equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(7, 7, 10), 'Isosceles')
        self.assertEqual(classify_triangle(200, 200, 100), 'Isosceles')

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(5, 6, 7), 'Scalene')

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(2, 9, 12), 'NotATriangle')
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(300, 150, 150), 'InvalidInput')
        self.assertEqual(classify_triangle(0, 2, 2), 'InvalidInput')
        self.assertEqual(classify_triangle(-3, 4, 5), 'InvalidInput')
        self.assertEqual(classify_triangle(2.5, 2, 2), 'InvalidInput')
        self.assertEqual(classify_triangle(1, 1, 1.414), 'InvalidInput')