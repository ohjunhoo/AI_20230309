def bucket_sort(arr):
    buckets =[[] for _ in range(len(arr))]

    for value in arr:
        bucket_index = value * len(arr) //(max(arr)+1)
        buckets[bucket_index].append(value)
    sorted_list =[]
    for bucket in buckets:
        sorted_list.extend((quick_sort(bucket)))
    return sorted_list
# def quick_sort(arr):
#     arr_length = len(arr)
#     if arr_length <= 1:
#         return arr
    
#     pivot = len(arr) // 2
#     front_arr , pivot_arr , back_arr =[], [], []
#     for value in arr:
#         if value < arr[pivot]:
#             front_arr.append(value)
#         elif value > arr[pivot]:
#             back_arr.append(value)
#         else:
#             pivot_arr.append(value)
#         return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if ARRAY_LENGTH <= 1:
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

if __name__ == '__main__':
    unsorted = [4, 2, 7, 3, 2, 6, 8, 9, 2, 3, 1]
    sorted = bucket_sort(unsorted)

    print(sorted)