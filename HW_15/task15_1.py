import logging
import argparse


logging.basicConfig(filename='log_1.log', filemode='w', encoding='utf-8',
                    format='{levelname:<6}  {asctime} в строке {lineno:>3d} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        logger.info("d>0")
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        logger.info("один корень")
        return -b / (2 * a)
    else:
        logger.info(f"нет вещественных корней{d= }<0")
        return "нет вещественных корней"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))
