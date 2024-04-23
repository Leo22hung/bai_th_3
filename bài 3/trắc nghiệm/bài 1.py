def max_in_window(num_list, k=3):
    if k <= 0 or k > len(num_list):
        raise ValueError("Invalid value of k")

    result = []
    window = []
    
    for i in range(len(num_list)):
        while window and window[0] < i - k + 1:
            window.pop(0)

        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(num_list[window[0]])

    return result

test = [3, 4, 5, 1, -44]
assert max_in_window(num_list=test, k=3) == [5, 5, 5]

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
print(max_in_window(num_list=num_list, k=3))
