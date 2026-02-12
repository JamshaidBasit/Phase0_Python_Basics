#Program ka rasta decide karne ke liye.
#if / elif / else

age=int(input("Enter your age please"))
if(age>18):
    print("Eligible!You can caste a vote")
elif(age<18 and age>12):
    print("Phaly bara hoga")
else:
    print("Kia bolo gaali ni dy skta")

###########################################################################################################
#For Loop & While Loop
#For: Jab iteration count pata ho (e.g., list ke elements).
#While: Jab tak condition True hai, chalao.

for i in range(10):    ## start from 0 to 9 
    print(i*"*")
for i in range(1,10):  ## starting(1) and ending(10)
    print(i*"*")
for i in range(1,10,2):  ## start is 1 , end is 10 and increment is 2
    print(i*"*")

while(age<10):
    print(age)
    age=age+1

####################################################################################################
