## Welcome to Pybind with xlwings

How to debug:

A) Checkout the code from git into for example C:\dev\xlwings\pybind

B) Start Visual Studio and open pybind.sln.<br/>
Build the example project using debug x86<br/>
Copy example.pyd and example.pdb to C:\dev\xlwings\pybind\excel<br/>

C) Start Pycharm and open the project in C:\dev\xlwings\pybind\excel

D) Start Excel and open the workbook C:\dev\xlwings\pybind\excel\sample.xlsm<br/>
Calulate the sheet by pressing F9 to see if it works.

E) set a breakpoint in pycharm<br/>
Press F9 in the XL sheet.<br/>
You should now hit the breakpoint<br/>
In Visual Studio attach to the python.exe process<br/>
Set a breakpoint in the C++ code.<br/>
Set one line in Pycharm and you should hit the breakpoint in Visual Studio.

You need to have the following software installed:<br/>
pycharm<br/>
anaconda 32 bit (which includes xlwings)<br/>
Excel 32 bit<br/>
Visual Studio 2017
