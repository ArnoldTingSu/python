

#Create a Python file called for_loop_basic1.py that performs the following tasks.


#1. Basic - Print all integers from 0 to 150.

for x in range(0, 151, 1):
    print("counting to 150 - ", x)
    print("okie, im done counting")


#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(0, 1001, 5):
    print("counting to 1000 by 5 - ", x)
    print("im done counting by 5s")


#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for x in range(0, 101, 1):
    if(x % 10 == 0):
        print("Coding Dojo")
    elif(x % 5 == 0):
        print("Coding")
    else:
        print(x)


#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

#sum = 0
#for x in range(1,500000, 2):
#    sum+=x
#    print("current number: ",sum)


#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for x in range(2018, 0 , -4):
    print(x)


#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexible_counter(low_num, high_num, mult):
  for i in range(low_num, high_num + 1):
    if i % mult == 0:
      print(i)

flexible_counter(2, 9, 3)
#### ask Michael about this question ####