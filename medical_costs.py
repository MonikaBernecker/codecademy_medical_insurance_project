import csv
# CSV-Datei öffnen und Daten in Listen speichern

# Listen für jede Spalte
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# CSV-Datei öffnen und Daten in Listen speichern
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

# Zum Testen die ersten Datenpunkte ausgeben
print(sex[:5])
print(age[:5])
# ... und so weiter für die restlichen Spalten
