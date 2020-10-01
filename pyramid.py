Answer = 'Y'
print("Please enter, how many times you want to repeat this loop")
r = input()
r = int(r)
for maincount in range(r):
    print("please enter the hight ")
    h = int(input())
    for Count in range(1, h):
     b = ""
     c = ""
     f = h - Count
     g = (Count * 2) - 1
     for count1 in range(f, 0, -1) : 
         b = b + " "
     for count2 in range(0, g):
         c = c + "*"
     e = b + c
     print(e)
    print('Do you want to repeat this loop ')
    Answer = input("")
    Answer = Answer.upper()
    if Answer == 'N':
     break
