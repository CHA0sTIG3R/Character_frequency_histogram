from os import strerror

uin = input("Enter the file location: ") # file name
if '\\' in uin: 
    nsplit = uin.rsplit('\\', maxsplit=1) # splitting into a list and using \ to split make sure the list index is 2
    endstr = f"{nsplit[0]}/hist_{nsplit[1]}"  # concatenating the filename to make sure the new file created is in the same location as the original file
else:
    endstr = uin 
try:
    src = open(uin, 'rt', errors='ignore')
except IOError as e:
    print("Cannot Open File: ", strerror(e.errno))
    exit(e.errno)
try:
    sysin = open(endstr, 'wt')
except IOError as e:
    print("Cannot Create Destination File: ", strerror(e.errno))
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
    for key, val in sorted(aldict.items(), key = lambda kv: kv[1], reverse = True): # to sort the dictionary using values in reverse order.
        out = f"{key} -> {val}\n"
        sysin.write(out)
except Exception as e:
    print("Cannot Read File: ", e)
    exit(e)
src.close()
sysin.close()
