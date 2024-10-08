import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
print("-- ", arr)
bubble_sort(arr)
print("-- ", arr)

start_time = time.time()
end_time = time.time()

print("Tempo de execução:", end_time - start_time, "segundos")
