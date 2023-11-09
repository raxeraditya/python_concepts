import numpy as np
print("enter")


# a = np.array(5,6)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
arr1 = np.array([[[3,4,5]]])
print(arr1)

a = np.array([[5,6,7] , [4,6,43]])
lst = ["a", "b", "c", "d", "e"]



# index: 0   1    2    3    4
# index:-5  -4   -3   -2   -1 negative indexing 

# print(lst[-1])

# pop fuction can can remove word or number remove

remove = lst.pop(2)
print(remove)
print(lst)
# lst.append(5)
# print(lst)