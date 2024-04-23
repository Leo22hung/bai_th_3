from collections import deque

def max_in_sliding_window(num_list, size):
    if size <= 0 or size > len(num_list):
        return []

    result = []
    window = deque()

    for i in range(size):
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        window.append(i)

    result.append(num_list[window[0]])

    for i in range(size, len(num_list)):
        while window and window[0] <= i - size:
            window.popleft()

        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()

        window.append(i)
        result.append(num_list[window[0]])

    return result

# ví dụ
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
print(max_in_sliding_window(num_list, size))
