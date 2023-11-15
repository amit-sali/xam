def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements of the array:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    print("Original array:")
    print_array(arr)

    selection_sort(arr)

    print("Sorted array:")
    print_array(arr)
