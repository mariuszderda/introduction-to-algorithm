comparison_count = 0
swap_count = 0


def divide(numbers_list, start, end, debug=False):
    global comparison_count
    global swap_count
    border_value = numbers_list[end]
    i = start - 1

    for j in range(start, end):
        comparison_count += 1
        if numbers_list[j] <= border_value:
            i += 1
            swap_count += 1
            (numbers_list[i], numbers_list[j]) = (numbers_list[j], numbers_list[i])
        if debug:
            print(f"Pivot {border_value} | LIST | {numbers_list}")
    swap_count += 1
    (numbers_list[i + 1], numbers_list[end]) = (numbers_list[end], numbers_list[i + 1])
    return i + 1


def quick_sort(numbers_list, start, end, debug=False, **kwargs):
    global comparison_count
    global swap_count

    for k, v in kwargs.items():
        if k == "comp":
            comparison_count = v
        elif k == "swap":
            swap_count = v

    if start < end:
        border_index = divide(numbers_list, start, end, debug)
        quick_sort(numbers_list, start, border_index - 1, debug)
        quick_sort(numbers_list, border_index + 1, end, debug)

    return comparison_count, swap_count
