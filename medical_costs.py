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
