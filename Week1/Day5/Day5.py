sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
#print(f'History: {}')
print(sample_dict["class"]["student"]['marks']['history'])

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
for rem in keys_to_remove:
    del sample_dict[rem]
print(sample_dict)

my_list = []
#my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
my_list = [ i*j for i in [100,200,300] for j in [1,2,3]]
print(my_list)

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
new_year = 1
print(family_age.items())
new_family_age = {name: age+new_year for (name, age) in family_age.items()}
print(new_family_age)

