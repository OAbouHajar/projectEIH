import argparse
import os
import pdb
import sys

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
listArg =  sys.argv[1:]
pdb.set_trace()

## send date to post file
if 'out' in listArg:
    print('out program')
if 'in' in listArg:
    print('in program')
