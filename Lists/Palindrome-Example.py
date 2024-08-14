"""List are mutable in python"""

# Example 1:
nums1 = [1,2,3,2,1]
nums2 = nums1.copy()
nums2.reverse()

if(nums2 == nums1): print("Palindrome")
else: print("Not a palindrome")

# Example 2:
name = "racecar"
print("Palindrome" if name == name[::-1] else "Not a plaindrome" )

# Example 3:
marks = [90, 92, 94, 84, 93]

marks.sort()
print(marks)

marks.append(98)
print(marks)

# marks.clear()
# print(marks)

marks.pop(4)
print(marks)

print(marks[1:4])
print(marks[-3: -1])