class QuickSort:

    def __init__(self):
        data_in = str(input("Enter in integers separated by spaces to sort: "))
        data_split = data_in.split()
        data = map(int, data_split)
        self.list_data = list(data)
        self.length = len(self.list_data)

    def switch(self, index1, index2):
        data1 = self.list_data[index1]
        self.list_data[index1] = self.list_data[index2]
        self.list_data[index2] = data1

    def sort(self, low, high):
        length = high - low + 1
        pivot = self.list_data[high]
        i = low
        j = low

        if length == 1:
            return self.list_data

        else:
            while j != high:
                if self.list_data[j] <= pivot:
                    if i == j:
                        i += 1
                        j += 1
                    else:
                        self.switch(i, j)
                        i += 1
                        j += 1

                else:
                    j += 1

        self.switch(i, j)

        if i > low:
            self.sort(low, i - 1)

        if i < high:
            self.sort(i + 1, high)

        return self.list_data

def main():
    quick_sort = QuickSort()
    print(quick_sort.sort(0, (quick_sort.length - 1)))


if __name__ == "__main__":
    main()
