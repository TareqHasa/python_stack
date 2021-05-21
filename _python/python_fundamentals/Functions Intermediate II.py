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

x[1][0]=15
print(x)

students[0]["last_name"]="Bryant"
print(students)

sports_directory["soccer"][0]="Andres"
print(sports_directory)

z[0]["y"]=30
print(z)

############################################################################

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students) :
    for i in range (len(students)):
        students_dictionary=students[i]
        for key,value in students_dictionary.items():
            print(f"{key} -{value}")
        

iterateDictionary(students)
###############################################################################
def iterateDictionary2(key_name, some_list):
    for i in range (len(some_list)):
        print (some_list[i][key_name])

print (iterateDictionary2("first_name",students))

iterateDictionary2('last_name', students)

##############################################################



def printInfo(dojo):
    for key,value in dojo.items():
        print(f"{len(value)}{key.upper()}")
        for item in value:
            print(item)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)