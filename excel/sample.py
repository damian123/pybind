import numpy as np
import pandas as pd
import xlwings as xw
import example


@xw.sub
def get_workbook_name():
    """Writes the name of the Workbook into Range("D3") of Sheet 1"""
    wb = xw.Book.caller()
    wb.sheets['Sheet1'].range('D3').value = wb.name


@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    #return 2 * (x + y)
    return example.add(x,y)



@xw.func
@xw.arg('data', ndim=2)
def add_one(data):
    """Adds 1 to every cell in Range"""
    return [[cell + 1 for cell in row] for row in data]


@xw.func
@xw.arg('x', np.array, ndim=2)
@xw.arg('y', np.array, ndim=2)
def matrix_mult(x, y):
    """Alternative implementation of Excel's MMULT, requires NumPy"""
    return x.dot(y)


@xw.func
@xw.arg('x', pd.DataFrame, index=False, header=False)
@xw.ret(index=False, header=False)
def CORREL2(x):
    """Like CORREL, but as array formula for more than 2 data sets"""
    return x.corr()

def main():
    # To run this with the debug server, set UDF_DEBUG_SERVER = True in the xlwings VBA module
    xw.serve()

if __name__ == '__main__':
    main()

