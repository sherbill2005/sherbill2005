def table():
    """This fuction prints a Table"""
    u = int(input("enter the number you want to print the Table of: "))
    print("This is the Table of ", u)
    for i in range(10):
        i += 1
        xx = lambda a: a * i
        print(u, " x ", i, " = ", xx(u))
if __name__ == "__main__" :
    print("Made by me")

for i in range(10):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    table()


