from array import *

#1.Create an array and traverse
print("Step 1")
arr1=array('i',[1,2,3,4,5])
for num in arr1:
    print(num)
    
# 2. Access individual elements through index
print("Step 2")
print(arr1[2])

#3. Append any value to the array using the append method
print("Step 3")
arr1.append(6)
print(arr1)

#4. Insert value in an array using the insert method
print("Step 4")
arr1.insert(3,12)
print(arr1)

# 5. Extend python array using the extend method
print("Step 5")
arr2=array('i',[7,8,9,10])
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist method
print("Step 6")
list1=[44,45,46]
arr1.fromlist(list1)
print(arr1)

# 7. Remopve any array element using remove method
print("Step 7")
arr1.remove(12)
print(arr1)

# 8. Remove last element using pop method
print("Step 8")
arr1.pop()
print(arr1)

# 9. Fetch the index of any element using the index method
print("Step 9")
print(arr1.index(7))

# 10. Reverse the array using reverse method
print("Step 10")
arr1.reverse()
print(arr1)
