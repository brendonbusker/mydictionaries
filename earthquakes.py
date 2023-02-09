'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

import json



# Main
def main():
   # Loads File
   infile = open('eq_data.json', 'r')
   equakes = json.load(infile)

   # Prints amt of equakes
   print("Total number of earthquakes:", len(equakes["features"]))

   # New dictionaries
   eq_dict = {"earthquakes": []}
   temp_dict = {}

   # Loops thru earthquakes and filters them into new dictionary
   for i in range(0, len(equakes["features"])):
      if equakes["features"][i]["properties"]["mag"] > 6:
         
         temp_dict["location"] = equakes["features"][i]["properties"]["place"]
         temp_dict["magnitude"] = equakes["features"][i]["properties"]["mag"]
         temp_dict["longitude"] = equakes["features"][i]["geometry"]["coordinates"][0]
         temp_dict["latitude"] = equakes["features"][i]["geometry"]["coordinates"][1]

         # Appends to new dictionary
         eq_dict["earthquakes"].append(temp_dict)

         # Resets temp dict
         temp_dict = {}

   # Prints new dictionary
   print(eq_dict, "\n")
         
   # Print out specific info
   for i in range(0, len(eq_dict["earthquakes"])):
      print("Location:", eq_dict["earthquakes"][i]["location"])
      print("Magnitude:", eq_dict["earthquakes"][i]["magnitude"])
      print("Longitude:", eq_dict["earthquakes"][i]["longitude"])
      print("Latitude:", eq_dict["earthquakes"][i]["latitude"])

      print()

   infile.close()

main()

