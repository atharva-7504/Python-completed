def merge_sort(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i+j <m+n:
        if i == m:
            C.append(B[j])
        elif j == n:
            C.append(A[i])
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i +1
        elif A[i] < B[j]:
            C.append(B[j])
            j = j+1
    return(C)

A = [3,2,4,56,7,9]
print(A)
B = [2,1,3,4,57,5]
print(B)
ms = merge_sort(A,B)
print("Merge Sort :",ms)

