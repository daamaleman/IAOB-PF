# Algoritmos: Búsqueda lineal y binaria
def linear_search(number_list, target_value):
    for position_index, current_value in enumerate(number_list):
        if current_value == target_value:
            return position_index
    return -1

def binary_search(sorted_list, target_value):
    lower_bound, upper_bound = 0, len(sorted_list) - 1
    while lower_bound <= upper_bound:
        middle_index = (lower_bound + upper_bound) // 2
        if sorted_list[middle_index] == target_value:
            return middle_index
        if sorted_list[middle_index] < target_value:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index - 1
    return -1

if __name__ == "__main__":
    raw_input_numbers = input("Lista de números: ")
    number_list = [int(value) for value in raw_input_numbers.split()]
    algorithm_option = input("Algoritmo (L=lineal, B=binario): ").upper()
    search_target = int(input("Número a buscar: "))

    if algorithm_option == "B":
        number_list.sort()
        found_index = binary_search(number_list, search_target)
    else:
        found_index = linear_search(number_list, search_target)

    if found_index != -1:
        print("Índice encontrado:", found_index)
    else:
        print("No encontrado")