l = input("Enter the elements in list :")
l1 =list(l)
print(l1)
def insertion_sort(l):
    """Sorts a sequence (list) using the insertion sort algorithm."""

    for slice_end in range(len(l)): # sliceEnd is the index of the element to insert
        pos = slice_end  # pos is where we'll try to insert seq[sliceEnd]

        # Move elements greater than seq[pos] to the right
        while pos > 0 and l[pos] < l[pos - 1]:
            # Swap seq[pos] and seq[pos-1]
              l[pos],l[pos - 1] =   l[pos - 1],   l[pos]  # Efficient swap in Python
              pos -= 1  # Move one position to the left

inserted = insertion_sort(l)
print(inserted)