# This is a 'less annoying' and simplified version of ex17, per study drill 1

from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)
