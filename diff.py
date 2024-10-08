import difflib

# Два тексти для порівняння
text1 = "Електронний журнал дозволяє студентам отримувати доступ до своїх оцінок в режимі онлайн."
text2 = "Електронний журнал дає можливість викладачам оновлювати інформацію про оцінки в режимі онлайн."

# Розбиваємо тексти на слова для детальнішого порівняння
text1_words = text1.split()
text2_words = text2.split()

# Використовуємо unified_diff для виведення детальної різниці
diff = difflib.unified_diff(text1_words, text2_words, lineterm='', fromfile='Text 1', tofile='Text 2')

# Підрахунок кількості змін
total_words_text1 = len(text1_words)
total_words_text2 = len(text2_words)
added_words = 0
removed_words = 0
replaced_words = 0

# Аналіз змін
diff_list = list(diff)
for line in diff_list:
    if line.startswith('-'):
        removed_words += 1
    elif line.startswith('+'):
        added_words += 1

# Виводимо результат порівняння
print('\n'.join(diff_list))

# Аналіз замін: якщо кількість доданих і видалених слів збігається, це заміна
replaced_words = min(added_words, removed_words)

# Виведення аналізу змін
print("\nАналіз змін:")
print(f"Загальна кількість слів у тексті 1: {total_words_text1}")
print(f"Загальна кількість слів у тексті 2: {total_words_text2}")
print(f"Кількість доданих слів: {added_words}")
print(f"Кількість видалених слів: {removed_words}")
print(f"Кількість замінених слів: {replaced_words}")