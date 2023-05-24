# parse_verilog.py

import argparse
import re
import csv
import os

# Define the command line arguments
parser = argparse.ArgumentParser(description='Parse and sort defines and plusargs from a all verilog flies in a directory/sundirs')
parser.add_argument('file', help='The Verilog file to parse')
args = parser.parse_args()

# Define the regex patterns for defines and plusargs

define_pattern = re.compile(r'(\+define)(\S*)')
plusarg_pattern = re.compile(r'(\s+\+)(\S*)')
netlist = re.compile(r'(S = )(\S*)')
snapshot = re.compile(r'(\-s\s)(\S*)')
rundir = re.compile(r'(log_dirname = )(\S*)')
regression = re.compile(r'(\-r\s)(\S*)')
config = re.compile(r'(\-x\s)(\S*)')

# Create empty lists to store the defines and plusargs
plusargs = []
defines = []
netlist = []
snapshot = []
rundir = []
regression = []
config = []

            
# Open the Verilog file and read its contents
with open(args.file, 'r') as sv_file:
    verilog = sv_file.read()

    # Loop through each line of the Verilog file
    for line in verilog.splitlines():
        
        # Match the plusarg pattern
        plusarg_match = plusarg_pattern.search(line)
        if plusarg_match:
            type = plusarg_match.group(1)
            name = plusarg_match.group(2)
            # Add the plusarg to the list as a tuple of (name, type, 'plusarg') 
            plusargs.append(('plusarg',name))
            
        # Match the ifdef/ifndef pattern  
        cmd_defines_match = define_pattern.search(line)
        if cmd_defines_match:
            name = cmd_defines_match.group(2)
            # Add the define to the list as a tuple of (name, type, 'ifdef/ifndef') 
            defines.append(('+defines',name))

print(plusargs)
print(defines)
