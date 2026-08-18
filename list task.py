#1 Take a name and print it in uppercase.
a="gunaswetha"
print(a.upper())

# o/p:GUNASWETHA


#2 Take a name and print the number of characters.
b="hello world"
print("number of characters:", len(b))

#o/p:number of characters: 11

#3 Take a string and print its first and last character.
c="hi hello"
print("First character:", c[0])
print("Last character:", c[-1])

#o/p:First character: h
#   Last character: o

#4 Reverse a string using slicing.
d="python"
print("Reversed string:",d[::-1])

#o/p:Reversed string: nohtyp

#5  Take a sentence and count how many times "a" occurs.
e="Take a sentence and count how many times a occurs"
print(e.count("a"))

#o/p:5

#6 Take a person's full name and convert it to title case.
f="gunaswetha h"
print(f.title())

#o/p:Gunaswetha H

#7 Take an email address and check whether "@" exists.
g="gsgunaswetha@gmail.com"
if "@" in g:
    print("The email is valid")
else:
    print("The email is invalid")

#o/p:The email is valid


#8 Take a sentence and replace "Java" with "Python".
h="I like Java programming"
print(h.replace("Java","Python"))

#o/p:I like Python programming

#9 Take a string and check whether it contains "Python".
i="I am learning Python programming"
if "Python" in i:
    print("The string contains Python")     
else:
    print("The string does not contain Python")

#o/p:The string contains Python