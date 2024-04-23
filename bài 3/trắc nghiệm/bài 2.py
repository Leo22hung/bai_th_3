def intersection(lst1, lst2):
    # Tạo một set từ danh sách lst1 và lst2
    set1 = set(lst1)
    set2 = set(lst2)
    
    # Tìm các phần tử chung bằng phép giao của hai set
    common_elements = set1.intersection(set2)
    
    # Chuyển kết quả từ set sang list và sắp xếp lại danh sách
    result = sorted(list(common_elements))
    
    # In ra kết quả dưới dạng [4, 9]
    print(result)
    return result

# Test cases
test_list1 = [4, 9]
test_list2 = [9, 2]
assert intersection(lst1=test_list1, lst2=test_list2) == [9]

num_list1 = [4, 9, 5]
num_list2 = [9, 4, 9, 8, 4]
intersection(num_list1, num_list2)
# đáp án : câu b