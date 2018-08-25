'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    list_dict = [ele for ele in dictionary.keys()]
    list_dict.sort()
    for ele in list_dict:
        if dictionary[ele] is 1:
            print(ele, "-", "#")
        elif dictionary[ele] is 2:
            print(ele, "-", "##")
        elif dictionary[ele] is 3:
            print(ele, "-", "###")
        elif dictionary[ele] is 4:
            print(ele, "-", "####")
        elif dictionary[ele] is 5:
            print(ele, "-", "#####")
        elif dictionary[ele] is 7:
            print(ele, "-", "#######")
        elif dictionary[ele] is 8:
            print(ele, "-", "########")
        elif dictionary[ele] is 11:
            print(ele, "-", "###########")

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
