import csv
with open('insurance.csv') as insurance_costs:
    insurance_costs_data = csv.reader(insurance_costs)
    for row in insurance_costs_data:
        print(row)