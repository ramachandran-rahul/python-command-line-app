#!/bin/python3

import sys
import re
import os

def validateArgument(option):
    validationOption = r'^\-(a|s|c|v)$'
    validArg1 = re.search(validationOption, option)
    if(not validArg1):
        print("Error: Please pass valid option: -a, -c, -s, -v")
        exit(-1)
    elif(len(sys.argv)>4):
        print("Error: Too many arguments.")
        exit(-1)
    return (validArg1)

def readArgFile(readList):
    try:
        readList = []
        fileParse = open(fName,'r')
        for line in fileParse:
            line = line.rstrip()
            name, code, isoSet = re.split(r'\s+',line)
            newItem = {'name':name,'code':code,'isoSet':isoSet}
            readList.append(newItem)
        return readList
    except FileNotFoundError:
        print(f"Error: {fName} does not exist.")
        exit(-1)
    except PermissionError:
        print(f"Error: {fName} is not readable.")
        exit(-1)
    except IsADirectoryError:
        print(f"Error: {fName} is a directory, not a file.")
        exit(-1)

def isFileEmpty():
    try:
        if(os.path.getsize(fName) <= 1):
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"Error: {fName} does not exist.")
        exit(-1)
    except PermissionError:
        print(f"Error: {fName} is not readable.")
        exit(-1)
    except IsADirectoryError:
        print(f"Error: {fName} is a directory, not a file.")
        exit(-1)

def optionA():
    if(len(sys.argv)==3):
        languageList = []
        if(fileEmpty):
            print('No languages in this file')
            exit(-1)
        else:
            for item in fileContent:
                languageList.append(item['name'])
            if(languageList):
                print('Languages in this file:')
                for sortItems in sorted(languageList):
                    print(sortItems)
    else:
        print("Error: Too many arguments. \nFollow format: ./languages.py -a argument_file")

def optionC():
    if(len(sys.argv)==4):
        matchList=[]
        if(len(sys.argv[2])>2):
            print(f"Code {sys.argv[2]} not present in this file")
            print("Error: Code should have only two characters")
        elif(fileEmpty):
            print(f"Code {sys.argv[2]} not present in this file")
            exit(-1)
        else:
            for item in fileContent:
                if(item['code']==sys.argv[2]):
                    matchList.append(item['name'])
            if(matchList):
                for foundItem in matchList:
                    print(foundItem)
            else:
                print(f"Code {sys.argv[2]} not present in this file")
    elif(len(sys.argv)>4):
        print("Error: Too many arguments. \nFollow format: ./languages.py -c code argument_file")
    else:
        print("Error: Not enough arguments. \nFollow format: ./languages.py -c code argument_file")

def optionS():
    if(len(sys.argv)==4):
        matchList=[]
        if(fileEmpty):
            print(f"Character set {sys.argv[2]} not present in this file")
            exit(-1)
        else:
            for item in fileContent:
                if(item['isoSet']==sys.argv[2]):
                    matchList.append(item['name'])
            if(matchList):
                for foundItem in matchList:
                    print(foundItem)
            else:
                print(f"Character set {sys.argv[2]} not present in this file")
    elif(len(sys.argv)>4):
        print("Error: Too many arguments. \nFollow format: ./languages.py -s set argument_file")
    else:
        print("Error: Not enough arguments. \nFollow format: ./languages.py -s set argument_file")

def optionV():
    if(len(sys.argv)==3):
        print("First Name: Rahul\nSurname: Ramachandran\nStudent ID: 24910212\nDate of Submission: 03/11/2023")
        print("Assignment is submitted by Rahul Ramachandran(24910212) on 3rd November 2023")
    elif(len(sys.argv)>3):
        print("Error: Too many arguments. \nFollow format: ./languages.py -v argument_file")


#Main Code

if(len(sys.argv)>=3):
    opt = sys.argv[1]
    fName = sys.argv[len(sys.argv)-1]
    fileContent = []
    validArguments = validateArgument(opt)
    if(validArguments):
        fileEmpty = isFileEmpty()
        if(not fileEmpty):
            fileContent = readArgFile(fileContent)
        match opt:
            case '-a': optionA()
            case '-c': optionC()
            case '-s': optionS()
            case '-v': optionV()
else:
    print("Error: Not enough arguments. \nFollow format: ./languages.py option argument_file")
