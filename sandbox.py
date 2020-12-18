

# a file to simply run code:


print("hellO")

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)


capitals = { "1": "2", "3": "4"}

for key in capitals.keys():
     print(key)

print("keys returned")


for val in capitals.values():
     print(val)

print("values returned")

for key, val in capitals.items():
     print(key, " <---keys // values ----> ", val)

print("keys and values returned")

for count in range(0,500,499):
    print("looping to 499 - ", count)
    print("loop to 499 is done")



    count = 0
while count < 1100:
    print("looping to a big number - ", count)
    count += 7