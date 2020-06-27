import os, re, shutil
from pathlib import Path

filetype = ".html"
replacements = {
    r'http://vjs.zencdn.net/ie8/1.1.0/videojs-ie8.min.js': r'https://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js',
    r'http://vjs.zencdn.net/5.0.2/video.js': r'https://vjs.zencdn.net/7.8.2/video.js'}

def replace_in_files(parent, dir):
    """makes replacements in all files in a directory, returns a list of all files updated"""
    log = []
    full_path = os.path.join(parent, dir)
    for entry in os.listdir(full_path):
        entry_full_path = os.path.join(full_path, entry)
        if os.path.isdir(entry_full_path):
            replace_in_files(full_path, entry)
        elif filetype_matches(entry, filetype):
            if make_replacements(entry_full_path, replacements):
                log.append(entry_full_path)
    return log

def filetype_matches(file, filetype):
    """returns True if filetype matches"""
    f, e = os.path.splitext(file)
    if e == filetype:
        return True
    else:
        return False

def make_replacements(file, replacements):
    """takes in a file and a dictionary of patterns : replacements to enact"""
    """returns True if replacements made, False if no change"""
    match = False
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

def do_replace(pattern, replacement, string):
    """helper function for move_files"""
    if string.startswith(pattern):
        return replacement + string[len(pattern):]

    return string

def move_files(list, pattern, replacement):
    """takes a list of files and moves them to another target location"""
    dest_list = [] # list of destinations
    # setup the new destination list
    for entry in list:
        dest = do_replace(pattern,replacement,entry)
        dest_list.append(dest)
    # make the moves
    for file, dest in zip(list, dest_list):
        new_path = shutil.copyfile(file.strip(' \n'), dest)
        print(new_path)

def main():
    # print("Enter local directory to update ")
    # dir = Path(input("Input: "))
    dir = r'C:\Users\Chris\Desktop\Python Scripts\find_replace_in_files\big_test'
    log = replace_in_files("", dir)
    print(log)
    outfile = "change_log.txt"
    with open(os.path.join(dir, outfile), 'w') as f:
        f.writelines('%s\n' % item for item in log)
    print("writing result to {}\{}".format(dir, outfile))
    new_dest = r'C:\Users\Chris\Desktop\Python Scripts\find_replace_in_files\dest\big final_dest'
    move_files(log, dir, new_dest)
    outfile_moved = "change_log_moved.txt"
    with open(os.path.join(dir, outfile_moved), 'w') as f:
        f.writelines('%s\n' % item for item in log)
    print("writing result to {}\{}".format(dir, outfile_moved))
    with open(os.path.join(new_dest, outfile_moved), 'w') as f:
        f.writelines('%s\n' % item for item in log)
    print("writing result to {}\{}".format(new_dest, outfile_moved))

if __name__ == "__main__":
    main()