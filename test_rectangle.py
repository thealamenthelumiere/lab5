# test_rectangle.py
import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # Тесты для площади
    def test_zero_area(self):
        """Проверка площади при нулевых значениях"""
        result = area(10, 0)
        self.assertEqual(result, 0)
        
    def test_square_area(self):
        """Проверка площади квадрата"""
        result = area(10, 10)
        self.assertEqual(result, 100)
        
    def test_normal_area(self):
        """Проверка площади обычного прямоугольника"""
        result = area(5, 7)
        self.assertEqual(result, 35)
    
    # Тесты для периметра
    def test_zero_perimeter(self):
        """Проверка периметра при нулевых значениях"""
        result = perimeter(0, 5)
        self.assertEqual(result, 10)
        
    def test_square_perimeter(self):
        """Проверка периметра квадрата"""
        result = perimeter(10, 10)
        self.assertEqual(result, 40)
        
    def test_normal_perimeter(self):
        """Проверка периметра обычного прямоугольника"""
        result = perimeter(3, 4)
        self.assertEqual(result, 14)

if __name__ == "__main__":
    unittest.main()