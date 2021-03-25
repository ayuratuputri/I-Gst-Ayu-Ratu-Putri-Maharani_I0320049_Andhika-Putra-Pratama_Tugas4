#exercise 4.1
x = 15
y = 4

# Output : x + y = 19
print('x + y =', x+y)

#Output: x - y = 11
print('x - y =', x-y)

#Output: x * y = 60
print('x * y =', x*y)

#Output: x / y = 3.75
print('x / y =', x/y)

#Output: x // y = 3
print('x // y =', x//y)

#Output: x ** y = 50625
print('x ** y =', x**y)

#exercise 4.2
x = 15
x = 10
y = 12

# Output: x > y is False
print('x > y is', x>y)

#Output: x < y is True
print('x < y is', x<y)

#Output: x == y is False
print('x == y is', x==y)

#Output: x != y is True
print('x != y is', x!=y)

#Output: x <= y is True
print('x <= y is', x<=y)

#exercise 4.3
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

#exercise 4.4
#string

str1 = "Hello"
str2 = "World"

# concat
result = str1 + " " + str2

#Output
print(result);

#exercise 4.5
# string
str = "HA"

# replicate
result = str * 3

#Output
print(result)

#exercise 4.6
# string
needle = "lo"
haystack = "Hello World"

# check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#exercise 4.7
#strings
needle = "HA"
haystack = "Hello World"

#check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")

#exercise 4.8
# string
str = "Jane Doe"

# character
ch = str[1]

#output
print(ch)   # a

#exercise 4.9
# string
str = "Hello World"

#substring
substr = str[3:5]

print(substr)   #lo

#exercise 4.10
# string
str = "Hello World"

# skip
new_str = str[0::2]
print(new_str)

#exercise 4.11
# string

str = "Hello World"


#reverse
result = str[::-1]

#output
print(result)
