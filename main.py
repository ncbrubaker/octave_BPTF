# This is a sample Python script.
# import oct2py
# oc = oct2py.Oct2Py()
# x = oc.zeros(3,3)
# print(x, x.dtype)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# octave.addpath(octave.genpath('C:/Users/Nolan Brubaker/Desktop/Repositories/export_bptf'))
# octave.run('demo.m')

from oct2py import Oct2Py
oc = Oct2Py()

oc.compute(2, 5)

# octave.addpath('C:/Users/Nolan Brubaker/PycharmProjects/octave_BPTF') # doctest: +SKIP
# octave.run('add.m') # doctest: +SKIP


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
