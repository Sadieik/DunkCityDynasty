
# find duplicates
duplicated = []
filestrings = {}
for string1 in strings:
    dupmatch = 0
    for string2 in strings:
        if string1[3] == string2[3]:
            continue
        if string1[0] == string2[0]:
            if string1[2] != string2[2]:
                dupmatch = 1
            break
    if dupmatch == 1:
        dupmatch = 0
        for string2 in duplicated:
            if string1[0] == string2[0]:
                dupmatch = 1
                break
        if dupmatch == 0:
            duplicated.append(string1)
    else:
        dupmatch = 0
        if string1[2] in filestrings:
            for fs in filestrings[string1[2]]:
                if fs[0] == string1[0]:
                    dupmatch = 1
                    break
        else:
            filestrings[string1[2]] = []
        if dupmatch == 0:
            filestrings[string1[2]].append(string1)

print '\n\n\n\n\n'
print '/*\n * SHARED STRINGS\n */\n'

# output filewise
for key in filestrings.keys():
    print '/*\n * ' + key + '\n */\n'

    strings = filestrings[key]
    for string in strings:
        if string[1] == '':
            print '"' + string[0] + '" = "' + string[0] + '";'
            print
        else:
            print '/* ' + string[1] + ' */'
            print '"' + string[0] + '" = "' + string[0] + '";'
            print

# output duplicates
for string in duplicated:
    if string[1] == '':
        print '"' + string[0] + '" = "' + string[0] + '";'
        print
    else:
        print '/* ' + string[1] + ' */'
        print '"' + string[0] + '" = "' + string[0] + '";'
        print
