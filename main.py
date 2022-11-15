#!/usr/bin/env python3
import os
import glob
from subprocess import call

def list_files():
    listing = glob.glob('[2][0][1-2][0-9]\/*')
    
    return [each for each in listing if each.endswith('.py') and not 'init' in each and not 'test' in each]

def run_script(script):
    call(["python", script])

def main():
    files = list_files()
    print(files)
    for file in files:
        run_script(file)


if __name__ == '__main__':
    main()
