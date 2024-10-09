def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо елемент не знайдений, повертаємо "верхню межу"
    return (iterations, upper_bound)

# Приклад використання двійкового пошуку на відсортованому масиві дробових чисел
arr = [1.2, 2.3, 3.5, 4.6, 5.7, 6.8, 7.9, 8.2, 9.4, 10.5]

# Пошук числа 4.5, якого немає в масиві
result = binary_search(arr, 4.5)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Виведе: Кількість ітерацій: 4, Верхня межа: 4.6

# Пошук числа 7.9, яке є в масиві
result = binary_search(arr, 7.9)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")  # Виведе: Кількість ітерацій: 3, Верхня межа: 7.9
