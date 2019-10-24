import xlsxwriter

outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

names = ["alwi", "yahya", "muljabar"]
values = [10,20,30]

#write headers
outSheet.write("A1","Nama")
outSheet.write("B1","Scores")

#write data to file
for item in range(len(names)):
    outSheet.write(item+1, 0, names[item])
    outSheet.write(item+1, 1, values[item])

outWorkbook.close()