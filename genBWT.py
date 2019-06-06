# Written By Mark Dhruba Sikder
# ID- 26529548

def suffixMaker(s):
    ''' 
        This function creates the suffix arrays and stores it in a list.
        Time Complexity: O(N)
        :param s: the text in the file
        :return: suffixes
    '''
    List = []                           # empty list
    for i in range(len(s)):
        astring = s[i:]                 # creating all the suffixes
        new_string = (astring, i)       # creating up the index of each of the suffixes
        List.append(new_string)         # appending the values inside a list
    return List

def suffix_Array(string):
    '''
    creating the suffix arrays by sorting the suffixes.
    Time Complexity: O(NlogN)
    :param string: suffixes
    :return: sorted suffixes
    '''
    sort = mergeSort(string)     # calling the merger function to sort the suffixes
    return sort


def mergeSort(alist):
    '''
    Sorting the elements inside the list by incrementing the i by 2**i.
     Time Complexity: O(NlogN)
    :param alist: list to be sorted.
    :return: sorted list
    '''
    if len(alist) > 1:
        mid = len(alist)//2                 # finding the middle value
        lefthalf = alist[:mid]              # left half of the array
        righthalf = alist[mid:]             # right half of the array

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        # sorting the left half
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = 2**i                      # incrementing the range by 2**i for the left half
            k = k+1
        # sorting the right half
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = 2**j                      # incrementing the range by 2**j for the right half
            k = k+1
    return alist

def bwt(t):

    '''
    This function returns the BWT from the suffix array created above.
    Time Complexity: O(N)
    :param t: The suffix array
    :return: a string which contains the bwt
    '''
    bw = []                         # empty list for bw
    for i in range(len(t)):         # for range in suffix array
        bw.append(t[i][1]-1)        # getting the last array
    string = ''
    for item in bw:
        if item != -1:
            string += aString[item]
            print(string)
        else:
            string += aString[len(aString)-1]        # appending the bwt in string
            print(string)

    return string


if __name__ == "__main__":
    aString = ''  # creating an empty string

    file = open('file.txt', 'r')  # filename = input("Enter the filename: ")
    for line in file.read().strip('\n'):
        aString += line  # inserting the word from file inside a string.
    print("The original string: " + str(aString))

    suffix_maker = suffixMaker(aString)  # suffix maker function
    print('Suffixes: ' + str(suffix_maker))
    suffix_array = suffix_Array(suffix_maker)  # suffix array function
    print('Suffix array: ' + str(suffix_array))
    print('BWT: ' + str(bwt(suffix_array)))  # bwt function

    # writing to file
    newfile = open('outputbwt.txt', 'w')
    newfile.write(bwt(suffix_array))
    newfile.close()

