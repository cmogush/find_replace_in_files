import os
import re
from pathlib import Path

# def iterate(dir):
#     """iterate over the directory"""
#     for entry in os.listdir(dir):
#         currObj = os.path.join(dir, entry)
#
#         # get the filetype
#         if not os.path.isdir()
#         f, e = os.path.splitext(entry)
#
#         # directories, iterate
#         if os.path.isdir(currObj):
#             iterate(currObj, swfOnly, evenOdd)
#
#         # html, convert
#         elif e[1] == ".html":
#             convertHTML(currObj)
#             # print(entry+" : html")
#
#         # config, convert
#         elif entry == "config.xml":
#             convertConfig(currObj, swfOnly, evenOdd)
#             # print(entry+" : config")
#
#         else:
#             continue
#         evenOdd += 1

def filetype_matches(file, filetype):
    """returns True if filetype matches"""
    f, e = os.path.splitext(file)
    if e == filetype:
        return True
    else:
        return False

def make_replacements(file, replacements):
    """takes in a file and a dictionary of patterns : replacements to enact"""
    # get content
    with open(file, 'r') as f:
        content = f.read()
    # check to see if patterns match
    for key in replacements:
        if re.search(str(key), content):
            match = True
            break
    # if a match found, make the replacements
    if match:
        with open(file, 'w') as f:
            for key in replacements:
                content = re.sub(str(key), replacements[key], content)
            f.write(content)
            return True
    return False

def main():
    pattern = r""
    replacement = r""
    print("Enter local directory to update ")
    targetDir = Path(input("Input: "))
    # targetDir = Path(r"D:\Edison\n2k_ALL\SC\Biology N2K")
    parentDir = str(targetDir.parent)
    dir = str(os.path.basename(targetDir))


    iterate(targetDir)

if __name__ == "__main__":
    main()