def find_max_sum_sub_array(k, arr):
    max_sum = float("-inf")
    current_sum = 0  

    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - (k - 1)]  # Mengurangi elemen pertama jendela dari jumlah saat ini

    return max_sum
    return 0

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8