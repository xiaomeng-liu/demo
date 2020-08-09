import os

path = os.getcwd()


def get_txt_file():
    lst = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            print(file)
            lst.append(file)
    return lst


file = get_txt_file()
print(file)
print(len(file))


