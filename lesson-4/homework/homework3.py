def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0

    while i < len(txt):
        result.append(txt[i])

        
        if (i + 1) % 3 == 0:
            result.append('_')

        
        if txt[i] in vowels or (result and result[-1] == '_'):
            if i + 1 < len(txt):
                result.append(txt[i + 1])
                result.append('_')
                i += 1 
        i += 1

    return ''.join(result)
txt = "abcdefghijklmno"
result = insert_underscores(txt)
print(result)