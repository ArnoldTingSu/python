#1
def a():
    return 5
print(a())
## returns a as 5. prints 5
print("end of 1")
#2
def a():
    return 5
print(a()+a())
print"end of 2"
## should print10. .

#3
def a():
    return 5
    return 10 #prints 10, acutally returns 5
print(a())
print("end of 3")


#4
def a():
    return 5
    print(10)
print(a()) # returns 5 and prints 10, only returns 5.
print("end of 4")



#5
def a():
    print(5)
x = a()
print(x) #prints 5, doesnt print anything, because a() was never called
print("end of 5")


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))  # 3 + 5. returns 8, gets type error return**
print("end of 6")

#7
def a(b,c):
    return str(b)+str(c) # turns numbers into string**
print(a(2,5)) ##should return 7*, acutally returns "25" directly as a string
print("end of 7")

#8    
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
	else:
		return 10
        return 7
print(a()) # returns 100 and 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # prints 7
print(a(5,3)) # prints 14
print(a(2,3) + a(5,3)) #prints 21
print("end of 8")


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # should return 8, returns 8.
print("end of 9")

#11
b = 500
print(b) # prints 500
def a():
    b = 300
    print(b) # prints 300
print(b) # prints 300, 300
a() # prints 300,300
print(b) #prints 300 -- acutaly prints 500
print("end of 11") #(prints 500, 300, 500)

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
print("end of 12") # 500, 500, 300, 300, 500


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a() # acutally calls and changes b = 300
print(b)
print("end of 13") # 500, 500, 500 500,// 500, 500, 300( gets printed from a() and final is from last print(b). ==> 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
print("end of 14") # 1, 3 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
print("end of 15") # prints 1, x =?, prints 3, x = 5? print 5 #>> 1,3,5,10