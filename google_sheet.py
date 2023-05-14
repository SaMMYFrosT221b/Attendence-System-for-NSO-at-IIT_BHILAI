import gspread
import time
import os
os.system('cls')

SERVICE_ACCOUNT = gspread.service_account(filename="attendence-system-386508-ddacdc70bb67.json")

SHEET = SERVICE_ACCOUNT.open("Attendence testing")

WORK_SHEET_1 = SHEET.worksheet("Sheet1")
WORK_SHEET_2 = SHEET.worksheet("ID")

# Number of Row filled
row_filled = len(WORK_SHEET_1.get_all_values())

# Roll number to find
# query = "12240120"

# Finding the Roll number
# cell = WORK_SHEET_2.find(query)

# Accessing the Row number from the cell
# roll_number_row = str(cell)[7:9]

# Accessing the details of the student from that row
# student_details = WORK_SHEET_2.get(f"A{roll_number_row}:F{roll_number_row}")[0]
# print(student_details[1])

# Adding the current time
# student_details.append(f"{time.ctime(time.time())}")

# Marking the attendece in sheet1
# WORK_SHEET_1.update(f"A{row_filled+1}:G{row_filled+1}",[student_details])

def hello(query1):
        
    # Finding the Roll number
    cell1 = WORK_SHEET_2.find(query1)

    # Accessing the Row number from the cell
    roll_number_row1 = str(cell1)[7:9]

    # Accessing the details of the student from that row
    student_details1 = WORK_SHEET_2.get(f"A{roll_number_row1}:F{roll_number_row1}")[0]

    # Adding the current time
    student_details1.append(f"{time.ctime(time.time())}")

    # Marking the attendece in sheet1
    WORK_SHEET_1.update(f"A{row_filled+1}:G{row_filled+1}",[student_details1])

    return student_details1[1]