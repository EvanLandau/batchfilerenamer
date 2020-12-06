import os
import argparse
import re

#Get CLI input
parser = argparse.ArgumentParser(description = 'Rename files that fit a regular expression in a folder.')
parser.add_argument('regex', metavar='RegEx', type = str, nargs=1, help="Regular expression for files to be renamed.")
parser.add_argument('out_name_base', metavar='Output', type = str, nargs=1, help="Output file name. Question marks ('?') will be replaced with the file number, or the file number will be appended to the name if none are found.")
parser.add_argument('-p', '--path', metavar='path', default = os.getcwd(), type = str, nargs = 1, help="Path to folder.")
args = parser.parse_args()

#Make list of files
file_list = [name for name in os.listdir(str(args.path)) if os.path.isfile(args.path + '\\' + name)]
#Remove elements that do not fit regex
file_list = [name for name in file_list if re.match(args.regex[0], name)]
if len(file_list) == 0:
    raise ValueError('No files matching regular expression ' + str(args.regex[0]) + ' found.')
extension = os.path.splitext(file_list[0])[1]
#Check if output has a ? in it
append = False if re.match('\?', args.out_name_base[0]) else True
#Rename files
counter = 0
for name in file_list:
    if append:
        os.rename(str(args.path) + '\\' + name, str(args.path) + '\\' + args.out_name_base[0] + str(counter) + extension)
    else:
        os.rename(str(args.path) + '\\' + name, str(args.path) + '\\' + re.sub("\?", str(counter), args.out_name_base[0] + extension))
    counter += 1