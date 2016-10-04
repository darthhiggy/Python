import re

with open("names.txt", encoding='utf-8') as open_file:
    data = open_file.read()

    #print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
    #print(re.findall(r'\b[trehous]{9}\b', data, re.I))
    #print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
    #print(re.findall(r'\b[trehous]{9}\b', data, re.I))
    #print(re.findall(r'''
    #    \b@[-\w\d.]* # First a word boundary, an @, and then any number of characters
    #    [^gov\t]+ # Ignore 1+ instances of the letters'g', 'o', or 'v' and a tab
    #    \b #match another work boundary
    #    ''', data, re.VERBOSE | re.I))
    # print(re.findall(r'''
    #    \b[-\w]+, # find a word boundary, 1+ hyphens or characters, and a comma
    #    \s # Find 1 whitespace
    #    [-\w ]+ # 1+ hypnes and characters and explicit spaces
    #    [^\t\n] # Ignore tabs a newlines
    #    ''', data, re.X))
    line = re.search(r'''
        ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first names
        (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
        (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
        (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and compnay
        (?P<twitter>@[\w\d]+)?$ # Twitter
        ''', data, re.X|re.M)

    print(line)
    print(line.groupdict())
