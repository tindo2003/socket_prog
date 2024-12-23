# swapping the smallest element in the unsorted part to the current index
def selection_sort(arr):
    N = len(arr)
    for idx in range(N):
        min_idx = idx
        for j in range(idx + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx == idx: continue 
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

# shift all elements greater than cur in the sorted portion of arr 
def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur
    
def main():
    arr = [7, 6, 5, 4]
    #selection_sort(arr)
    insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
