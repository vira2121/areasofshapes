def rectangle(a,b):
    return a*b

def perimeter_rect(a,b):
    return 2*(a+b)

def area_square(a):
    return a*a


if __name__=="__main__":

    check = 1
    while check:
        c = int(input("main menu \n 1) Find Area of rectangle\n 2) Find perimeter of Rectangle \n 3) Find Area of Square\n 4) Exit"))

        if c==1:
            length = int(input("Enter the length of rectangle: "))
            breadth = int(input("Enter the breadth of rectangle: "))
            result = rectangle(length,breadth)
            print(result)

        elif c==2:
            length = int(input("Enter the length of rectangle: "))
            breadth = int(input("Enter the breadth of rectangle: "))
            result1 = perimeter_rect(length,breadth)
            print(result1)
        elif c==3:
            side = int(input("Enter side of square: "))
            result2 = area_square(side)
            print(result2)
        else:
            check = 0
            print("Exit")