# While Loop
number = 20 # Initialize your number - set the first number
while number <= 25 :
    print(number) # Set a Condition - to give it a range
    number += 1 # Incrementing
print()

    # Decrementing
count = 105
while count >= 100 :
    print("Number is", count)
    count -= 1
print()

#Break and Continue
a = 20
while a <= 25 :
    print(a)
    if a == 23:
        break
    a += 1
print()

counter = 35
while counter >= 30 :
    if counter == 33:
        counter -= 1
        continue
    print(counter)
    counter -= 1
print()


# For Loop
languages = ["Python", "C++", "Java", "PHP"]
for lang in languages:
    print(lang)
print()

for num in range(5):
    print(num)
print()

for x in range(10,15):
    print(x)
print()

for z in range(10, 20, 3):
    print(z)
print()




