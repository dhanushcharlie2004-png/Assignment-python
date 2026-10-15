name="Dhanush"
result= name[0].lower() + name[1:].upper() #first letter in lower case and remaining in upper case
print(result)

name="Mohammad Nasir"
words=name.split() #swapping the first and last words and using (split concept)
print(words[1]+ words[0]) 

name="Mohammad Nasir"
print(name.split())  #split concept (convert string to list)

name1=["Mohammad","Nasir"]
print(" ".join(name1))      #join concept (convert list to string) and (" " without this symbol join will not work) 

name="Mohammad Nasir"
FN=name[0:8]          #using slicing concept and swappling two words
LN=name[9:14]
print(LN+FN)

name="Dhanush" 
print(name[::-1]) #reverse string

name="Dhanush hari"
dh=name.split()         # split ,reverse and join concept
print(dh)
reverse=dh[::-1]
print(reverse)
print(" ".join(reverse))

name="hari krishnan"
print( " ".join(name.split() [::-1]))  # short form of split,reverse and join concept

name="Dhanush" 
print(name[0])    # indexing concept
print(name[1])

name="harish"
print(name.capitalize())  #capitalize concept (first letter only in upper case)

name="hari krishnan"
print(name.title())    # title concept (first letter of each word in upper case)

name="hari krishnan"
print(name.swapcase())  # swapcase concept (upper case to lower case and lower case to upper case)

name="hari krishnan"
print(len(name))   # length concept (counting the number of characters in the string) 

name="hari krishnan"
print(name.replace("hari","harish"))  # replace concept (replacing a word in the string with another word)

name="hari krishnan"
print(name.count("h"))  # count concept (counting the number of occurrences of a character in the string)

name="hari krishnan"
print(name[6:9])    # slicing concept (extracting a substring from the string)

name="hari krishnan"
print(name [1] + name[11])
print(name[1])               #indexing concept (same letter)
print(name[11])  

name="hari krishnan"                  
age="21"                               # Formatting string concept (important concept)
print(f" My name is {name} and I am {age} years old")   

First_name="hari"
Last_name="krishnan"                    #concatenation concept (joining two strings)
print(First_name + " " + Last_name)

name="hari krishnan"
print(name.index("a"))
  # index concept (finding the index of a character in the string)

s="Pythonh"# 
print(s[4:1:-1]) # slicing concept (extracting a substring from the string in reverse order)




