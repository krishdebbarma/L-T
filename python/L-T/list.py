# Creating Empty List
li = []
li2 = list() # List Constructor
print(li)
print(type(li2))

# Values in the list
li3 = [1,22.3,"Hello",True,False,None]
print(li3)
# Taking Dynamic Input
# li4 = list(map(int,input().split()))
# print(li4)

# Indexing 
# List have both positive and Negative indexing\
# li = [12,17,21,32,11,10]
# idx= [0, 1, 2, 3, 4, 5] - Positive Indexing -> 0 to n-1 -> n = length 
# idx= [-6,-5,-4,-3,-2,-1] - Negative Indexing -> -n to -1 
li = [18,"Hello",98,23,12,"Nabanitha","Suborijeet"]
print(li[2])
print(li[-1])
# print(li[22]) Index Out Of Range
print(len(li))
print(li[6])
print(li[len(li)-2])

# Slicing
# Extracting the Subarray - [1,2,3,4] -> [1],[2,3],[1,2,3], X[3,2],X[1,2,4]
# Slicing - list[start:end:step] - takes index positions
li = [1,2,3,4,5,6,7,8]
print(li[:4]) # li[end] = start = 0
print(li[2:6]) # li[start:end]
print(li[1:6:2]) # li[start:end:step]
print(li[::])
print("Reverse",li[::-1]) # Reverse
# 2D Lists 
matrix = [[1,2,3],[4,5,6]]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[0][1])
print(matrix[1][1])

# List Methods and Mutability
li = [22,33,12,43,54]
print(li)
# Adding Values
li.append(500)
print(li)
li.insert(2,900)
print(li)
li.insert(22,1000) # Invalid index so element is added at end
print(li)
# Deleting Values
print(li)
li.pop() # if no index is given last element will be removed
print(li)
li.pop(2) # if index specified that element is removed
print(li)
li.remove(500) # deletes element if element not found raises error
print(li)
# li.remove(500)
# print(li)

# More Methods
li.sort()
print(li)
print("length",len(li))
li2 = [1,2,2,3]
# li.append(li2)
# print(li)
li.extend(li2)
print(li)
print("Count of 2's",li.count(2))
print("Index of 22",li.index(22))
li.clear()
print(li)
del li
# print(li)

# Iteration or Trversing -> accessing each element in the list
li = [1,5,2,7,9]
print("Using For.. range")
for i in range(len(li)): # 0 - 5
    print(li[i])
print("Using for Each loop")
for i in li:
    print(i)

# Concatenation -> joining 2 lists
li1 = [5,6,7]
li2 = [10,11,12]
li3 = li1+li2
print(li3)
# repetetion
li = [1,2,3]
li2 = li*3
print(li2)
# Membership Operators
li = [22,19,11,5,2] #43
print(22 in li)
print(22 not in li)
print(15 not in li )
print(15 in li)

# Deepcopy and Shallowcopi
orig_li = [1,2,3,4]
shallow_copy = orig_li
print(orig_li)
print(shallow_copy)
shallow_copy[0] = 1000
print(shallow_copy)
print(orig_li)

# Deep COpy -> Creates a new Object copy
orig_li = [1,2,3,4,5]
deep_copy = orig_li.copy()
deep_copy2 = orig_li[::]
print(orig_li)
print(deep_copy)
deep_copy[0] = 1000
print(deep_copy)
print(orig_li)