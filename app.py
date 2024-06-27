
from cal_func import do_addition ,do_substraction
def main():
    print("welcome to the calculator")
    print("""
          \nselect fun1
          ction form the options 
          1.add
          2.substract
          """)
    user_input = input("select function")
    a=int(input(("Val of A")))
    b=int((input("Val of B")))

    if user_input =="1":
        result= do_addition(a,b)
    elif user_input =="2":
        result= do_substraction(a,b)
    print("result",result)
if __name__=="__main__":
    main()
