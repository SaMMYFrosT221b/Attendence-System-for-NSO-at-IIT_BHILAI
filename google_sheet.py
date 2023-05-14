import gspread

SERVICE_ACCOUNT = gspread.service_account(filename="attendence-system-386508-ddacdc70bb67.json")

SHEET = SERVICE_ACCOUNT.open("Attendence testing")

WORK_SHEET_1 = SHEET.worksheet("Sheet1")
WORK_SHEET_2 = SHEET.worksheet("Sheet2")

all_data_list = WORK_SHEET_2.get_all_values()

query = "123456"

for i in all_data_list:
    if(i[0]==query):
        print(i)



































# print(WORK_SHEET.acell('A2').value) # acell(cell address)
# print(WORK_SHEET.cell(3,4).value) # cell.(row,col)
# print(WORK_SHEET.get("A2:E4")) # return list of list where each element represent a row.
# print(WORK_SHEET.get_all_values()) # return all data in a list
# print(WORK_SHEET.get_all_records()) # return all data in a dictionary

# WORK_SHEET.update('A2',"Ratnakar Gautam") # update a cell
# WORK_SHEET.update('D2:E3',[["ADIL","Anant"],["Roushan","Shishir"]]) # update a range of cell.

# WORK_SHEET.update('A3',"=UPPER(A2)",raw=False) # use some formulas.

# WORK_SHEET.delete_rows(5) # delete a row

# print(WORK_SHEET.get_all_values())

# WORK_SHEET.update('A2:G2',[["12141360","Ratnakar Gautam","EE","Badminton","2","parkoursammyfrost@gmail.com",f"{time.ctime(time.time())}"]])


# print(WORK_SHEET.get_all_values())