# s="Pyhton"
# print (s[0],s[-1],s[6])    Q1 : s[6] is out of range. so,it will give an error mesage .  

# s="Python"              s[6] normal index kudutha out of range error varum.
# print(s[0:6])           s[0:6] kudutha 0 to 5 index varai print aagum. so, it will print "Python"

s="Python"
print(s[0],s[-1],s[4])      #Q1: correct format 


num=13
for i in num:
    if i % 2==0:
        print("this number is even")
    else:
        print("this number is odd")
