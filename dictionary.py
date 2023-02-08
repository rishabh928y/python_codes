data = {1:'Navin', 2:'Kiran', 4:'Harsh'}
print(data)
print(data[4])
print(data[1])
# print(data[3])  //gives error as key3 is not present
print(data.get(1))
data.get(3)
print(data.get(3))
print(data.get(1,'Not Found'))
print(data.get(3,'Not Found'))
key = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(key, values))
print(data)
print(data['Kiran'])
data['Monica'] = 'CS'
print(data)
del data['Harsh']
print(data)
prog = {'JS':'ATOM', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
print(prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])
print(help())




