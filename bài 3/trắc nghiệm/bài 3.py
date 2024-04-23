def count_chars(inp_str):
    # Khởi tạo dictionary để đếm số lần xuất hiện của mỗi ký tự
    char_count = {}
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in inp_str:
        # Kiểm tra nếu ký tự là chữ cái và đã xuất hiện trước đó trong từ điển
        if char.isalpha() and char in char_count:
            # Tăng số lần xuất hiện của ký tự
            char_count[char] += 1
        # Nếu ký tự là chữ cái và chưa xuất hiện trước đó trong từ điển
        elif char.isalpha():
            # Thêm ký tự vào từ điển và đặt số lần xuất hiện là 1
            char_count[char] = 1
    print(char_count)
    return char_count

# Test cases
test_string = 'Happiness'
assert count_chars(inp_str=test_string) == {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string = 'smiles'
count_chars(string)
# đáp án : câu a
