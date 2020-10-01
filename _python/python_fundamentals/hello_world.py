# 1. TASK print "Hello World"
print("Hello World")

# 2a. Store your name in a variable, use it to print the string: "Hello {{your name}}"
name = "Arnold"
print("Hello",name) #with a comma
print("Hello " + name) #with a +
# 3. Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function
favNumber = 11
print("Hello", favNumber) # with a comma
print("Hello " + str(favNumber)) # with a + # help
# 4. Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings
favorite_1 = "eggs"
favorite_2 = "bacon"
print(f"My favorite foods are breakfast items like {favorite_1} and {favorite_2}") 