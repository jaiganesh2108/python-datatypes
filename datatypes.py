# Datatypes in python programming
# string, int, float datatypes
name = "jaiganesh"
age = 5
weight = 23.5
print(type(name))
print(type(age))
print(type(weight))
print(age,"is integer number?",isinstance(5,int))
# string datatype
str1 = 'string in single qoute!'
str2 = "string in double quote!"
str3 = ''' string in triple quote!, 'single' and
 'double' quotes can be used '''
print(str1)
print(str2)
print(str3)
str = "hello world"
print(str)
print(str[0])
print(str[3:6])
print(str[2:])
print(str[-1])
# list datatype
List = []
print("empty list:",List)
List1 = [10,20,30,40]
print(List1)
print(List1[0])
print(List1[2])
print(List1[1:4])
print(List1[-1])
print(len(List1))
# tuple datatype
tuple1 = (2,4,'one',6.5,"hello",10)
tuple2 = (2,4,6)
print("tuple1 :",tuple1)
print("tuple2 :",tuple2)
print(tuple1[0])
print(tuple1[1:])
print(tuple2*2)
# set datatype
set1 = {5,3,7,9,11,13}
print(set1)
print(type(set1))
set2 = {1,2,2,3,3,3}
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
# dictionary datatype
dict1 = {1 : 'value1','key' : 2}
print(dict1[1])
print(dict1['key'])
print(dict1.keys())
print(dict1.values())
