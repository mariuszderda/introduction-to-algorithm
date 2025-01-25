def shell_sort(numbers_list, debug = False):
    comparison_count = 0
    swap_count = 0
    h = 1
    while h < len(numbers_list) / 9:
                h = 3 * h + 1
    while h > 0:
        for i in range(h, len(numbers_list)):
            temp = numbers_list[i]
            j = i
            comparison_count += 1
            while j >= h and numbers_list[j-h] > temp:
                comparison_count += 1
                swap_count += 1
                numbers_list[j] = numbers_list[j-h]
                j =  j - h
            numbers_list[j] = temp
            if debug:
                print(f"Temp: {temp} | List: {numbers_list}")
        h //= 3
    return comparison_count, swap_count
