class SortedArray:
    def __init__(self):
        self.n = 0
        self.a = []

    def getArray(self):
        self.n = int(input("Enter the size of the array: "))
        self.a = sorted(map(int, input("Enter space-separated elements of the array: ").split()))
        print("Sorted Array:", " ".join(map(str, self.a)))

arr = SortedArray()
arr.getArray()
