import os
file_path= input("type in file path: ")
with open(file_path,'r') as file:
    print(file.read())
    file.close()