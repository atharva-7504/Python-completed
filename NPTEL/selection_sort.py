def selection_sort(l):
    for i in range(len(l)):
        minpos = i
        for j in range(i + 1, len(l)):  # Start from i+1
            if l[j] < l[minpos]:
                minpos = j
        l[i], l[minpos] = l[minpos], l[i]  # Swap elements
    return l  # Return sorted list

l = list(range(100,0,-2))
print("Original List:", l)

sorted_list = selection_sort(l.copy())  # Use .copy() to avoid modifying the original list
print("Sorted List:", sorted_list)