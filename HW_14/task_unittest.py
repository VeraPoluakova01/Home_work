"""Решить задания, которые не успели решить на семинаре.
Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
doctest,
unittest,
pytest.
"""

import math
import unittest


class TestCaseName(unittest.TestCase):
    '''Тестирование функции  roots_quadratic'''

    def test_method(self):
        self.assertEqual(roots_quadratic(1, 2, 1), 'x1 = x2 = -1.0')
        self.assertEqual(roots_quadratic(4, 2, 1), 'Корней нет')


def roots_quadratic(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return f"x1 = {x1} \nx2 = {x2}"
    elif discr == 0:
        x = -b / (2 * a)
        return f"x1 = x2 = {x}"
    else:
        return "Корней нет"


if __name__ == '__main__':
    unittest.main(verbosity=2)
