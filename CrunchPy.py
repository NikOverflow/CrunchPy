# -*- coding: utf-8 -*-
import itertools, string, sys, re
from datetime import datetime

args = sys.argv
args.pop(0)
i = 0

def createWordlist(min, max, filename, characters = None):
    started = datetime.now()
    try:
        int(min)
        int(max)
        file = open(filename + ".txt","w")
        if characters != None:
            chars = characters
        else:
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        for i in range(int(min), int(max) + 1):
            for xs in itertools.product(chars, repeat=i):
                print(''.join(xs))
                file.write(''.join(xs) + "\n")
        file.close()
        print("Wordlist complete in " + str(datetime.now() - started))
        exit()
    except ValueError:
        print("Usage: python3 CrunchPy.py -create <Min amount> <Max amount> <Filename without .txt>")
        exit()

if __name__ == "__main__":
    chars = None
    while(i < len(args)):
        if args[i] == "-h":
            i += 1
            print("---Commands---")
            print("python3 CrunchPy.py -h | You can see the command list")
            print("python3 CrunchPy.py -create <Min length> <Max length> <Filename without .txt> | You can create a wordlist")
            print("---Commands---")
            exit()
        if args[i] == "-create":
            i += 1
            if(3 < len(args)):
                i += 3
                if i < len(args):
                    if args[i] == "-chars":
                        i += 1
                        if i < len(args):
                            chars = args[i]
                    if args[i] == "-pattern":
                        i += 1
                        if i < len(args):
                            if re.match("[" + args[i] + "]", "A"):
                                if chars != None:
                                    chars += string.ascii_uppercase
                                else:
                                    chars = string.ascii_uppercase
                            if re.match("[" + args[i] + "]", "a"):
                                if chars != None:
                                    chars += string.ascii_lowercase
                                else:
                                    chars = string.ascii_lowercase
                            if re.match("[" + args[i] + "]", "0"):
                                if chars != None:
                                    chars += string.digits
                                else:
                                    chars = string.digits
                            if re.match("[" + args[i] + "]", "."):
                                if chars != None:
                                    chars += string.punctuation
                                else:
                                    chars = string.punctuation
                    createWordlist(min = args[1], max = args[2], filename = args[3], characters = chars)
                else:
                    createWordlist(min = args[1], max = args[2], filename = args[3])
            else:
                print("Usage: python3 CrunchPy.py -create <Min length> <Max length> <Filename without .txt>")
                exit()
        i += 1