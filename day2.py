""" Python 3 program to remove a given 
element from an array
whether from beginning or any position"""

# function to remove an element x from arr[] 
"""since size of array can't be changed after 
removing therefore reduce the 
size if the element to be removed is found"""
def deleteElement(arr, n, x): 
	
	# first Search x in array 
	for i in range(n): 
		if (arr[i] == x): 
			break

	# If x found in array 
	if (i < n): 
		
		# reduce size of array and move 
		# all elements one space ahead 
		n = n - 1; 
		for j in range(i, n, 1): 
			arr[j] = arr[j + 1] 

	return n 

# Driver Code 
if __name__ == '__main__': 
	arr = [11, 15, 6, 8, 9, 10] 
	n = len(arr) 
	x = int(input())

	# Delete x from arr[] 
	n = deleteElement(arr, n, x) 

	print("Array after deletion of",x) 
	for i in range(n): 
		print(arr[i], end = " ") 
		
