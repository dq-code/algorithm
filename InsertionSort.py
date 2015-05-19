#!/usr/bin/python

class InsertionSort:
    def __init__(self, array):
        self.array = array
    
    def sortArray(self):
        for i in range(1, len(self.array)):
            index = i
            target = self.array[i]
            while(index > 0 and target < self.array[index - 1]):
                self.array[index] = self.array[index - 1]
                index = index -  1
            self.array[index] = target
    def toString(self):
        print ", ".join(str(x) for x in self.array)

if __name__ == "__main__":
    arr = [9,18,0,66,145,4,333,22,1]
    sort = InsertionSort(arr)
    print "before sorting"
    sort.toString()
    sort.sortArray()
    print "after soring"
    sort.toString()
