from .models import MDMDataDetails, TeachersDetails
import xlrd


def run():

    loc = "C:/Users/DELL/Downloads/mdmschools.xlsx"


    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(sheet.nrows - 1):
        MDMDataDetails(sn=sheet.cell_value(i+1, 0), dCode=sheet.cell_value(i+1, 1), schName=sheet.cell_value(i+1, 2),
                       devBlk=sheet.cell_value(i+1, 3), agencyName=sheet.cell_value(i+1, 4)).save()
    '''
    MDMDataDetails.object.all().delete()
    '''


def teach():
    locTeach = "C:/Users/DELL/Downloads/EducatiomStafkhandwa.xlsx"
    wbNew = xlrd.open_workbook(locTeach)
    sheetNew = wbNew.sheet_by_index(0)

    for i in range(sheetNew.nrows - 2):
        TeachersDetails(sn=sheetNew.cell_value(i+2, 0), schName=sheetNew.cell_value(i+2, 2), tName=sheetNew.cell_value(i+2, 5), desig=sheetNew.cell_value(i+2, 9)).save()