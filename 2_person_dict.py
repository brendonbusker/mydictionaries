person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}


print(person)
#Name of the 2nd child
print(person["children"][1])

#Name of the cat
print(person["pets"]["cat"])

#For loop to list each child
for child in person["children"]:
    print(child)

#print out pets
for i, j in person["pets"].items():
    print(f"Type of pet:{i} name of pet: {j}")