'@author Exequiel Sepulveda https://github.com/exepulveda'
import csv
import argparse
import sys
import io

from pandas import DataFrame

def parse_input(input):
    if isinstance(input, io.TextIOBase):
        fd_gslib = stdin
    elif isinstance(input, str):
        fd_gslib = open(input)
    else:
        raise ValueError("The input is not a valid stream of filename")

    reader = csv.reader(fd_gslib, delimiter=' ', skipinitialspace=True) # GSLIB uses space as delimiter
    
    # read file title
    title = next(reader)
    # read number of variables
    row = next(reader)
    nvars = int(row[0])
    # read name of variables
    var_names = []
    for i in range(nvars):
        row = next(reader)
        name = '_'.join(row) # trick to join each separated text with _
        var_names += [name.strip()]

    
    #read values
    rows = []
    for row in reader:
        rows += [row[:n_cols]]

    return title, var_names, rows

def load_input_numpy(input):
    title, var_names, rows = parse_input(input)

    return title, var_names, np.array(rows)

def load_input_df(input):
    title, var_names, rows = parse_input(input)

    return title, DataFrame(var_names, np.array(rows))