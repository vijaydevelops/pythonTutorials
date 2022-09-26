a = 10
b = 5
if a > b :
	print("Valid condition check 1")
if a < b :
	print("Valid condition check 2")
else:
	print("Else block")



# print("Valid short hand condition check 1") if a > b 			# error: else expected here

print("Valid short hand condition check 1") if a > b else print("Else required in short hand notation")

# also valid - one line if statement
if a > b : print("Valid condition check 1")

#multiple else blocks in one line
print("Valid 1") if a > b else print("Else ==") if a == b else print("Else 1")