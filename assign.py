def recarea():

       area = length * breadth
       print("Area of rectangle is : ",area)

def recperi():

       peri = 2 * length * breadth
       print("Perimeter of rectangle is : ",peri)

def squarea():

       area = 4 * length
       print("Area of square is : ", area)



print("Menu-\n"

       "1. Area of Rectangle\n"

       "2. Perimeter of Rectangle\n"

       "3. Area of Square\n")


x = int(input("Enter the corresponding choice : "))

if x == 1:

       length = int(input("enter the length of the rectangle : "))
       breadth = int(input("enter the breadth of the rectangle : "))
       recarea()
elif x==2:
       length = int(input("enter the length of the rectangle : "))
       breadth = int(input("enter the breadth of the rectangle : "))
       recperi()

elif x==3:
       length = int(input("enter the length of the square : "))
       squarea()

else:

   print("Wrong Input!")

