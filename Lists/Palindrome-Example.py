# Example 1:
nums1 = [1,2,3,2,1]
nums2 = nums1.copy()
nums2.reverse()

if(nums2 == nums1): 
    print("Palindrome")
else: 
    print("Not a palindrome")

# Example 2:
name = "racecar"

print("Palindrome" if name == name[::-1] else "Not a plaindrome" )