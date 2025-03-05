import sys

def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

if __name__ == "__main__":
    try:
        numbers = list(map(int, sys.stdin.readline().strip().split()))
        even_count, odd_count = count_even_odd(numbers)
        print(f"Четных: {even_count}, Нечетных: {odd_count}")
    except ValueError:
        print("Ошибка: Введите список целых чисел, разделенных пробелами.")
