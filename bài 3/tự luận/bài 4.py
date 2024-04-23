def word_count(file_path):
    word_counts = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    
    return word_counts

# ví dụ
file_path = 'thực hành/P1_data.txt'
print(word_count(file_path))
