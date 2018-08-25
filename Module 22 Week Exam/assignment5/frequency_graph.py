'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''frequency graph function'''
    list_dict = [ele for ele in dictionary.keys()]
    list_dict.sort()
    for ele in list_dict:
        print("{} - {}".format(ele, "#"*list_dict[ele]))

def main():
    '''main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
