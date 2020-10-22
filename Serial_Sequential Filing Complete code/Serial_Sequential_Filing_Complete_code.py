choice = 0
import re
import os

#complete
#Appending file
def Command1_Click():
#-------------------------------------------------------------------------
    s = 0
    m = open("nubers.txt", "a")
    m = open("nubers.txt", "r")
    s = int(m.read())
    s = s + 1
    m = open("nubers.txt", "w")
    m.write(str(s))
    m = open("nubers.txt", "r")
    m.close
#-------------------------------------------------------------------------
    RollNo = 0
    sName = ""
    f = open("stuFile.txt", "r")
    f = open("stuFile.txt", "a")
    RollNo = s
    RN = str(RollNo)
    f.write(RN)
    print("Enter Student Name")
    sName = input()
    f.write(":" + sName + " ")
    print("_" * 100)


#complete
# read fron a file
def Command2_Click():
    os.system('cls')
    RollNo = 0 
    sName = ""
    f = open("stuFile.txt", "r")
    print(f.read())
    f.close()
    print("_" * 100)





# ADD a record in sequence
def Command3_Click():
   final_str = ""
   q = ""
   e = ""
   f = open("stuFile.txt", "r")
   e = f.read()
   le = len(e)
   print("Enter roll number")
   c = input()
   r = e.find(c)
   print("")  
   m = open("nubers.txt", "r")
   s = m.read()
   if r > 0:
       print("This Roll nuber already exist")
   elif c < s:
       j = 0
       k = 0
       print("Enter Student name")
       sName = input()
       d = open("deleted_number.txt", "a")
       d.write("0")
       d = open("deleted_number.txt", "r")
       g = d.read()
       v = g.find(c)
       sa = int(g[v])
       if sa > 0:
          j = sa - 1
          k = sa + 1
          j = str(j)
          k = str(k)
          bl = e.find(j)
          for count4 in range (bl, le):
             qw = e.find(" ")

          b = bl + qw
          m = e.find(k)
          sb = e[0 : b]
          sa = e[m : le]
          final_str = sb + " " +  c + ":" +  sName + " " + sa 
          f = open("stuFile.txt", "w")
          f.write("")
          f.close()
          f = open("stuFile.txt", "a")
          f.write(final_str)
          f = open("stuFile.txt", "r")
          print(f.read())
          
   else:
       Command1_Click()

   print("_" * 100)
      

  

 
     





#complete
# DELETE a record from the file
def Command4_Click():

    RollNo = 0
    count = 0
    h = ""
    g = ""
    finalStr = ""
    f = open("stuFile.txt", "r")
    w = f.read()
    RollNo = input(" enter the roll no of the name you wanna delete: ")
    e = w.find(RollNo)
    p = len(w)
    for Count in range (e, p):
        char = w[Count : Count + 1]
        if char != " ":
            count = count + 1
        else:
            break

    d = open("deleted_number.txt", "a")
    d.write(str(RollNo))
    d = open("deleted_number.txt", "r")
    print(d.read())

    count3 = count + e
    h = w[0 : e]
    g = w[count3 : p]
    finalStr = h + g
    f = open("stuFile.txt", "w")
    f.write("")
    f.close()
    f = open("stuFile.txt", "a")
    f.write(finalStr)
    f = open("stuFile.txt", "r")
    print(f.read())
    print("_" * 100)


#complete
#EDIT a record in the file
def Command5_Click():
  
    RollNo = 0
    count = 0
    h = ""
    g = ""
    finalStr = ""
    f = open("stuFile.txt", "r")
    w = f.read()
    RollNo = input(" enter the roll no of the name you wanna edit: ")
    e = w.find(RollNo)
    p = len(w)
    for Count in range (e, p):
        char = w[Count : Count + 1]
        if char != " ":
            count = count + 1
        else:
            break
    sName = input("Enter the student name you want to replace on the place on previous student :")

    count3 = count + e
    h = w[0 : e]
    g = w[count3 : p]
    finalStr = h + RollNo + ":"+ sName + g
    f = open("stuFile.txt", "w")
    f.write("")
    f.close()
    f = open("stuFile.txt", "a")
    f.write(finalStr)
    f = open("stuFile.txt", "r")
    print(f.read())
    print("_" * 100)

#SEARCH a record from the file
def Command6_Click():
     i = ""
     r = ""
     print("Please enter the first letter in capital")
     i = input("Enter what you looking for: ")
     i = i.upper()
     pattern = re.compile(i)
     f = open("stuFile.txt", "r")
     r = f.read()
     r = r.upper()
     result = pattern.findall(r)
     s = r.find(i)
     if s > 0:
         print("Search found!!")
     else:
         print("This Student do not exist in our list")

     print("_" * 100)
   
     
      

#formate file
def MyFix():
   f = open("stuFile.txt", "w")
   m = open("nubers.txt", "w")
   m.write("0")
   f.write("") 
   d = open("deleted_number.txt", "w")
   d.write("")

Answer = input("Are you using this program for the first time, if yes then enter Y: ")
if Answer == "Y":
    MyFix()


choice = 0
while choice != 8:
       os.system('cls')
#Serial Sequential Filing Complete code
       print("Enter 1 to APPEND record to the file")
       print("Enter 2 to READ record from the file")
       print("Enter 3 to ADD a record in sequence")
       print("Enter 4 to DELETE a record from the file")
       print("Enter 5 to EDIT a record in the file")
       print("Enter 6 to SEARCH a record from the file")
       print("Enter 7 to formate file")
       print("Enter 8 to exit")
       print("_" * 100)

       choice = int(input("Your choice...")) 

       if choice == 1:
           Command1_Click()
       elif choice == 2:
           Command2_Click()
       elif choice == 3:
           Command3_Click()
       elif choice == 4:
           Command4_Click()
       elif choice == 5:
           Command5_Click()
       elif choice == 6:
           Command6_Click()
       elif choice == 7:
           MyFix()

