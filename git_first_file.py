import os

path = os.getcwd()


def get_txt_file():
    for file in os.listdir(path):
        if file.endswith('.txt'):
            print(file)


get_txt_file()
