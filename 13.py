def romanToInt(s: str) -> int:
    list_s = list(s)
    value = 0
    i = 0
    while i < len(list_s):
        if list_s[i] == 'I':
            if i + 1 < len(list_s) and list_s[i + 1] == 'V':
                value += 4
                i += 2
                continue
            elif i + 1 < len(list_s) and list_s[i + 1] == 'X':
                value += 9
                i += 2
                continue
            else:
                value += 1
        elif list_s[i] == 'V':
            value += 5
        elif list_s[i] == 'X':
            if i + 1 < len(list_s) and list_s[i+1] == 'L':
                value += 40
                i += 2
                continue
            elif i + 1 < len(list_s) and list_s[i+1] == 'C':
                value += 90
                i += 2
                continue
            else:
                value += 10
        elif list_s[i] == 'L':
            value += 50
        elif list_s[i] == 'C':
            if i+1 < len(list_s) and list_s[i+1] == 'D':
                value += 400
                i += 2
                continue
            elif i+1 < len(list_s) and list_s[i+1] == 'M':
                value += 900
                i += 2
                continue
            else:
                value += 100
        elif list_s[i] == 'D':
            value += 500
        elif list_s[i] == 'M':
            value += 1000
        
        i += 1
        return value