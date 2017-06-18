## Welcome to Pybind with xlwings

How to debug:

A) Checkout the code from git into for example C:\dev\xlwings\pybind

B) Start Visual Studio and open pybind.sln. 
Build the example project using debug x86
Copy example.pyd and example.pdb to C:\dev\xlwings\pybind\excel

C) Start Pycharm and open the project in C:\dev\xlwings\pybind\excel

D) Start Excel and open the workbook C:\dev\xlwings\pybind\excel\sample.xlsm
Calulate the sheet by pressing F9 to see if it works.

E) set a breakpoint in pycharm
Press F9 in the XL sheet.
You should now hit the breakpoint
In Visual Studio attach to the python.exe process
Set a breakpoint in the C++ code.
Set one line in Pycharm and you should hit the breakpoint in Visual Studio.

You need to have the following software installed:
pycharm
anaconda 32 bit (which includes xlwings)
Excel 32 bit
Visual Studio 2017
