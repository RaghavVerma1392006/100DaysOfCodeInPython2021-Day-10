#Write your code below this row 👇
total = 0
for number in range(2,101,2):
	total += number 
print(total)

# or
total1 = 0
for number in range(1,101):
	if number % 2 == 0:
		total1 += number 
print(total1) 