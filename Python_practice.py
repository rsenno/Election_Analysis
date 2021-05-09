print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

print("in module 3.2.10 DICT section")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
    
print("...using keys")

for county in counties_dict.keys():
    print(county)

print("...for values")

for voters in counties_dict.values():
    print(voters)

print("...using dict keys to get dict values")

for county in counties_dict:
    print(counties_dict[county])

print("...using the get() method")

for county in counties_dict:
    print(counties_dict.get(county))

print("...getting key, value pairs")

for county, voters in counties_dict.items():
    print(county, voters)

print("...skills drill")

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " voters.")

print("...review getting each dictionary in a list of dictionaries.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("...interate over the list with the range() function")

for i in range(len(voting_data)):
      print(voting_data[i])
    
print("...getting values via a nested for loop")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("...getting just the values")

for county_dict in voting_data:
     print(county_dict['registered_voters'])

print("...getting just the keys")

for county_dict in voting_data:
    print(county_dict['county'])

print("...in module 3.2.11")
print("...working with f-strings")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

print("...a skill drill")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print("...another skill drill")

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

