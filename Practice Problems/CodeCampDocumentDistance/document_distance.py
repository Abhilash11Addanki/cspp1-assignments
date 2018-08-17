'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
def word_list(string):
    '''function to find the word list'''
    regex = re.compile('[^a-z]')
    return [regex.sub("", w.strip()) for w in string.lower().split(" ")]
def remove_stopwords(word, dict_1, stop_word, index):
    '''function to remove stopwords'''
    for w_1 in word:
        if w_1 not in stop_word and len(w_1) > 0:
            if w_1 not in dict_1.keys():
                dict_1[w_1] = [0, 0]
            dict_1[w_1][index] += 1
    return dict_1
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    word_1 = word_list(dict1)
    word_2 = word_list(dict2)
    stop_word = load_stopwords("stopwords.txt")
    dict_1 = {}
    word_freq = remove_stopwords(word_1, dict_1, stop_word, 0)
    word_freq = remove_stopwords(word_2, dict_1, stop_word, 1)
    numer_n = sum([v[0]*v[1] for v in word_freq.values()])
    denom_1 = math.sqrt(sum([v[0]**2 for v in word_freq.values()]))
    denom_2 = math.sqrt(sum([v[1]**2 for v in word_freq.values()]))
    return numer_n/(denom_1*denom_2)
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
