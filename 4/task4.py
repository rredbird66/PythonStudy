print("--------Task4--------")
def wordcount(filename):
    fd = open(filename, "r")
    word_list = fd.read().split()  
    word_dict = {word:word_list.count(word) for word in word_list}
    for i in word_dict:
        print(i, ':', word_dict[i], sep = '')
wordcount("data.txt")
