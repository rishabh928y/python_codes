# def add(x,y):
#     c = x+y
#     return c

# result = add(5,4)
# print(result)

# from tkinter import Y


# def add_sub(x,y):
#     c = x+y
#     d = x-y
#     return c,d

# result1,result2 = add_sub(5,4)
# print(result1, result2)

# def update(lst):
#     print(id(lst))
    
#     lst[1] = 25
#     print(id(lst))
#     print("x ", lst)
    
# lst = [10,20,30]
# print(id(lst))
# update(lst)
# print("lst ", lst)    

# def sum(a, *b):      # *b is the variable length argument 
    
#     c = a
    
#     for i in b:
#         c = c+i
        
#     print(c)
    
# sum(5,6,34,78)            

# def person(name, **data):
#     print(name)
#     print(data)
    
# person('navin', age = 28, city='Mumbai', mob = 9865432)  

# def person(name, **data):
    
#     print(name)
    
#     for i, j in data.items():
#         print(i,j)
        
# person('navin', age = 28, city='Mumbai', mob = 98765432)   

# from re import A


a = 10

# def something():
#     global a
#     a = 15
#     print("in fun ",a)
    
# something()

# print("outside", a)   

a = 10
# print(id(a))

# def something():
#     a = 9
#     x = globals()['a']
#     print(id(x))
#     print("in fun " ,a)
    
#     globals()['a'] = 15 
    
# something()

# print("outside", a)

import matplotlib.pyplot as plt
import seaborn as sns
  
sns.distplot([0,1,2,3,4,5])
plt.show()    
           