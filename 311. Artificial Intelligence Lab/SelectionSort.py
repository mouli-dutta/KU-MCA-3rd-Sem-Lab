def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def selection_sort(list):
    size = len(list)
    sorted = list.copy()

    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if sorted[j] < sorted[min_index]:
                min_index = j
        
        swap(sorted, i, min_index)
    
    return sorted

def main():
    size = int(input("Enter the size of the list: "))
    input_list = []
    for i in range(size):
        element = int(input(f"Enter the element at position {i}: "))
        input_list.append(element)

    sorted_list = selection_sort(input_list)
    print(f"Unsorted list = {input_list}\nSorted list = {sorted_list}")


main()