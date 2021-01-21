import os
import re

# print(os.listdir())
for folder in os.listdir()[:]:
    if folder.startswith("ch"):
        print(folder)
        for fn in os.listdir(folder):
            print("\t"+fn)
            res = re.findall("(\d+)(-)(\d+)\s*(.*)", fn)
            if res:
                res = res[0]
                # print("{}{}{:0>2} {}".format(res[0],res[1],res[2],res[3]))
                new_fn = "{}{}{:0>2} {}".format(res[0],res[1],res[2],res[3])
                print("\t -> "+new_fn)
                os.rename(folder+"/"+fn, folder+"/"+new_fn)