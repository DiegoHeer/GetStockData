import xlwings as xw
import pandas as pd
import random

# Reference site for coding with python in vba
# https://towardsdatascience.com/how-to-supercharge-excel-with-python-726b0f8e22c2

# def main():
#     wb = xw.Book.caller()
#     df = pd.read_csv(r"C:\Users\diego\Desktop\aapl_income_statement_annual.csv")
#     df['total_length'] = df['2020-09-26_FY'] + df['2019-09-28_FY']
#     wb.sheets(0).range('A1').value = df

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    return line


def main():
    wb = xw.Book.caller()
    listloc = str(wb.sheets[0].range('B3').value)
    fhandle = open(listloc, encoding='utf-8')

    wb.sheets[0].range('A5').value = wb.sheets[0].range('B2').value + ' ' + wb.sheets[0].range(
        'B1').value + ' here is a joke for you'
    wb.sheets[0].range('A6').value = random_line(fhandle)


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("ISS.xlsm").set_mock_caller()
    main()
