x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def rewrite(scan_list):
    for current_dict in scan_list:
        string_to_print = ""
        for current_key in current_dict.keys():
            string_to_print += f"{current_key} -- {current_dict[current_key]}, "
        string_to_print = string_to_print[:len(string_to_print) -2]
        print(string_to_print)

rewrite(students)

def get_values(key, current_list):
    for values in current_list:
        print(values[key])

get_values('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(current_dict):
    for values in current_dict.keys():
        print(len(current_dict[values]), values.upper())
        for items in current_dict[values]:
            print(items)
        print('\n')

printInfo(dojo)