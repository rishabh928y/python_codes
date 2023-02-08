# a = input("Enter the number: ")
# print(f"Multiplication tav]ble of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid Input!")
    
# print("Some imp lines of code")
# print("End of program")            

# finally is used when we want to print something even 
# if the function returns

# def func1():
#     try:
#       l = [1, 5, 6, 7]
#       i = int(input("Enter the index: "))
#       print(l[i])
#       return 1  
#     except:
#         print("Some error occurred")
#         return 0
    
#     finally:
#         print("I am always executed")
     
#     #print("I am always executed")
    
# x = func1()
# print(x)        

a = int(input("Enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
