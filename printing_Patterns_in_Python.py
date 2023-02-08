# for i in range(4):
#     for j in range(4):
#         print("# ",end="")

#     print()

# print()
# for i in range(4):
#     for j in range(i+1):
#         print("# ",end="")

#     print()  


# print()
# for i in range(4):
#     for j in range(4-i):
#         print("# ",end="")

#     print()    

# nums = [12,16,18,21,26]

# for num in nums:

#     if num % 5 == 0:
#         print(num)
#         break

# else:
#     print("not found")      

# num=10

# for i in range(2,num):
#     if num%i==0:
#         print("Not Prime")
#         break

# else:
#     print("Prime")

from array import *
vals = array('i', [5,9,-8,4,2])

print(vals)
print(vals.buffer_info())

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)    

newArr = array(vals.typecode, (a for a in vals))

for e in newArr:
    print(e) 

newArr2 = array(vals.typecode, (a*a for a in vals))

i=0

while i<len(newArr2):
    print(newArr2[i])
    i+=1




       