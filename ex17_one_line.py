# This is my 'one line' version of exercise 17
# I could make this truly one line using semicolons but that seems like cheating

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())
