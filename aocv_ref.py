import sys
import re
import argparse

parser = argparse.ArgumentParser(description='To be pipelined with revsim(wiht -t), generates reference wavefrom vsim commands')
parser.add_argument('-l','--dir', action='store', help='change directory location')
parser.add_argument('-a','--ocvvsim', action='store_true', help='Print original revsim')
args = parser.parse_args()

ocvopt = re.compile(r'(\"\+define\+OCV_SDF\+OCV_SDF_DIR.*default\")')
log_dir = re.compile(r'\-l (.*dbg)')

for input_text in sys.stdin:
    if 'q' == input_text.rstrip():
        break
    opt_match = ocvopt.search(input_text)
    dir_match = log_dir.search(input_text)
    define_rm = opt_match.group(1)
    dbg_dir = dir_match.group(1)
    if args.dir :
        ref_dir = args.dir
        dbg_new_dir = ref_dir.replace("ref","dbg")
    else :      
        ref_dir = dbg_dir.replace("dbg","ref")
    aocvvsim = input_text.replace(dbg_dir,dbg_new_dir)
    if args.ocvvsim :
        print('#AOCV wavedump')
        print(aocvvsim)
    refvsim = input_text.replace(define_rm, "")
    refvsim = refvsim.replace(dbg_dir,ref_dir)
    print('#ref wavedump')
    print(refvsim)
    
print("#Done")
