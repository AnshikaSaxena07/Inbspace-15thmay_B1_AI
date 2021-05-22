############### QUESTION 1 ##########################

print("################ QUESTION 1 ###############")
n=[386,462,47,418,907,344,236,375,823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
  758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
   626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
     958,743, 527]
for x in n:
    if x==237:
        print(x)
    elif x%2==0:
        print(x)



############ QUESTION 2 ############################
        
print("################ QUESTION 2 ###############")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)


################# QUESTION 3 ########################

print("################ QUESTION 3 ###############")
a = input('Enter string for checking Pangram : ')
c = {i for i in a if i.isalpha()}
if(len(c) == 26):
    print(a,', is a Pangram')
else :
    print(a,', is not a Pangram')


####################### QUESTION 4 ################################

print("################ QUESTION 4 ###############")
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

###################### QUESTION 5#################################

print("################ QUESTION 5 ###############")
n = input('Enter the string in required fashion : ')
a = n.split('#')
list_1 = a[0].split()
list_2 = a[1].split()
list_1 = [int(i) for i in list_1]
list_2 = [int(i) for i in list_2]

print('list 1 : ',list_1)
print('list 2 : ',list_2)

######################### QUESTION 6#############################

print("################ QUESTION 6 ###############")
i = input("Input comma separated sequence of words::")
words = [word for word in i.split(",")]
print(",".join(sorted(list(set(words)))))

############################## QUESTION 7 ################################

print("################ QUESTION 7 ###############")
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
i = d['Marks'].index(max(d['Marks']))
print(d['Student'][i])

######################### QUESTION 8 #################################

print("################ QUESTION 8 ###############")
s = input("Input a string::")
a=i=0
for c in s:
    if c.isdigit():
        a=a+1
    elif c.isalpha():
        i=i+1
    else:
        pass
print("Letters", i)
print("Digits", a)

###################### QUESTION 9 #####################################

print("################ QUESTION 9 ###############")
a = {'Name': ['Akash', 'Soniy', 'Vishakha','Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

newData = {'Name' : [],'Ratings' : []}
index = 0
for sub in a['Subject']:
    if(sub == 'Python'):
        newData['Name'].append(a['Name'][index])
        newData['Ratings'].append(a['Ratings'][index])
    index += 1 

print('new dictionary of students : ',newData)


############################# QUESTION 10 ##################################

print("################ QUESTION 10 ###############")
class generator_class :
    def __init__(num,n):
        num.n = n
  
    def generator_function(num) :
        for i in range(0,num.n + 1):
            if(not i%7):
                yield i
n = int(input('Enter the value of n : '))
gen = generator_class(n)
gen_list = list(gen.generator_function())
print('List of numbers divisible by 7 in the range 0 and ',n,' = ',gen_list)

####################################### QUESTION 11 ##############################

print("################ QUESTION 11 ###############")
up = eval(input('UP : '))
down = eval(input('DOWN : '))
left = eval(input('LEFT : '))
right = eval(input('RIGHT : '))

net_up = abs(up - down)
net_right = abs(right - left)

total_distance = (net_up**2 + net_right**2)**0.5

print('distance = ',round(total_distance))
