#Program1
age = int(input("How old are you?: "))

if age >= 18 :
    print("You are a voter")
else:
    print("You are not a voter")
    print()

#Program2
temperature = float(input("Enter Currrent Room Temperature e.g 25.0: "))

if temperature > 25.0:
    print("It is too hot")

elif temperature < 25.0:
    print("It is too cold")

else:
    print("Normal Temperature")
print()

#Program3
first = int(input("Enter First Number "))
second = int(input("Enter Second Number "))
third = int(input("Enter Third Number "))

if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest number")







