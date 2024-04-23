def count_words(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

file_path =  'thực hành/P1_data.txt'
assert count_words ( file_path ) ['success'] == 3

file_path = 'thực hành/P1_data.txt'
count_words ( file_path ) ['man']
print(count_words (file_path) ['man'])
# đáp án : câu c
