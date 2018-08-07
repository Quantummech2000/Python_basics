#Python Program to Sort an array of elements using Bubble sort technique

print("\nProgram To Sort an Array of Elements using Bubble Sort technique...")

size  = input("\n Enter the size of array to store the elements you type:")

arr = list()
print ("\n Enter the elements of the array now :")

for i in range(int(size)):
    n = input("Enter the Element :")
    arr.append(int(n))

print("\n Sorting Begins now")
for i in range(size):
	for j in range(0, size-i-1):
	  if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(size):
	print("\n")
	print("%d" %arr[i])
