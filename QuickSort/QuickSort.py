class QuickSort:
    global switch

    def __init__(self):
        global list_data
        dataIn = str(input("Enter in integers separated by spaces to sort: "))
        dataSplit = dataIn.split()
        data = map(int, dataSplit)
        list_data = list(data)
        print(list_data)

    def switch(self, index1, index2):
        data1 = list_data[index1]
        data2 = list_data[index2]
        list_data[index1] = data2
        list_data[index2] = data1

    def sort(self):
        length = len(list_data)
        pivot = list_data[length - 1]
        i = -1

        for j in range(length):
            if list_data[j] < pivot:
                i += 1
                switch(j, i)
            j += 1

        switch(length-1, i)


def main():
    quickSort = QuickSort()
    quickSort.sort()

if __name__ == "__main__":
    main()
