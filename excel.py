import xlswriter

workbook = xlsxwriter.workbook("output.xlsx")
worksheet =workbook.add_worksheet("firstsheet")