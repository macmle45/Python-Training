# My first python script in python training

# Value assigment with '=' operator
script_info = "Lesson 1/7"
script_info += "\n[Comments, Variable Types, Arithmetic operations]\n"

print(script_info)

print("Assignment:\n")

# Data Types
a = 3
b = 4.56
c = -5
d = 6.32
e = "test string"
f = True

print("a =", a,"\nb =", b,"\nc =", c,"\nd =", d,"\n\n---\n")

print("Data types:\n")

a_type = type(a)
b_type = type(b)
c_type = type(c)
d_type = type(d)
e_type = type(e)
f_type = type(f)

print("a: ", a_type,"\nb: ", b_type,"\nc: ", c_type,"\nd: ", d_type,"\ne: ", e_type, "\nf: ", f_type,"\n\n---\n")

# Arithmetic operations
# Order of operations: PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print("Arithmetic operations:\n")

print("a+b= ",a+b)
print("b-c= ",b-c)
print("c/a= ",c/a)
print("c//a= ",c//a)
print("c*d= ",c*d)
print("a**c= ",a**c)
print("d%b= ",d%b)
print("-c= ",-c,"\n\n---\n")

# min, max and abs functions

print("Min, max and abs functions\n")

print("(",a,",",b,",",c,")\n")

print("min: ",min(a, b, c))
print("max: ",max(a, b, c))
print("abs: ",abs(c),"\n\n---\n")

# Conversion

print("Conversion\n")

print("Int->Float: ",float(a))
print("Float->Int: ",int(b)) 
print("String->Int: ",int('567')+1)
