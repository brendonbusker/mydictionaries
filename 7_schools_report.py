"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json', 'r')

schools = json.load(infile)
conference_schools = [372, 108, 107, 130]
schools_women_grad_rate = []
schools_off_campus = []

print(type(schools))

#How many schools are in this file?
print(len(schools))


for i in range(0, len(schools)):
    school_dict = schools[i]

    if school_dict["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if school_dict["Graduation rate  women (DRVGR2020)"] > 75:
            schools_women_grad_rate.append(school_dict["instnm"])
        
        if school_dict["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            schools_off_campus.append(school_dict["instnm"])

print("Schools With Women Grad rate above 75% : ")
