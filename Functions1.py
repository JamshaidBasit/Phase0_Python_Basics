#3. Functions
#Code ko reusable banane ke liye.
#Normal Function: def keyword se banta hai.
#Default Arguments: Agar value na di jaye toh default use ho.
#Lambda: One-liner anonymous function.
#*args / **kwargs: Variable number of arguments (list/tuple) aur keyword arguments (dict) handle karne ke liye

def calculate(a,b):
    sum=a+b
    return sum
a=10
b=50
c=calculate(a,b)
print(c)

def Student_Data(Name,*marks,college_name="MCS NUST"):
    print(f"Name of Student is:{Name} and he studied in {college_name}")
    print(f"Marks Obtain in 3 subjects Math, Physics  and Chemistry Repectively are:{marks}")
Student_Data("Jamshaid Basit",20,30,40)

## Use of lambda fucntion
square=lambda x:x**2  ## define any variable(Square) , lambda funtion with inout varibale(x):formula(logic)
print(square(4))

##power 
import math as mat
Power=lambda x: mat.pow(x,2)
print(Power(3))

##Logrithum
Logritum=lambda x:mat.log(x)
print(Logritum(10))

## Cosint
Cose=lambda x:mat.cos(x)
print(Cose(30))

## Tangent
Tan1=lambda x:mat.tan(x)
print(Tan1(10))