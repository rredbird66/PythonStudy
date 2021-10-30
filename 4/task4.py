import sys
print("--------Task4--------")
def wordcount(filename):
    fd = open(filename, "r")
    word_list = fd.read().split()  
    word_dict = {word:word_list.count(word) for word in word_list}
    for i in word_dict:
        print(i, ':', word_dict[i], sep = '')
if len(sys.argv) < 2:
    print("No input file given\nExit(0)")
    exit(0)
wordcount(sys.argv[1])
