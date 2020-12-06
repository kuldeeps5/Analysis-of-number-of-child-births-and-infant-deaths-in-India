import pandas as pd
from os import walk

state= []
for (dirpath, dirnames, filenames) in walk("HMIS"):
    state.extend(dirnames)
    break;

print(state)
