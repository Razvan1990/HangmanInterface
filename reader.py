import os
import random


class FileReader:

    def __init__(self, path, file):
        self.path = path
        self.file = file

    def read_file(self):
        file_words = os.path.join(self.path, "words", self.file)
        with open(file=file_words, encoding="utf-8", mode="r") as words:
            hangman_words = words.readlines()
            list_words = []
            for i in range(0, len(hangman_words)):
                if i == len(hangman_words) - 1:
                    list_words.append(hangman_words[i])
                else:
                    list_words.append(hangman_words[i][:-1])
            return list_words

    def get_random_word(self, my_list):
        list_words = list()
        random_value = random.randint(0, len(my_list) - 1)
        hidden_string = ""
        for character in my_list[random_value]:
            if character != " ":
                hidden_string += "_"
            else:
                hidden_string += " "
        list_words.append(my_list[random_value].upper())
        list_words.append(hidden_string)
        return list_words
