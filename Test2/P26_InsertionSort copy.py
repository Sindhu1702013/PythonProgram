#Author: OMKAR PATHAK
#This program shows an example of insertion sort using Python

#  Insertion sort is good for collections that are very small
#  or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much. Each time an insertion is made,
#  all elements in a greater position are shifted.

#  Best O(n); Average O(n^2); Worst O(n^2)

def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        j = i - 1
        while j >= 0 and List[j] > currentNumber:
            List[j + 1] = List[j]
            j -= 1
        List[j + 1] = currentNumber

    return List

if __name__ == '__main__':
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print('Sorted List:',insertionSort(List))
