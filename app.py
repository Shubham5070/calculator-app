
from cal_func import do_addition ,do_substraction ,do_division
from multiply import do_multiply
def main():
    print("welcome to the calculator")
    print("""
          \nselect fun1
          ction form the options 
          1.add
          2.substract
          3.Multiply
          """)
    user_input = input("select function")
    a=int(input(("Val of A")))
    b=int((input("Val of B")))

    if user_input =="1":
        result= do_addition(a,b)
    elif user_input =="2":
        result= do_substraction(a,b)
    elif user_input =="3":
        result= do_multiply(a,b)
    elif user_input =="4":
        result= do_division(a,b)

    print("result",result)
if __name__=="__main__":
    main()
