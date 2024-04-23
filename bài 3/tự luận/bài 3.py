def count_chars(string):
    char_count = {}
    for char in string:
        char = char.lower()
        if char.isalpha() and char in char_count:
            
            char_count[char] += 1
        
        elif char.isalpha():
            char_count[char] = 1
    
    return char_count

# ví dụ
string1 = 'Happiness'
print(count_chars(string1))

string2 = 'smiles'
print(count_chars(string2))