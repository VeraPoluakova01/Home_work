import argparse
import logging


logging.basicConfig(filemode="a", level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


file_handler = logging.FileHandler('fibonacci_app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def fibonacci(n):
    """
    Генерирует последовательность чисел Фибоначчи.

    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    parser = argparse.ArgumentParser(description="Генератор чисел Фибоначчи")
    parser.add_argument("num", type=int, help="Количество чисел Фибоначчи для генерации")
    args = parser.parse_args()

    try:
        num = args.num
        if num <= 0:
            logger.error("Число должно быть положительным.")
        else:
            result = list(fibonacci(num))
            logger.info(f"Числа Фибоначчи: {result}")
            print(result)
    except ValueError:
        logger.error("Некорректное значение числа.")


if __name__ == "__main__":
    main()
