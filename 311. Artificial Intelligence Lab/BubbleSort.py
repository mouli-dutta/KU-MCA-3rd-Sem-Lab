def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubble_sort(list):
    size = len(list)
    sorted = list.copy()

    for i in range(size):
        swapped = False

        for j in range(0, size-i-1):
            if sorted[j] > sorted[j+1]:
                swap(sorted, j, j+1)
                swapped = True
        
        if not swapped:
            break
    
    return sorted

def main():
    size = int(input("Enter the size of the list: "))
    unsorted_list = []
    for i in range(size):
        element = int(input(f"Enter the element at position {i}: "))
        unsorted_list.append(element)

    sorted_list = bubble_sort(unsorted_list)
    print(f"Unsorted list = {unsorted_list}\nSorted list = {sorted_list}")

main()