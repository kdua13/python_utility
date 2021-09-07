# python program to distinct word count

import sys
args1 = str(sys.argv[1])

def word_count(file_path):
    import os 
    file_path = os.path.abspath(os.path.realpath(file_path))
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
    
    #print(word_list)
    word_dict = {}
    for word_uniq in word_list:
        if word_uniq not in word_dict:
            word_dict.update({word_uniq: word_list.count(word_uniq)})
    #print(word_dict)
    file.close()
    return word_dict


def word_count_perm(file_path):
    import os
    file_path = os.path.abspath(os.path.realpath(file_path))
    file = open(file_path, "r")
    ftext = file.read()
    lines = ftext.split("\n")
    
    words_list = []
    sorted_list = []
    for line in lines:
        words = line.split(" ")
        for word in words:
            words_list.append(sorted(word.strip().lower()))
        
    #print(words_list)
    for word_list in words_list:
        sorted_word = ""
        for char in word_list:
            sorted_word += char
        sorted_list.append(sorted_word)
    
    #print(sorted_list)
    word_dict = {}
    for word_u in sorted_list:
        if word_u not in word_dict:
            word_dict.update({word_u: sorted_list.count(word_u)})
     
    file.close()
    return word_dict
