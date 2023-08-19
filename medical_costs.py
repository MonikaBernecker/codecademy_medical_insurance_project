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

