######String Entry##############
s = input("Enter your string : ")
a = {i:s.count(i) for i in s}
print("Count of all characters in String is :\n "+
str(dict(a)))

a_length = len(a)
a_value = list(a.values())
a_max = max(a_value)
a_new = [a_max - a_value[i] for i in range(a_length)]


if(a_new.count(0)==a_length or a_new.count(0)==1):
    print("My String")

else:
    print("Not My String")
