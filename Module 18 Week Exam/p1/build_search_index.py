'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    regex = re.compile('[^a-z]')
    word_l = [regex.sub("", w.strip()) for w in text.lower().split(" ")]
    return word_l
def remove_stopwords(word, stop_word):
    '''Remove Stopwords function'''
    lis_2 = word.copy()
    for w_1 in word:
        if w_1 in stop_word:
            lis_2.remove(w_1)
    return lis_2
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        # clean up doc and tokenize to words list
        # add or update the words of the doc to the search index
    # return search index
    stop_word = load_stopwords("stopwords.txt")
    search_index = {}
    for index, doc in enumerate(docs):
        list_1 = remove_stopwords(word_list(doc), stop_word)
        for ele in set(list_1):
            if ele in search_index:
                search_index[ele].append((index, list_1.count(ele)))
            else:
                search_index[ele] = [(index, list_1.count(ele))]
    return search_index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
