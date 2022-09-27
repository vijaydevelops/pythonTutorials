a = 10
b = 5
if a > b:
	print("Valid condition check 1")
if a < b:
	print("Valid condition check 2")
else:
	print("Else block")



# print("Valid short hand condition check 1") if a > b 			# error: else expected here

print("Valid short hand condition check 1") if a > b else print("Else required in short hand notation")

# also valid - one line if statement
if a > b: print("Valid condition check 1")

#multiple else blocks in one line
print("Valid 1") if a > b else print("Else ==") if a == b else print("Else 1")


#while loop runs based on condition and the iterator(indexing) variable i
#Printing 1 to 10
i = 1
while i <= 10:
	print(i)
	i += 1

#Printing 1 to 3
i = 1
while i <= 10:
	print(i)
	if i == 3:
		break
	i += 1

#Printing 1 to 10 except 3 and 7
i = 0
while i <= 10: #runs till 11
	i += 1
	if i == 3 or i == 7:
		continue
	print(i)

#for loop - iterating over a sequence (also strings)
#list
listFruits = ["apple", "banana", "mango"]
for x in listFruits:
	print(x)

#break and continue can be used in for loops

#range() function variations
#range(start_num = 0, till_integer, step = 1)
#eg:
for x in range(6):
	print(x)	#0 till 5
else:  #runs only when the loop is finished
	print("This Loop is finished")

for x in range(2, 6):
	print(x) 	#2 till 5

for x in range(2, 30, 3):
	print(x)

#nested loop example
for x in "ABC":
	for y in range(1, 6):
		print(x, y)   # prints the values separated by space
