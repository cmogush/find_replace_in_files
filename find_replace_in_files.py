import os, re, shutil
from pathlib import Path

# setup
filetype = ".html"  # filetype to search for
exceptions = []
replacements = {
    r'http://vjs.zencdn.net/ie8/1.1.0/videojs-ie8.min.js': r'https://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js',
    r'http://vjs.zencdn.net/5.0.2/video.js': r'https://vjs.zencdn.net/7.8.2/video.js'}
# directory to check
dir = r'D:\Edison\MP4_JS_Update\Files'
# if moving the files, enter the destination dir, else set dest to dir
dest = r'D:\Edison\MP4_JS_Update\Update'
# backup directory
backup_dir = r'D:\Edison\MP4_JS_Update\Backup'
log = []

def replace_in_files(parent, dir):
    """makes replacements in all files in a directory, returns a list of all files updated"""
    full_path = os.path.join(parent, dir)
    for entry in os.listdir(full_path):
        entry_full_path = os.path.join(full_path, entry)
        if os.path.isdir(entry_full_path):
            replace_in_files(full_path, entry)
        elif filetype_matches(entry, filetype):
            if make_replacements(entry_full_path, replacements):
                log.append(str(entry_full_path))
        else:
            print("no filetype match | {}".format(entry))

def filetype_matches(file, filetype):
    """returns True if filetype matches"""
    f, e = os.path.splitext(file)
    if e == filetype:
        return True
    else:
        return False

def check_dir(file):
    """creates the directory if it doesn't exist"""
    dir_path = os.path.dirname(os.path.realpath(file))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

def make_replacements(file, replacements):
    """takes in a file and a dictionary of patterns : replacements to enact"""
    """returns True if replacements made, False if no change"""
    match = False
    # get content
    try:
        with open(file, 'r') as f:
            content = f.read()
        # check to see if patterns match
        for key in replacements:
            if re.search(str(key), content):
                match = True
                break
    except Exception as exc:
        print("{} generated an exception: {}".format(file, exc))
        exceptions.append("{} | {}".format(file, exc))
    # if a match found, make the replacements
    if match:
        # backup the file
        backup = do_replace(dir, backup_dir, file) # create the backup file
        check_dir(backup) # check the backup dir exists, if not make it
        with open(backup, 'w') as f: # write the backup file
            f.write(content)
        print("backing up {}".format(backup))
        # setup the updated output file
        outfile = do_replace(dir, dest, file) # create the output file
        check_dir(outfile) # check the outfile dir exists, if not make it
        with open(outfile, 'w') as f:  # make the replacements
            for key in replacements:
                content = re.sub(str(key), replacements[key], content)
            print("updated | {}".format(outfile))
            f.write(content)  # write the content
        return True
    print("no replacement | {}".format(file))
    return False

def do_replace(pattern, replacement, string):
    """helper function for move_files"""
    if string.startswith(pattern):
        return replacement + string[len(pattern):]

    return string

# def move_files(list, pattern, replacement):
#     """takes a list of files and moves them to another target location"""
#     dest_list = [] # list of destinations
#     # setup the new destination list
#     for entry in list:
#         dest = do_replace(pattern, replacement, entry)
#         dest_list.append(dest)
#     # make the moves
#     for file, dest in zip(list, dest_list):
#         new_path = shutil.copyfile(file, dest)
#         print(new_path)
#     return dest_list

def write_log(log, dir, outfile):
    with open(os.path.join(dir, outfile), 'w') as f:
        f.writelines('%s\n' % item for item in log)

def main():
    # print("Enter local directory to update ")
    # dir = Path(input("Input: "))
    # dir = r'D:\Edison\MP4 - JS Update\Backup'
    replace_in_files("", dir)
    write_log(log, dir, "change_log.txt")
    write_log(exceptions, dir, "exceptions.txt")
    write_log(log, dest, "change_log.txt")
    write_log(exceptions, dest, "exceptions.txt")
    print("writing result to {}".format(dir))
    print("writing result to {}".format(dest))
    #
    # # move the files
    # # dest = r'D:\Edison\MP4 - JS Update\Update'
    # moved_log = move_files(log, dir, dest)
    # write_log(moved_log, dest, "change_log_moved.txt")
    # write_log(moved_log, dir, "change_log_moved.txt")
    # print("writing result to {}".format(dest))

if __name__ == "__main__":
    main()