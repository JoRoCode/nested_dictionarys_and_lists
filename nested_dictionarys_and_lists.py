# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
# 3. In the sports_directory, change 'Messi' to 'Andres'
# 4. Change the value 20 in z to 30


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

x[1][0] =15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

print(x)
print(students[0]['last_name'])
print(sports_directory['soccer'][0])
print(z)

# 2. key and the associated value. For example, given the following list:Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for student in range(len(list)):
        for key,val in list[student].items():
            print(key, "-", val)
            
iterateDictionary(students)


# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
    
# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name, some_list):
    for student in range(len(some_list)):
        print(students[student][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size # of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict_name):
    for each_key in dict_name:
        print(len(dojo[each_key]), each_key)
        print(*dojo[each_key], sep = '\n')
printInfo(dojo)