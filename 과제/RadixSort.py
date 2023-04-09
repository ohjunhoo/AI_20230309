class RadixSort:
    
    def __init__(self, arr):
        self.array = arr
    
    def radix_sort(self):
        max1 = max(self.array)
        exp = 1
        while max1 / exp > 0:
            self.count_sort(self.array, exp)
            exp *= 10
    
    def count_sort(self, arr, k):
        output_arr = [0] * len(arr)
        count_arr =[0] * 10

        for num in arr:
            idx = num // k
            count_arr[idx % 10] +=1
        
        for i in range(len(count_arr)-1):
            count_arr[i+1] += count_arr[i]
        
        for i in range(len(arr)-1, -1, -1):
            _idx =(arr[i]//k) % 10
            output_arr[count_arr[_idx]-1] = arr[i]
            count_arr[_idx] -=1
        
        for i in range(len(arr)):
            arr[i] = output_arr[i]

if __name__ == '__main__':
    numbers = [ 170, 45, 75, 90, 802, 24, 2, 66] 
    arr = RadixSort(numbers)

    print('Unsorted : ', arr.array)
    arr.radix_sort()
    print('Sorted   : ', arr.array)

