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
def average_age(age):
  """Calculates the average age of a list of patients.

  Args:
    age: A list of integers representing the ages of the patients.

  Returns:
    The average age of the patients.
  """

  total_age = sum([int(i) for i in age])
  num_patients = len(age)
  return total_age / num_patients

# Average BMI of the patients
def average_bmi(bmi):
  """Calculates the average BMI of a list of patients.

  Args:
    bmi: A list of floats representing the BMIs of the patients.

  Returns:
    The average BMI of the patients.
  """

  total_bmi = sum([float(i) for i in bmi])
  num_patients = len(bmi)
  return total_bmi / num_patients

# Average number of children of the patients
def average_children(children):
  """Calculates the average number of children of a list of patients.

  Args:
    children: A list of integers representing the number of children of each patient.

  Returns:
    The average number of children of the patients.
  """

  total_children = sum([int(i) for i in children])
  num_patients = len(children)
  return total_children / num_patients

# The most common region of origin
def most_common_origin(region):
  """Calculates the most common region of origin for a list of patients.

  Args:
    region: A list of strings representing the regions of origin for each patient.

  Returns:
    The most common region of origin.
  """

  origin = {}
  for r in region:
    if r in origin:
      origin[r] += 1
    else:
      origin[r] = 1

  most_common_origin = max(origin, key=origin.get)
  return most_common_origin

#Average cost
def average_cost(charges):
  """Calculates the average cost of a list of charges.

  Args:
    charges: A list of floats representing the charges.

  Returns:
    The average cost of the charges.
  """

  total_cost = sum(charges)
  num_charges = len(charges)
  return total_cost / num_charges

#Gender distribution
def most_common_gender(sex):
  """Calculates the most common gender from a list of strings.

  Args:
    sex: A list of strings representing the genders of the patients.

  Returns:
    The most common gender.
  """

  distribution = {}
  for s in sex:
    if s in distribution:
      distribution[s] += 1
    else:
      distribution[s] = 1

  most_common_gender = max(distribution, key=distribution.get)
  return most_common_gender

#Percantage of smokers with children
def percentage_of_smokers_with_children(smoker, children):
  """Calculates the percentage of smokers who have children.

  Args:
    smoker: A list of strings representing the smoking status of each patient.
    children: A list of integers representing the number of children each patient has.

  Returns:
    The percentage of smokers who have children.
  """

  all_smokers = 0
  smokers_with_children = 0
  for s, c in zip(smoker, children):
    if s == "yes":
      all_smokers += 1
      if c > 0:
        smokers_with_children += 1
  percentage = (smokers_with_children / all_smokers) * 100
  return percentage

# Age with the highest costs
def get_age_with_highest_cost(age, cost):
  """
  This function returns the age with the highest cost.

  Args:
    age: A list of ages.
    cost: A list of costs.

  Returns:
    The age with the highest cost.
  """

  costs_per_age = {}
  for a, q in zip(age, cost):
    if a not in costs_per_age:
      costs_per_age[a] = 0
    try:
      costs_per_age[a] += float(q)
    except ValueError:
      print(f"Unable to convert {q} to float.")
  age_with_the_highest_cost = max(costs_per_age, key=costs_per_age.get)
  return age_with_the_highest_cost