Char1 = ""
char2 = ""
Char3 = ""
NewString = ""

#taking input

print("Please enter the String you want to edit: ")
String1 = input()
print("Please enter the charecter you want to replace: ")
Char1 = input()
print("Please enter the charecter you want to replace With: ")
char2 = input()

r = len(String1)

# Replacing Char

for Count in range (0, r):
    Char3 = String1[Count : Count + 1]
    if (Char3) != (Char1):
        NewString = NewString + Char3
    else:
        NewString = NewString + char2

print(NewString)
