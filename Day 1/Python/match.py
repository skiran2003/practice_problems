day = int(input())
day=day%7
match day:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")     


# Default case in Match

num = 1
match num:
    case 0:
        print("Number is Zero")
    case _:
        print("Number not Zero")


# Combined Match statement

n = int(input())
match n:
    case 2|4|6|8:
        print("Even")
    case 3|5|7|9:
        print("Odd")

# Match combined with if statement

year=int(input("year: "))
month = int(input("month: "))
match month:
    case 2 if year%4==0:
        print("Leap year")
    case 2 if year%4!=0:
        print("not a leap year")