import sys
from statistics import mean


sys.path.append('lib')
sys. setrecursionlimit(30000)
# noinspection PyUnresolvedReferences
from insertion_sort import insertion_sort
from quick_sort import quick_sort
# noinspection PyUnresolvedReferences
from shell_sort import shell_sort
# noinspection PyUnresolvedReferences
from numbers_generator import random_list, descending_list


def show_sorting(sorting_type, list_type, elements_numbers):
    numbers_list = random_list(elements_numbers) if list_type == 1 else descending_list(elements_numbers)
    print(f"Utworzono listę: {numbers_list}")
    if sorting_type == 1:
        print("Wybrano algorytm INSERTION SORT")
        insertion_sort(numbers_list, True)
    elif sorting_type == 2:
        print("Wybrano algorytm SHELL SORT")
        shell_sort(numbers_list, True)
    elif sorting_type == 3:
        print("Wybrano algorytm QUICK SORT")
        end = len(numbers_list)
        quick_sort(numbers_list, 0, end - 1, True)
    elif sorting_type == 4:
        pass

def sorting_benchmark(numbers_count, list_type):
    quick_sort_score = []
    insertion_sort_score = []
    shell_sort_score = []

    for i in range(0, 10):
        numbers_array = random_list(numbers_count) if list_type == "random" else descending_list(numbers_count)

        quick_sort_array = numbers_array[:]
        insertion_sort_array = numbers_array[:]
        shell_sort_array = numbers_array[:]

        end = len(numbers_array)
        comparison_quick, swap_quick = quick_sort(quick_sort_array, 0, end - 1, comp=0, swap=0)
        comparison_insertion, swap_insertion = insertion_sort(insertion_sort_array)
        comparison_shell, swap_shell = shell_sort(shell_sort_array)

        quick_sort_score.append((comparison_quick, swap_quick))
        insertion_sort_score.append((comparison_insertion, swap_insertion))
        shell_sort_score.append((comparison_shell, swap_shell))

    comparison_mean_quick = mean(item[0] for item in quick_sort_score)
    swap_mean_quick = mean(item[1] for item in quick_sort_score)

    comparison_mean_insertion = mean(item[0] for item in insertion_sort_score)
    swap_mean_insertion = mean(item[1] for item in insertion_sort_score)

    comparison_mean_shell = mean(item[0] for item in shell_sort_score)
    swap_mean_shell = mean(item[1] for item in shell_sort_score)

    print(f"{"": <20}   {"QUICK": ^10} | {"INSERTION": ^10} | {"SHELL": ^10}")
    # print("{:20} - {:10.0f} {:10.0f} {:10.0f}".format("comparison mean ",comparison_mean_quick, comparison_mean_insertion, comparison_mean_shell))
    print(
        f"{"comparison mean": <20} - {comparison_mean_quick : ^10} | {comparison_mean_insertion: ^10} | {comparison_mean_shell : ^10}")
    print(f"{"swap mean": <20} - {swap_mean_quick : ^10} | {swap_mean_insertion: ^10} | {swap_mean_shell : ^10}")
    # print("{:20} - {:10.0f} {:10.0f} {:10.0f}".format("swap mean", swap_mean_quick, swap_mean_insertion, swap_mean_shell))

if __name__ == "__main__":
    print("-" * 10, "Jakie działanie wykonujemy?", "-" * 10)
    print("1 - Działanie algorytmów sortowania?")
    print("2 - Benchmark algorytmów sortowania?")
    first_action_choice = int(input("Co robimy?: "))

    sorting_type_number = 0
    if first_action_choice == 1:
        print("=" * 10, "Który typ sortowania chcesz sprawdzić?", "=" * 10)
        while sorting_type_number == 0:
            print('''
    1 - Insertion sort
    2 - Shell sort
    3 - Quick sort
    4 - Hybrid sort
            ''')
            sort_type_answer = input("Który wybierasz? Jeżeli chcesz zakończyć wciśnij \"Y\" ")
            if sort_type_answer.lower() == "y":
                break
            sort_type = int(sort_type_answer)
            count_of_elements = int(input("Z ilu elementów ma zostać wygenerowana lista? "))
            numbers_list_type = int(input('''
    Jak posortować tablicę?
        1 - liczby pseudolosowe
        2 - lista posortowana malejąco
            '''))
            show_sorting(sort_type, numbers_list_type, count_of_elements)

    elif first_action_choice == 2:
        print()
        print(" Wyniki dla tablicy n=100 ".center(80, "-"))
        print()
        print(" tablica wypełniona losowymi danymi ".center(80, " "))
        print()
        sorting_benchmark(100, "random")
        print()
        print(" tablica wypełniona liczbami posortowanymi malejąco danymi ".center(80, " "))
        print()
        sorting_benchmark(100, "desc")
        print()
        print()
        print(" Wyniki dla tablicy n=1000 ".center(80, "-"))
        print()
        print(" tablica wypełniona losowymi danymi ".center(80, " "))
        print()
        sorting_benchmark(1000, "random")
        print()
        print(" tablica wypełniona liczbami posortowanymi malejąco danymi ".center(80, " "))
        print()
        sorting_benchmark(1000, "desc")
        print()
        print()
        print(" Wyniki dla tablicy n=10000 ".center(80, "-"))
        print()
        print(" tablica wypełniona losowymi danymi ".center(80, " "))
        print()
        sorting_benchmark(10000, "random")
        print()
        print(" tablica wypełniona liczbami posortowanymi malejąco danymi ".center(80, " "))
        print()
        sorting_benchmark(10000, "desc")

    else:
        print("Zły wybór, uruchom ponownie program i wpisz odpowiednią liczbę!")