import re
import random


class TextProcessor:
    def __init__(self):
        self.data = None
        self.result = None

    def input_data(self):
        self.data = input("Введите текст: ")
        self.reset_result()

    def generate_data(self):
        words = ["example", "text", "generation", "random", "words", "vowels", "consonants"]
        self.data = " ".join(random.choices(words, k=random.randint(5, 15)))
        print(f"Сгенерированные данные: {self.data}")
        self.reset_result()

    def process_data(self):
        if not self.data:
            print("no input data")
            return
        words = re.findall(r'\b\w+\b', self.data)
        vowels = "aeiouyAEIOUY"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

        total_vowels = sum(1 for char in self.data if char in vowels)
        self.result = [
            (word, sum(1 for char in word if char in vowels), sum(1 for char in word if char in consonants), total_vowels)
            for word in words
        ]
        print("algorithm completed")

    def reset_result(self):
        self.result = None

    def get_result(self):
        if not self.result:
            print("algorithm failed")
            return None
        return self.result


class Menu:
    def __init__(self):
        self.processor = TextProcessor()

    def display_menu(self):
        print("\nМеню:")
        print("1. Ввод данных вручную")
        print("2. Генерация случайных данных")
        print("3. Выполнение алгоритма")
        print("4. Вывод результата")
        print("5. Завершение работы")

    def handle_choice(self, choice):
        if choice == '1':
            self.processor.input_data()
        elif choice == '2':
            self.processor.generate_data()
        elif choice == '3':
            self.processor.process_data()
        elif choice == '4':
            result = self.processor.get_result()
            if result:
                print("\nРезультат обработки текста:")
                for word, vowels, consonants, total_vowels in result:
                    print(f"Слово: {word}, Гласные: {vowels}, Согласные: {consonants}, Всего гласных в тексте: {total_vowels}")
        elif choice == '5':
            print("Программа завершена.")
            return False
        else:
            print("Неверный выбор. Повторите ввод.")
        return True

    def run(self):
        while True:
            self.display_menu()
            choice = input("Выберите пункт меню: ")
            if not self.handle_choice(choice):
                break

