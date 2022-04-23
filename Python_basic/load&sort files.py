from natsort import natsorted
from glob import glob

file_list = glob('../sample_num/*')
file_list = natsorted(file_list)
for file in file_list:
    print(file)
