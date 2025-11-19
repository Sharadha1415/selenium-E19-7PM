'''

*   Workbook()  --> creates a new excel workbook
*   .active     --> gets the current sheet

'''

from openpyxl import Workbook

## open the new excel workbook
excel_workbook = Workbook()

## initialize the worksheet
worksheet = excel_workbook.active

## set the title for the worksheet(optional)
worksheet.title = 'personal_data'

## Add the data to the excel
worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'email_id'
worksheet['D1'] = 'phone_number'

data_list = [
    ['Lakshmi', 'Hyderabad', 'lakshmi@gmail.com', 9080706050],
    ['Rekha', 'Bengaluru', 'rekha@gmail.com', 9181716151],
    ['Bharathi', 'Chennai', 'bharathi@gmail,com', 9282726252],
    ['Pavithra', 'Mumbai', 'pavithra@gmail.com', 9383736353]
]

for data in data_list:
    worksheet.append(data)

# excel_workbook.save('e19_data.xlsx')    ## The file will be stored in the same location as our python file

## To store the data in some other location
excel_workbook.save(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\e19_info.xlsx')















































