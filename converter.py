import sys
import os
from os.path import join
from os.path import splitext

def main():
    count = 0

    directory = input("Enter full path of directory: ")
    current_extension = input("Enter current extension (example: .txt): ")
    new_extension = input("Enter new extension (example: .jpg): ")

    for filename in os.listdir(directory):
        if current_extension == splitext(filename)[1]:
            count = count + 1
            newfile = filename.replace(current_extension, new_extension)
            os.rename(join(directory, filename), join(directory, newfile))

    if count == 0:
        print("Error: Please check path of directory or file extension")
    else:
        print(count,"file's extension has been changed!")

main()