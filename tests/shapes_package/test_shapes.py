from unittest import TestCase
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle
from shapes_library.shapes_package.shapes_module import RightTriangle


class CircleTests(TestCase):
    """
    Contains all unit tests for the shapes_module.Circle class
    """
    def test_circle_area_returns_correct_result_with_valid_radius(self):
#common to have long descriptive names for functions
        """
        Tests that a Circle object with a radius > 0 returns the correct area
        """
        mock_radius = 5.0
        expected_area = 78.54
        mock_circle = Circle(radius=mock_radius)
        self.assertEqual(mock_circle.area(), expected_area)
#assert equal is a built in method in unittest library, 1 of 15 built in to compare 2 things, b/c it's a test
#mock_circle.area() & expected_area --> 2 parameters being compared by the assertEqual method
#self --> function
#self is a keyword: means "this" sorta like itself?????????

    def test_circle_area_raises_value_error_with_negative_radius(self):
        """
        Tests that Circle object raises value error with negative radius
        """
        with self.assertRaises(ValueError):
            mock_circle = Circle(radius=-1.0)

class RectangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Rectangle class
    """
    def test_rectangle_area_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
        """
        mock_height, mock_width = 10., 10.
        expected_area = 100.
        mock_rectangle = Rectangle(height=mock_height, width=mock_width)
        self.assertEqual(mock_rectangle.area(), expected_area)

    def test_rectangle_area_raises_value_error_with_negative_width_or_height(self):
        """
        Tests that Rectangle object raises value error with negative width or height
        """
        with self.assertRaises(ValueError):
            mock_rectangle = Rectangle(height=-1.0, width=-1.0)


class RightTriangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.RightTriangle class
    """
    def test_right_triangle_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Right Triangle object with a height > 0, width > 0, and a hypotenuse > 0 returns the correct area
        """
        mock_height, mock_width, mock_hypotenuse = 3., 4., 5.
        expected_area = 6.
        mock_right_triangle = RightTriangle(height=mock_height, width=mock_width, hypotenuse=mock_hypotenuse)
        self.assertEqual(mock_right_triangle.area(), expected_area)
  
    def test_right_triangle_raises_error_message_with_valid_height_and_width_and_hypotenuse(self):
        """
        Tests that Right Triangle object raises value error with width, height, and hypotenuse that are consistent with the Pythagorean Theorem
        """
        mock_height, mock_width, mock_hypotenuse = 3., 4., 5.

        mock_right_triangle = RightTriangle(height=mock_height, width=mock_width, hypotenuse=mock_hypotenuse)
        self.assertIs(mock_right_triangle.pythagorean(), True, "Test value is not true")
    
    def test_right_triangle_raises_value_error_with_negative_width_or_height_or_hypotenuse(self):
        """
        Tests that Right Triangle object raises value error with negative width, height, or hypotenuse
        """
        with self.assertRaises(ValueError):
            mock_right_triangle = RightTriangle(height=-1.0, width=-1.0, hypotenuse=-1.0)

    def test_right_triangle_raises_value_error_with_valid_hypotenuse(self):
        """
        Tests that Right Triangle object raises value error with greater width or height in relation to hypotenuse
        """
        mock_height, mock_width, mock_hypotenuse = 3., 4., 5.
        mock_right_triangle = RightTriangle(height=mock_height, width=mock_width, hypotenuse=mock_hypotenuse)
        self.assertGreater(mock_right_triangle.hypotenuse, mock_right_triangle.height, "Test value is not greater than height")
        self.assertGreater(mock_right_triangle.hypotenuse, mock_right_triangle.width, "Test value is not greater than width")