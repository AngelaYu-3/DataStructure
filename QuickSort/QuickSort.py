class QuickSort:
    def __init__(self):
        global list_data
        dataIn = str(input("Enter in integers separated by spaces to sort: "))
        dataSplit = dataIn.split()
        data = map(int, dataSplit)
        list_data = list(data)
        print(list_data)

    def sort(self):
        length = len(list_data)
        print(length)

def main():
   quickSort = QuickSort()
   quickSort.sort()

if __name__ == "__main__":
    main()
