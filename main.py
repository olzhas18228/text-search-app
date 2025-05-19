def search_word_in_file(file_path, word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            found = False
            for i, line in enumerate(lines):
                if word.lower() in line.lower():
                    print(f"Найдено на строке {i+1}: {line.strip()}")
                    found = True
            if not found:
                print("Слово не найдено.")
    except FileNotFoundError:
        print("Файл не найден.")

# Пример использования
file_name = "example.txt"
word_to_search = input("Введите слово для поиска: ")
search_word_in_file(file_name, word_to_search)
