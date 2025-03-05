import sys

def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

if __name__ == "__main__":
    try:
        numbers = list(map(int, sys.stdin.readline().strip().split()))
        min_value, max_value = find_min_max(numbers)
        if min_value is not None and max_value is not None:
            print(f"Минимум: {min_value}, Максимум: {max_value}")
        else:
            print("Ошибка: список пуст")
    except ValueError:
        print("Ошибка: Введите список целых чисел, разделенных пробелами.")
