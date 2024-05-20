number = 5

x = open("my_file.txt", "w")
x.write(f"This is a file handling assignment\nThere were {number} guests at the party\nI know how to handle files")
x.close()

x = open("my_file.txt", "r")
print(x.read())
x.close()

x = open("my_file.txt", "a")
x.write("I am appending three more lines to this file\nPractice more by building projects using Python\nPrompt chat GPT to give you projects")
x.close()

try:
    f = open('my_file.txt')
except FileNotFoundError:
    print("Sorry. There is no such file!")
except PermissionError as e:
    print(e)
finally:
    f.close()