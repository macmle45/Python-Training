# My second python script in python training

script_info = "Lesson 2/7"
script_info += "\n[Functions, docstrings, arguments]\n"

print(script_info,"\n")

# Example function 1

var1 = 6
var2 = 34

def division_variables(a,b):
    """Division two numbers (int, float) 'a' and 'b'
    parameters: a<int, float>, b<int, float>"""
    result = a/b
    return result

example = division_variables(var1, var2)

help(division_variables)
print(example,"\n")


# Example function 2

my_text = "ala ma kota"

# function without return (void)
def show_text(text):
    print(text+" <-- this text is print by function\n")

show_text(my_text)


# Function with arguments and default arguments

def say_hi(name="Johny"):
    result = "Hi "+name+"!"
    return result

print(say_hi(),say_hi("Peter"), sep="\n")

