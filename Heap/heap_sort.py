# python3

from collections import namedtuple

Switch = namedtuple("Switch", ["index1", "index2"])
class HeapSort:
    switched = []

    def __init__(self, count):
        self.count = count

    def sift_down(self, arr, root, length):
        smallest = root
        l = (2 * root) + 1
        r = (2 * root) + 2

        if l < length and arr[l] < arr[smallest]:
            smallest = l
        if r < length and arr[r] < arr[smallest]:
            smallest = r

        if smallest == root:
            #print(arr)
            return arr

        arr[smallest], arr[root] = arr[root], arr[smallest]
        self.switched.append(Switch(root, smallest))
        #print(smallest, root)
        self.count += 1
        self.sift_down(arr, smallest, length)


def main():
    length = int(input())
    data = input()
    split_data = data.split(" ")
    map_arr = map(int, split_data)
    arr = list(map_arr)

    test = HeapSort(0)

    for i in reversed(range(int((length/2) + 1))):
        test.sift_down(arr,i,length)

    print(test.count)
    for i in test.switched:
        print(i.index1, i.index2 )
    #print(arr)

if __name__ == "__main__":
    main()