import random

#Sample dictionary - Key will always be on the left, value on the right
phonebook = {} #can append a dictionary as well
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

"""
mydictionary = dict(m = 8, n = 9)

print(mydictionary)

print(f"Number of key-value pairs: len(phonebook)")


print()
print('*****  start section 1 - print dictionary ********')
print()





print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

#key error means it didn't find a match for your key, ex. if below was lowercase C it would have key error

name = "chris"

if name in phonebook:
    print(phonebook[name])

else:
    print(f"{name} does not exist in the phonebook")





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook["Chris"] = "555-4444"

phonebook["Joe"] = "555-0123"
#If a key already existed (Chris), it will merely update the value of that key.
#If a key didn't exist (Joe) it will append the dictionary
print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)
#If the key u are trying to delete does not exist it will result in an error

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

#Default setting will iterate through key
for key in phonebook:
    print(f"The key is: {key} and the value is {phonebook[key]}")

#Need .values to iterate through values
for value in phonebook.values():
    print(value)

#does both
for k, v in phonebook.items():
    print(f"The key is: {k} and the value is {v}")

#produces a tuple if you dont split up the elements into k and v
for ph_tuple in phonebook.items():
    print(ph_tuple)



print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

name = "chris"

#.get will return the value of a specified key, u can write a message if it isnt found
phone = phonebook.get(name, "key not found")

print(phone)

#doesn't delete the key, just clears the value
phonebook.clear()

print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop("Chris", "Not found")

print(remove)

print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()

print(a)
#pops out the last item, even though it is supposed to be random
print(phonebook)




print()
print('*****  end section 8 ********')
print()

"""

print()
print('*****  start section 9 - using random and converting to list ********')
print()

#Will make a list of keys by default
list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)

print(random_key)
print(phonebook[random_key])

#preferred to do it this way bc it is more efficient with no variables
print(phonebook[random.choice(list(phonebook))])



print()
print('*****  end section 9 ********')
print()








