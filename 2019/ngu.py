import os 

def read_file(day_num):
    dirname = os.path.dirname(__file__)
    filename = "input/day{}.txt".format(day_num)
    full_path = os.path.join(dirname, filename)
    with open(full_path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
