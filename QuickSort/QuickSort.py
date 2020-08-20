class QuickSort:

    def __init__(self, data):
        self.list_data = list(data)
        self.length = len(self.list_data)
        #print(self.list_data)
        #print(self.length)

    def switch(self, index1, index2):
        data1 = self.list_data[index1]
        self.list_data[index1] = self.list_data[index2]
        self.list_data[index2] = data1

    #logic wrong here!!--35 33 42 10 14 19 27 44 26 31
    def partition(self, low, pivot_index):
        i = low - 1
        pivot = self.list_data[pivot_index]
        for j in range(low, pivot_index):
            if self.list_data[j] < pivot:
                i += 1
                self.switch(i, j)
                print(self.list_data)

        i += 1
        self.switch(i, pivot_index)
        #print(self.list_data)
        return i

    def sort(self, low, high):
        mid = self.partition(low, self.length - 1)
        self.partition(low, mid - 1)
        print("LEFT")
        print(self.list_data)

        self.partition(mid + 1, high)
        print("RIGHT")
        print(self.list_data)


def main():
    data_in = str(input("Enter in integers separated by spaces to sort: "))
    data_split = data_in.split()
    data = map(int, data_split)
    quick_sort = QuickSort(data)
    quick_sort.sort(0, quick_sort.length - 1)


if __name__ == "__main__":
    main()
