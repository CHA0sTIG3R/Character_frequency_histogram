from os import strerror

uin = input("Enter the file location: ")
try:
    src = open(uin, 'rt', errors='ignore')
except IOError as e:
    print("Cannot Open File: ", strerror(e.errno))
    exit(e.errno)

try:
    ln = src.read()
    aldict = {}
    for ch in ln:
        if ch.isalpha():
            ch = ch.lower()
            if ch in aldict:
                aldict[ch] += 1
            else:
                aldict[ch] = 1
    src.close()
    for key, val in aldict.items():
        print(key, " -> ", val) 
except Exception as e:
    print("Cannot Read File: ", e)
    exit(e)
