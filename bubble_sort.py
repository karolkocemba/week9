import random

def sort(items):

	n = len(items)

	while n > 0:
		for i in range(n-1):
			if items[i] > items[i+1]:
				temp = items[i]
				items [i] = items[i+1]
				items [i+1] = temp
		n-=1
	
	return items

numbers = list(range(10))
random.shuffle(numbers)
# print(numbers)
# print(sort(numbers)) 

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
