#Capital indexes
def capital_indexes(input):
    upper_char_list = []
    char_list = list(input)
    for i in range(len(char_list)):
        if (char_list[i].isupper()):
            upper_char_list.append(i)
    return upper_char_list

#Middle letter
def mid (input):
    if len(input) % 2 != 0:
        return input[int((len(input)-1)/2)]
    else:
        return ""

#Online status
def online_count(input):
    online_count = 0
    for i in input:
        if input[i] == "online":
            online_count += 1
    return online_count

#Randomness
def random_number():
    import random
    return (random.randrange(1, 101))

#Type check
def only_ints(inp1, inp2):
    try:
        if int(inp1) is inp1 and int(inp2) is inp2:
            return True
    except ValueError:
        return False
    
def only_ints1(inp1, inp2):
    return isinstance(inp1, int) and isinstance(inp2, int)
#print(only_ints1(1, True))

#Double letters
def double_letters(input):
    char_t = ""
    char_pairs = []
    for i in range(len(input)):
        char = input[i]
        if char_t is char:
            print(char)
            char_pairs.append(char_t + char)
        char_t = char
    print(char_pairs)
    return True

#Double letters
def double_letters(input):
    char_t = ""
    retutn_bool = False
    for i in range(len(input)):
        char = input[i]
        if char_t is char:
            retutn_bool = True
        char_t = char
    return retutn_bool

#Adding and removing dots
def add_dots(string):
    #return ".".join(s)
    out = ""
    for char in string:
        out += char + "."
    return out[:-1]

def remove_dots(string):
    return string.replace(".", "")

#Counting syllables
def count(string):
    return string.count("-")+1

#Anagrams
def is_anagram(string1, string2):
    string1_list = list(string1)
    string1_list.sort()
    string2_list = list(string2)
    string2_list.sort()
    if string1_list == string2_list:
        return True
    return False

#Flatten a list
def flatten(list_of_list):
    flatten_list = []
    for inner_list in list_of_list:
        for item in inner_list:
            flatten_list.append(item)
    return flatten_list

#Min-maxing
def largest_difference(list):
    max = -100
    for item in list:
        if item > max:
            max = item
    print(max)
    min = 100
    for item in list:
        if item < min:
            min = item
    print(min)
    return max - min

def get_row_col(str):
    str_list = list(str)
    row_dict = {"A" : 0, "B" : 1, "C" : 2}  
    col = row_dict.get(str_list[0])
    row = int(str_list[1]) - 1
    return (row, col)

#Palindrome
def palindrome(string):
    return string == string[::-1]

#Up and down
def up_down(num):
    return (num-1, num+1)

#Consecutive zeros
def consecutive_zeros(num):
    counter = 0
    max_zeros = 0
    for i in list(str(num)):
        if int(i) == 0:
            counter += 1
            if max_zeros < counter:
                max_zeros = counter
        else:
            counter = 0
        print(str(i) + "," + str(counter) + "," + str(max_zeros))
    return max_zeros
        
#print(consecutive_zeros(10011010001100000))

#All equal
def all_equal(inp_list):
    result = True
    if len(inp_list) > 0 and max(inp_list) != min(inp_list):
        result = False
    return result

def convert(list_num):
    return list([str(i) for i in list_num])

#Custom zip
def zap(a,b):
    output = []
    for i in range(len(a)):
        output.append((a[i],b[i]))
    return output

#Solution validation
def validate(str):
    if "def" not in str:
        return "missing def"
    elif ":" not in str:
        return "missing :"
    elif "(" not in str or ")" not in str:
        return "missing paren"
    elif ("(" + ")") in str:
        return "missing param"
    elif "    " not in str:
        return "missing indent"
    elif "validate" not in str:
        return "wrong name"
    elif "return" not in str:
        return "missing return"
    else:
        return True

#print(validate("def validate(_):    return"))

#List xor
def list_xor(n, list1, list2):
    return bool(not((n in list1 and n in list2) or (n not in list1 and n not in list2)))

#Counting parameters
def param_count(*params):
    return len(params)

#Thousands separator
def format_number(num):
    out = list(str(num))
    if(len(out)%3 > 0):
        commas = range(int(len(out)/3))
    else:
        commas = range(int(len(out)/3)-1)
    for i in commas:
        pos = -3*(i+1)-i
        out.insert(pos, ",")
    out_str = ""
    for char in out:
        out_str += char
    return out_str

def format_number1(n):
    return "{:,}".format(n)

def format_number2(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

#print(format_number(1000000000000))


