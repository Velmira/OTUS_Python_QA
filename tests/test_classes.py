# -*- coding: utf8 -*-
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle

import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(5, 6, 30, 22),
                          (7.4, 3.6, 26.64, 22)])
def test_rectangle(side_a, side_b, area, perimeter):
    """Создание прямоугольника - позитивная проверка"""
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} x {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    """Создание прямоугольника - негативная проверка"""
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} x {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5.5, 30.25, 22)])
def test_square(side_a, area, perimeter):
    """Создание квадрата - позитивная проверка"""
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(0, 0, 0),
                          (-5, 25, -20)])
def test_square_negative(side_a, area, perimeter):
    """Создание квадрата - негативная проверка"""
    with pytest.raises(ValueError):
        s = Square(side_a)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(10, 6, 8, 24, 24),
                          (10.5, 11.3, 12.7, 56.1, 34.5)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    """Создание треугольника - позитивная проверка"""
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a} x {side_b} x {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-10, -6, -8, 24, -24),
                          (0, 0, 0, 0, 0),
                          (100, 10, 10, 150, 120)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    """Создание треугольника - негативная проверка"""
    with pytest.raises(ValueError):
        t = Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(5, 78.5, 31.4),
                          (3.3, 34.2, 20.7)])
def test_circle(radius, area, perimeter):
    """Создание круга - позитивная проверка"""
    c = Circle(radius)
    assert c.name == f"Circle {radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(0, 0, 0),
                          (-5, 25, -20)])
def test_circle_negative(radius, area, perimeter):
    """Создание круга - негативная проверка"""
    with pytest.raises(ValueError):
        c = Circle(radius)


r = Rectangle(2, 5)
s = Square(5)
t = Triangle(10, 10, 10)
c = Circle(5)


@pytest.mark.parametrize(("figure1", "figure2", "total_area"),
                         [(r, s, 35),
                          (r, t, 53.3),
                          (r, c, 88.5),
                          (s, t, 68.3),
                          (s, c, 103.5),
                          (t, c, 121.8)])
def test_add_area(figure1, figure2, total_area):
    """"Позитивный тест на проверку метода add_area(other_figure)"""

    assert figure1.add_area(other_figure=figure2) == total_area


def test_raise_is_not_in_instance():
    """"Негативный тест на проверку метода add_area(other_figure)"""
    rectangle = Rectangle(2, 5)
    with pytest.raises(ValueError):
        assert rectangle.add_area(other_figure="Parallelepiped")
