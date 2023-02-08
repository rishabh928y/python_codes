# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
    
# # average(4, 6)
# average(b = 9)

# def name(fname, mname = "John", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
    
# name("Amy", "Agarwal", "Jain")        

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i    
#     print("Average is: ", sum / len(numbers))    
    
    
# average(5, 6, 7, 1)    

def name(**name):
    # print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])
    
name(mname = "Buchanan", lname = "Barnes", fname = "James")    