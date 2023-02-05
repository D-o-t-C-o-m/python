import csv
import os

# Get the list of all .csv files in the current directory
files = [f for f in os.listdir() if f.endswith(".csv")]

# Display the list of files
for i, file in enumerate(files):
    print(f"{i+1}. {file}")

# Ask the user to choose a file
file_index = int(input("Enter the number of the file you want to open: "))
file_path = files[file_index - 1]

# Load the CSV file
with open(file_path) as file:
    reader = csv.reader(file)
    sheet = list(reader)

# Specify the locations of the data

ActualSales = sheet[2][0]
BudgetSales = sheet[2][2]

ActualMTO = sheet[40][0].replace(",", "")
BudgetMTO = sheet[40][2].replace(",", "")

ActualOTHERFRESH = sheet[42][0].replace(",", "")
BudgetOTHERFRESH = sheet[42][2].replace(",", "")

ActualShrink = sheet[81][1]
BudgetShrink = sheet[81][3]

ActualPerson = sheet[11][1]
BudgetPerson = sheet[11][3]

# Add up the values of MTO and Other Fresh
actual_freshtotal = float(ActualMTO) + float(ActualOTHERFRESH)
budget_freshtotal = float(BudgetMTO) + float(BudgetOTHERFRESH)

if (BudgetSales) < (ActualSales):
    print(f"Region HIT Inside Sales. Actual Total: ({ActualSales}) Budgeted Total: ({BudgetSales})")
elif (BudgetSales) > (ActualSales):
    print(f"Region MISSED Inside Sales. Budgeted Total: ({BudgetSales}) Actual Total: ({ActualSales})")
else:
    print(f"Region HIT Inside Sales. Actual Total({ActualSales}) Budgeted Total ({BudgetSales})")

if budget_freshtotal < actual_freshtotal:
    print(f"Region HIT Total Fresh Sales. Actual Total: ({actual_freshtotal}) Budgeted Total: ({budget_freshtotal})")
elif budget_freshtotal > actual_freshtotal:
    print(f"Region MISSED Total Fresh Sales. Budgeted Total: ({budget_freshtotal}) Actual Total: ({actual_freshtotal})")
else:
    print(f"Region HIT Total Fresh Sales. Actual Total: ({actual_freshtotal}) Budgeted Total: ({budget_freshtotal})")

#reverse the less/greater than for these

if (BudgetShrink) > (ActualShrink):
     print(f"Region HIT Shink %. Budgeted: ({BudgetShrink}) Actual: ({ActualShrink})")
elif (BudgetShrink) < (ActualShrink):
    print(f"Region MISSED Shink %. Budgeted: ({BudgetShrink}) Actual: ({ActualShrink})")
else:
    print(f"Region HIT Shink %. Budgeted: ({BudgetShrink}) Actual: ({ActualShrink})")

if (BudgetPerson) > (ActualPerson):
     print(f"Region HIT Personnel Costs. Actual: ({ActualPerson}) Budgeted: ({BudgetPerson})")
elif (BudgetPerson) < (ActualPerson):
    print(f"Region MISSED Personnel Costs. Actual: ({ActualPerson}) Budgeted: ({BudgetPerson})")
else:
    print(f"Region HIT Personnel Costs. Actual: ({ActualPerson}) Budgeted: ({BudgetPerson})")