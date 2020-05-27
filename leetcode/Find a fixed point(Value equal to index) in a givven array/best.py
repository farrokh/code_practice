# Python program to check fixed point 
# in an array using binary search 
'''
Method 2 (Binary Search)
First check whether middle element is Fixed Point or not. If it is, then return it; otherwise check whether index of middle element is greater than value at the index. If index is greater, then Fixed Point(s) lies on the right side of the middle point (obviously only if there is a Fixed Point). Else the Fixed Point(s) lies on left side.
'''
def binarySearch(arr, low, high): 
	if high >= low: 
		mid = (low + high)//2
	
	if mid is arr[mid]: 
		return mid 
	
	if mid > arr[mid]: 
		return binarySearch(arr, (mid + 1), high) 
	else: 
		return binarySearch(arr, low, (mid -1)) 
	
	# Return -1 if there is no Fixed Point 
	return -1


# Driver program to check above functions */ 
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
n = len(arr) 
print("Fixed Point is " + str(binarySearch(arr, 0, n-1))) 


# This code is contributed by Pratik Chhajer 
