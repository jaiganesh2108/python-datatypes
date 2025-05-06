# operators in python programming
# Assignment operators
a=10 # assigning x value is 10
print(a)
a+=1 # adds
print(a)
a-=3 # subtracts
print(a)
a*=3 # multiplies
print(a)
a/=3 # divides
print(a)
a%=3 # modulus
print(a)
a//=3 # power operations
print(a)
a**=3 # floor division
print(a)
# Arithmetic operations( +,-,*,/,%,//,** )
n1 = 5 # assigning n1 as 5
n2 = 2 # assigning n2 as 2
num = n1 + n2
print("sum of num is:",num)
num = n1 - n2
print("sub of num is:",num)
num = n1 * n2
print("multiple of num is:",num)
num = n1 / n2
print("div of num is:",num)
num = n1 // n2
print("sum of num is:",num)
num = n1 % n2
print("mod of num is:",num)
num = n1 ** n2
print("exponent of num is:",num)
# Relational or comparison operators( <,>,==,!=,>=,<= )
n1 = 2 # assigning n1 as 2
n2 = 3 # assigning n2 as 3
num = n1 < n2
print("value of num is:",num)
num = n1 > n2
print("value of num is:",num)
num = n1 == n2
print("value of num is:",num)
num = n1 != n2
print("value of num is:",num)
num = n1 <= n2
print("value of num is:",num)
num = n1 >= n2
print("value of num is:",num)
# logical operators( and, or, not )
a = 2 < 3 and 4 > 3
print("value of a:",a)
a = 2 < 3 or 4 > 3
print("value of a:",a)
a= not a
print("value of a:",a)
# Bitwise operators ( &,|,^,~,<<,>>)
a = 60 # assigning a as 60
b = 13 # assigning b as 13
c = a & b
print("value of c is:",c)
c = a | b
print("value of c is:",c)
c = a ^ b
print("value of c is:",c)
c = ~a 
print("value of c is:",c)
c = a << 2
print("value of c is:",c)
c = a >> 2
print("value of c is:",c)
# Membership operators( in, not in )
a = 10 # assigning a as 10
b = 20 # assigning b as 20
list = [1,2,3,4,5]
if(a in list):
    print("a is available in the given list")
else:
    print("a is not available in the given list")
if(b not in list):
    print("b is not available in the given list")
else:
    print("b is available in the given list")
# Identity operator ( is, is not )
a=10 # assigning a as 10
b=10 # assigning b as 10
if(a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")
if(id(a)==id(b)):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")
b=30 # assigning b as 30
if(a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")
if(a is not b):
    print("a and b do not have same identity")
else:
    print("a and b have same identity")