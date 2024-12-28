import heapq
import random 

class SortAlgorithm:
    def __init__(self, arr):
        self.arr = arr 
    
    def bubble_sort(self):
        for _ in range(len(self.arr)): 
            for j in range(len(self.arr) - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        return self.arr
    
    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1 
            while j >=0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key 
        return self.arr

    def selection_sort(self):
        arr_sorted = []
        for _ in range(len(self.arr)):
            min_ = min(self.arr)
            arr_sorted.append(min_)
            self.arr.remove(min_)
        return arr_sorted 
    
    def merge_sort(self, left, right):
        arr_sorted = [0] * (len(self.arr)  + 1) 
        if left >= right: 
            return 
        
        mid = (left + right) // 2 

        self.merge_sort(left, mid)
        self.merge_sort( mid + 1, right)

        i, j, cur = left, mid + 1, 0
        while i <= mid or j <= right: 
            # left pattern has no partition 
            if i > mid: 
                arr_sorted[cur] = self.arr[j]
                cur += 1 
                j += 1

            # right pattern has no partition 
            elif j > right:
                arr_sorted[cur] = self.arr[i]
                cur += 1
                i += 1
            
            # left partition < right partition 
            elif self.arr[i] < self.arr[j]:
                arr_sorted[cur] = self.arr[i]
                cur += 1 
                i += 1
            # left partition >= right partition 
            else: 
                arr_sorted[cur] = self.arr[j]
                cur += 1
                j += 1 
        for i in range(cur):
            self.arr[left + 1] = arr_sorted[i]

    def heap_sort(self):
        arr_sorted = []
        for i in range(len(self.arr)):
            heapq.heappush(arr_sorted, self.arr[i])

        return arr_sorted 
    
    def quick_sort(self, left, right):
        i, j = left, right 
        pivot = self.arr[left + random.randint(0, right-left)]

        # split arr to 2 parts 
        while (i <= j):
            while (self.arr[i] < pivot): i += 1
            while (self.arr[j] > pivot): j -= 1

            if i <= j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
                j -= 1
            
            if left < j: 
                self.quick_sort(left, j)
            if i < right: 
                self.quick_sort(i, right)

if __name__== "__main__":
    A = [34, 12, 6, 8, 45 , 17, 22, 18, 23, 18]
    sort_alg = SortAlgorithm(A)
    print(sort_alg.merge_sort(0, len(A)-1))