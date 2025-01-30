def get_common_chars(str1, str2) :
    
    set1 = set(str1)
    set2 = set(str2)
    
    common_chars = set1.intersection(set2)
    
    if common_chars:
        return ''.join(sorted(common_chars))
    else:
        return 'No common characters/没找到常见字符'
    
str1 = "Hello World"
str2 = "Meow"
common_chars = get_common_chars(str1, str2)
print("Common characters:", common_chars)    