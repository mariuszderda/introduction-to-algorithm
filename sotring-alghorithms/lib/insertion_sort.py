def insertion_sort(numbers_list, debug=False):
    comparison_count = 0
    swap_count = 0
    for sort_border in range(1, len(numbers_list)):
        curr_idx = sort_border - 1
        value = numbers_list[curr_idx + 1]
        comparison_count += 1
        while numbers_list[curr_idx] > value and curr_idx >= 0:
            comparison_count += 1
            swap_count += 1
            numbers_list[curr_idx + 1] = numbers_list[curr_idx]
            curr_idx = curr_idx - 1
        numbers_list[curr_idx + 1] = value
        if debug:
            print(f'Border {sort_border} | List: {numbers_list}')
    return comparison_count, swap_count
