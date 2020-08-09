import os

path = os.getcwd()
print(path)
for file in os.listdir(path):
    if file.endswith('.txt'):
        print(file)
