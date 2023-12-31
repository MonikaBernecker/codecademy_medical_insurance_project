import csv
# CSV-Datei öffnen und Daten in Listen speichern

# List for each column
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# open CSV file and save each column in a list
with open('insurance.csv') as insurance_costs:
    insurance_costs_data = csv.reader(insurance_costs) 
    header = next(insurance_costs_data) # Kopfzeile überspringen (falls vorhanden)
    for row in insurance_costs_data:

        age.append(row[0])
        sex.append(row[1])
        bmi.append(row[2])
        children.append(row[3])
        smoker.append(row[4])
        region.append(row[5])
        charges.append(row[6])

# Overview
print(sex[:5])
print(age[:5])
print(bmi[:5])
print(children[:5])
print(smoker[:5])
print(region[:5])
print(charges[:5])

# Average Age of the patients
average_age = sum([int(i) for i in age]) / len(age)
print("Average age of the patients: " + str(round(average_age, 2)) + " years")

# Average BMI of the patients
average_bmi = sum([float(i) for i in bmi]) / len(bmi)
print("Average BMI of the patients: " + str(round(average_bmi, 2)))

# Average number of children of the patients
average_children = sum([int(i) for i in children]) / len(children)
print("Average number of children of the patients: "+str(round(average_children, 2))+ ' children')

# The most common region of origin
origin= {}
for r in region:
    if r in origin:
        origin[r] += 1
    else:
        origin[r] = 1

most_common_origin = max(origin, key=origin.get)
print("The most common region of origin is: ", most_common_origin)

#Average cost
average_cost = sum([float(i) for i in charges]) / len(charges)
print("Average cost:",  str(round(average_cost, 2)))

#Gender distribution
distribution = {}
for s in sex:
    if s in distribution:
        distribution[s] += 1
    else:
        distribution[s] = 1
    
most_common_gender = max(distribution, key=distribution.get) 
print('Most Common Gender:', most_common_gender )

#Percantage of smokers with children
all_smoker = 0
smoker_with_children = 0
for s, c in zip(smoker, children):
    if s == "yes":
        all_smoker += 1
        if int(c) > 0:
            smoker_with_children += 1
percentage = (smoker_with_children/all_smoker)*100
print(str(round(percentage, 1)) + " of the smokers have children")

# In which region are the highest costs?
costs_per_region = {}
for r, cost in zip(region, charges):
    if r not in costs_per_region:
        costs_per_region[r] = 0
    costs_per_region[r] += float(cost)
region_with_highest_costs = max(costs_per_region, key=costs_per_region.get)
print("The region with the highest costs is: " + str(region_with_highest_costs))
print("Total cost: " + str(round(costs_per_region[region_with_highest_costs])))

#At which age have patients the highest costs?
costs_per_age = {}
for a, q in zip(age, cost):
    if a not in costs_per_age:
        costs_per_age[a] = 0
    try:
        costs_per_age[a] += float(q)
    except ValueError:
        print(f"Unable to convert {q} to float.")
age_with_the_highest_cost = max(costs_per_age, key=costs_per_age.get )
print("The age with the highest costs is: " + str(round(float(age_with_the_highest_cost))))

