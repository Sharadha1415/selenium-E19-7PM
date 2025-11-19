'''
To read excel files, we use xlrd

To install xlrd
    Go to command prompt    -->     pip install xlrd==1.2.0

    STEP1   :   import xlrd
    STEP2   :   open the excel file
    STEP3   :   open the worksheet
    STEP4   :   Convert the sheet object to the generator object

'''

import xlrd

## open the excel file
path = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\e19_info.xlsx'
workbook = xlrd.open_workbook(path)
# print(workbook)                 ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name('personal_data')
# print(worksheet)                ## Sheet object

## Convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)                     ## generator object

##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele)
#
# ## [text:'name', text:'place', text:'email_id', text:'phone_number']
# ## [text:'Lakshmi', text:'Hyderabad', text:'lakshmi@gmail.com', number:9080706050.0]
# ## [text:'Rekha', text:'Bengaluru', text:'rekha@gmail.com', number:9181716151.0]
# ## [text:'Bharathi', text:'Chennai', text:'bharathi@gmail,com', number:9282726252.0]
# ## [text:'Pavithra', text:'Mumbai', text:'pavithra@gmail.com', number:9383736353.0]


##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0], ele[1], ele[2], ele[3])
#
# ## text:'name' text:'place' text:'email_id' text:'phone_number'
# ## text:'Lakshmi' text:'Hyderabad' text:'lakshmi@gmail.com' number:9080706050.0
# ## text:'Rekha' text:'Bengaluru' text:'rekha@gmail.com' number:9181716151.0
# ## text:'Bharathi' text:'Chennai' text:'bharathi@gmail,com' number:9282726252.0
# ## text:'Pavithra' text:'Mumbai' text:'pavithra@gmail.com' number:9383736353.0

# ##---------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)
#
# ## name place email_id phone_number
# ## Lakshmi Hyderabad lakshmi@gmail.com 9080706050.0
# ## Rekha Bengaluru rekha@gmail.com 9181716151.0
# ## Bharathi Chennai bharathi@gmail,com 9282726252.0
# ## Pavithra Mumbai pavithra@gmail.com 9383736353.0


##---------------------------------------------------------------------------------------

# d = {}
#
# for ele in rows:
#     d[ele[0].value]= (ele[1].value, ele[2].value, ele[3].value)
#
# print(d['Rekha'])

header = next(rows)

for ele in rows:
    print(ele[0].value)



































