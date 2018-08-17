'''
    Document Distance - A detailed description is given in the PDF
'''
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1.lower()
    dict2.lower()
    a_dict = {}
    word_freq = {}
    list_1 = dict1.split(" ")
    list_2 = dict2.split(" ")
    list_3 = list_1 + list_2
    spl_char = "!@#$%^&*()-_+"
    for i in list_3:
        if i in spl_char:
            list_3.remove(i)
    for i in list_3:
        a_dict[i] = list_3.count(i)
    dict_3 = load_stopwords("stopwords.txt")
    for i in dict_3:
        if i in a_dict:
            del a_dict[i]
    for i in list_3:
        word_freq[i] = [list_1.count(i), list_2.count(i)]
    numer_n = sum([v[0]*v[1] for v in word_freq.values()])
    denom_1 = math.sqrt(sum([v[0]**2 for v in word_freq.values()]))
    denom_2 = math.sqrt(sum([v[1]**2 for v in word_freq.values()]))
    return numer_n/denom_1*denom_2
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
