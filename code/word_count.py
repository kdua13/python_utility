# python program to distinct word count
import os 
file_path = os.path.abspath(os.path.realpath("input.txt"))
file = open(file_path, "r")
ftext = file.read()

lines = ftext.split("\n")

word_list = []
for line in lines:
    words = line.split(" ")
    for word_raw in words:
        word = word_raw.strip()
        word_list.append(word)
 
print("lines count: " + str(len(lines)))
print("words count: " + str(len(word_list)))

word_dict = {}
for word_uniq in word_list:
    if word_uniq not in word_dict:
        word_dict.update({word_uniq: word_list.count(word_uniq)})
print(word_dict)

file.close()