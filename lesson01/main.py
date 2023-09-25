def sort_numbers_desc_imp(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

def sort_numbers_desc_decl(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers


numbers = [4, 2, 7, 1, 9]
# импративный стиль
sort_numbers_desc_imp(numbers)
print(numbers)
# декларативный стиль
sort_numbers_desc_decl(numbers)
print(numbers)


