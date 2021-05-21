#######################################
#For Registration of User
#######################################

print("REGISTER")
Fullname=input("Enter Your Full Name: ")
username=input("Enter Your Usename: ")
password=input("Enter Your Password: ")


print(Fullname, "YOU ARE READY TO GO")
print("\n")

######################################
#LOGIN FOR USER
######################################

print("LOGIN")
user = input("Enter Your Username")
pwd =input("Enter Your Password")

###################################
#LOGIN VERIFICATION
###################################

if user == username:
    if pwd == password:
        #if both are correct
        while True:
            print("Choose among the Following")
            print("1.Pattern Generator")
            print("2.Table Generator")
            print("3.Basic Calculator")
            a=int(input("Enter Your Choice :::: "))
            print("\n")
            if a==1:
                ########Pattern Generator################
                print("Pattern Generator")
                n=int(input("Enter number of rows you want to print in a pattern:::"))
                for i in range(1,n+1):
                      print(i*"$")
            if a==2:
                      ############Table Generator################
                      print("Table Generator")
                      u=int(input("Enter which Number Table you want to print:::"))
                      for i in range(1,11):
                       print(u, "X",i,"=",u*i)
            print("\n")
                      
            if a==3:
                ############Basic Calculator####################
                print("Basic Calculator")
                print("Enter 1 for Addition")
                print("Enter 2 for Subtraction")
                print("Enter 3 for Multiplication")
                print("Enter 4 for Division")
                b=int(input("Enter Your Choice ::::: "))
                Firstnum = int(input("Enter Your First Number:: "))
                Secondnum = int(input("Enter Your Second Number:: "))
                if b==1:
                    Add = Firstnum+Secondnum
                    print("Addition of the Numbers are" , Add)
                elif b==2:
                    Sub = Firstnum-Secondnum
                    print("Subtraction of the Numbers are" , Sub)
                elif b==3:
                    Mul = Firstnum*Secondnum
                    print("Multiplication of the Numbers are" , Mul)
                elif b==4:
                    Div = Firstnum/Secondnum
                    print("Division of the Numbers are" , Div)
                else:
                    print("You have Selected a Wrong Choice")
    else:
        print("You have Entered a Wrong Password")
else:
    print("You have Entered a Wrong Username")
            
                    
                
                
                  

        
