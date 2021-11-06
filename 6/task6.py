#! /usr/bin/python3

import argparse
import json
import os

from collections import defaultdict

storage_file = "storage.data"

#print("--------Task6--------")
parser = argparse.ArgumentParser(description='Key-value storage.')
parser.add_argument('-k', '--key', type = str, help = 'print the values corresponding to the key')
parser.add_argument('-v', '--val', type = str, help = 'value to save in storage')
args = parser.parse_args()

if args.key != None and args.val == None:
    read_file = open(storage_file,"r")

    try:
        data = json.load(read_file)
    except ValueError:
        print("Bad JSON file. Try another one.")
        exit(1)

    if args.key in data:
        print(*data[args.key], sep = ', ' )
    else:
        print(None)
    read_file.close();
if args.key != None and args.val != None:
    write_file = open(storage_file, "a+")
    if os.path.getsize(storage_file) == 0:
        data = defaultdict(list)
        data[args.key].append(args.val)
        json.dump(data, write_file)
    else:
        write_file.seek(0)

        try:
            data = json.load(write_file)
        except ValueError:
            print("Bad JSON file. Try another one.")

        if args.key in data:
            data[args.key].append(args.val)
        else:
            data[args.key] = list()
            data[args.key].append(args.val)
        write_file.close()
        write_file = open(storage_file, "w")
        json.dump(data, write_file)
    write_file.close()
