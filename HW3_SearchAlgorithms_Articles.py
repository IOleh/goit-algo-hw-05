import timeit

# 1. Завантаження тексту
def load_text(file_path):
    with open(file_path, 'r', encoding='windows-1251') as file:
        return file.read()

# Завантажуємо текст статей із поточної директорії
article1 = load_text('стаття 1.txt')
article2 = load_text('стаття 2.txt')

# 2. Алгоритми пошуку підрядків

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = skip.get

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        i += skip(text[i + m - 1], m)
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m, n = len(pattern), len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, q=101):
    d = 256  # Кількість символів у алфавіті
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1) % q
    p = 0  # Хеш паттерна
    t = 0  # Хеш тексту
    result = -1

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return result

# 3. Функція для вимірювання часу виконання пошуку
def test_search_time(search_func, text, pattern):
    # Вимірюємо час виконання функції
    start_time = timeit.default_timer()
    result = search_func(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time, result

# 4. Приклади підрядків
existing_substring_1 = "для вирішення практичних завдань"  # реальний підрядок, що є в статті 1
non_existing_substring_1 = "прискорення пошуку окремих елементів"  # Неіснуючий підрядок для статті 1

existing_substring_2 = "сховище даних має високі"  # підрядок, що є в статті 2
non_existing_substring_2 = "за вартістю або терміну"  # Неіснуючий підрядок для статті 2

# Для статті 1
print("Стаття 1 - Існуючий підрядок:")
print("Боєр-Мур:", test_search_time(boyer_moore, article1, existing_substring_1))
print("КМП:", test_search_time(kmp_search, article1, existing_substring_1))
print("Рабін-Карп:", test_search_time(rabin_karp, article1, existing_substring_1))

print("\nСтаття 1 - Неіснуючий підрядок:")
print("Боєр-Мур:", test_search_time(boyer_moore, article1, non_existing_substring_1))
print("КМП:", test_search_time(kmp_search, article1, non_existing_substring_1))
print("Рабін-Карп:", test_search_time(rabin_karp, article1, non_existing_substring_1))

# Для статті 2
print("\nСтаття 2 - Існуючий підрядок:")
print("Боєр-Мур:", test_search_time(boyer_moore, article2, existing_substring_2))
print("КМП:", test_search_time(kmp_search, article2, existing_substring_2))
print("Рабін-Карп:", test_search_time(rabin_karp, article2, existing_substring_2))

print("\nСтаття 2 - Неіснуючий підрядок:")
print("Боєр-Мур:", test_search_time(boyer_moore, article2, non_existing_substring_2))
print("КМП:", test_search_time(kmp_search, article2, non_existing_substring_2))
print("Рабін-Карп:", test_search_time(rabin_karp, article2, non_existing_substring_2))

bm_time, _ = test_search_time(boyer_moore, article2, non_existing_substring_2)
kmp_time, _ = test_search_time(kmp_search, article2, non_existing_substring_2)
rk_time, _ = test_search_time(rabin_karp, article2, non_existing_substring_2)

print(f"Стаття 2 (неіснуючий підрядок): Боєр-Мур: {bm_time}, КМП: {kmp_time}, Рабін-Карп: {rk_time}")
