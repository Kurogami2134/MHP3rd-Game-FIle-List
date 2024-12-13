from os import makedirs
from shutil import copy

with open("files.csv") as file:
    FILES = [x.replace("\n", "").split(",") for x in file.readlines() if x != '\n']

DIRS = set(["filetree/"+"/".join(x[1].split("/")[:-1]) for x in FILES])

for dir in DIRS:
    makedirs(dir, exist_ok=True)

for file in FILES:
    copy(f'DATA_BIN/{max(0, (int(file[0].split(".")[0])-1)//1000):0>2}/{file[0]}', "filetree/"+file[1])
