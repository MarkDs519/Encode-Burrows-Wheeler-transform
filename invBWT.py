# Written by Mark Dhruba Sidker
# ID - 26529548


def rankBwt(bw):
    '''
     Given BWT string bw, returns a parallel list of B-ranks. 
     Time Complexity: O(N)
    :param bw: the bwt
    :return: ranks of the elements in bwt
    '''
    table = dict()      # creating an empty table
    ranks = []
    for item in bw:
        if item not in table:
            table[item] = 0       # set all ranks initially as 0
        ranks.append(table[item])   # inserting all the ranks inside the table
        table[item] += 1             # ranking all the items
    return ranks, table

def firstCol(table):
    '''
    Returns the first column by sorting the bwt.
    Time Complexity: O(NlogN)
    :param table: the table of characters and rank
    :return: the first column elements
    '''
    first_col = {}                        # creating an empty table for the first column
    var = 0
    List = []                             # empty list
    for item in table:
        List.append((item, table[item]))
    sort = mergeSort(List)                # calling the sorting algo
    for i in range(len(sort)):
        first_col[sort[i][0]] = (var, var + sort[i][1])  # updating the rank of the items in the first column
        var += sort[i][1]
    print(first_col)
    return first_col

def reverseBwt(bw):
    '''
    creating the original string from the BWT.
    Time Complexity: O(NlogN)
    :param bw: 
    :return: 
    '''
    ranks, table = rankBwt(bw)     # calling the ranks function
    first = firstCol(table)        # calling the first column function
    rowi = 0
    t = "$"
    while bw[rowi] != '$':
        c = bw[rowi]
        print(c)
        t = c + t
        print(t)
        rowi = first[c][0] + ranks[rowi]
    return t

def mergeSort(alist):
    '''
    Sorting the elements inside the list by incrementing the i by 1.
     Time Complexity: O(NlogN)
    :param alist: list to be sorted
    :return: the sorted list
    '''
    if len(alist) > 1:
        mid = len(alist)//2                    # finding the middle value
        lefthalf = alist[:mid]                 # the lefthalf of the array
        righthalf = alist[mid:]                # the righthalf of the array

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
            i = i+1
            k = k+1
        # sorting the right half
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    return alist

if __name__ == "__main__":
    file = open('cipher.txt', 'r')    # opening file
    String = ''
    for line in file.read().strip('\n'):
        String += line                    # inserting the text in file inside a string
    #writing to file
    #reverse_bwt = reverseBwt(String)
    print(reverseBwt(String))
    '''newfile = open('originalstring.txt', 'w')
    newfile.write(reverse_bwt)
    newfile.close()'''
