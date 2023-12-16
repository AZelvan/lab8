from triangle_class import Triangle, IncorrectTriangleSides
import pytest

def test_triangle_creation():
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.a == 3
    assert triangle1.b == 4
    assert triangle1.c == 5

def test_triangle_type():
    triangle2 = Triangle(5, 5, 5)
    assert triangle2.triangle_type() == "equilateral"
    triangle3 = Triangle(5, 5, 7)
    assert triangle3.triangle_type() == "isosceles"
    triangle4 = Triangle(3, 4, 5)
    assert triangle4.triangle_type() == "nonequilateral"

def test_perimeter():
    triangle5 = Triangle(3, 4, 5)
    assert triangle5.perimeter() == 12
    triangle6 = Triangle(5, 5, 7)
    assert triangle6.perimeter() == 17

def test_incorrect_triangle_creation():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(3, 4, 8)
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)