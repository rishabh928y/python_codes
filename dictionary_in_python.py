# dic = { 
#    344: "Harry",
#    56: "Shubham",
#    678: "Zakir",
#    567: "Neha"           
# }

# print(dic[567])

# info = {'name':'Karan', 'age':19, 'eligible':True}
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# # print(info['name'])
# # print(info.get('name'))
# print(info['name2'])  #Throws error if the key doesnot exits.
# print(info.get('name2'))  #doesnot throws the error even if the key doesnot exists.

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())

# for key in info.keys():
#     print(info[key])

# for key in info.keys():
#     print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

