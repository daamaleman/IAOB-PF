# Benchmark de Algoritmos de Ordenamiento
# Compara el rendimiento de Bubble Sort, Quick Sort y Merge Sort

import random
import time
import statistics

def bubble_sort(number_list):
    """
    Bubble Sort - Algoritmo simple pero ineficiente
    Complejidad: O(n²) en el peor caso
    """
    # Crear copia para no modificar la lista original
    sorted_list = number_list.copy()
    list_length = len(sorted_list)
    
    for outer_index in range(list_length):
        swapped = False  # Optimización: detectar si ya está ordenado
        
        for inner_index in range(0, list_length - outer_index - 1):
            # Comparar elementos adyacentes e intercambiar si es necesario
            if sorted_list[inner_index] > sorted_list[inner_index + 1]:
                sorted_list[inner_index], sorted_list[inner_index + 1] = (
                    sorted_list[inner_index + 1], sorted_list[inner_index]
                )
                swapped = True
        
        # Si no se hizo ningún intercambio, la lista ya está ordenada
        if not swapped:
            break
    
    return sorted_list

def quick_sort(number_list):
    """
    Quick Sort - Algoritmo eficiente usando divide y conquista
    Complejidad: O(n log n) promedio, O(n²) en el peor caso
    """
    if len(number_list) <= 1:
        return number_list
    
    # Elegir pivote (primer elemento)
    pivot = number_list[0]
    
    # Dividir en sublistas: menores, iguales y mayores al pivote
    lower_partition = [x for x in number_list[1:] if x < pivot]
    equal_partition = [x for x in number_list if x == pivot]
    higher_partition = [x for x in number_list[1:] if x > pivot]
    
    # Recursivamente ordenar y combinar
    return quick_sort(lower_partition) + equal_partition + quick_sort(higher_partition)

def merge_sort(number_list):
    """
    Merge Sort - Algoritmo estable y eficiente
    Complejidad: O(n log n) en todos los casos
    """
    if len(number_list) <= 1:
        return number_list
    
    # Dividir la lista en dos mitades
    mid = len(number_list) // 2
    left = merge_sort(number_list[:mid])
    right = merge_sort(number_list[mid:])
    
    # Combinar las dos mitades ordenadas
    return merge(left, right)

def merge(left, right):
    """
    Función auxiliar para combinar dos listas ordenadas
    """
    result = []
    i = j = 0
    
    # Comparar elementos de ambas listas y agregar el menor
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agregar elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_data(size, data_type="random"):
    """
    Genera datos de prueba de diferentes tipos
    """
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, size) for _ in range(size)]

def run_single_test(sort_function, list_size, data_type="random"):
    """
    Ejecuta una sola prueba de benchmark
    Retorna el tiempo de ejecución en segundos
    """
    # Generar datos de prueba
    test_data = generate_data(list_size, data_type)
    
    # Medir tiempo de ejecución
    start_time = time.perf_counter()
    result = sort_function(test_data)
    end_time = time.perf_counter()
    
    # Verificar que el resultado esté ordenado correctamente
    if result != sorted(test_data):
        raise ValueError(f"Error en {sort_function.__name__}")
    
    return end_time - start_time

def run_benchmark(list_sizes, repetitions):
    """
    Ejecuta el benchmark completo para todos los algoritmos
    """
    # Definir los algoritmos a probar
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort
    }
    
    # Probar cada algoritmo
    for name, algorithm in algorithms.items():
        print(f"\n== {name} ==")
        
        for size in list_sizes:
            # Ejecutar múltiples pruebas y calcular estadísticas
            times = []
            for _ in range(repetitions):
                execution_time = run_single_test(algorithm, size)
                times.append(execution_time)
            
            # Calcular estadísticas
            average_time = statistics.mean(times)
            min_time = min(times)
            max_time = max(times)
            
            # Mostrar resultados
            print(f"{size:>6} elementos → "
                  f"promedio: {average_time:.6f}s "
                  f"(min: {min_time:.6f}s, max: {max_time:.6f}s)")

def main():
    """
    Función principal del programa
    """
    print("=== BENCHMARK DE ALGORITMOS DE ORDENAMIENTO ===")
    
    # Obtener parámetros del usuario
    try:
        # Tamaños de lista a probar
        user_input = input("Tamaños de lista (ej. 100 1000 10000): ").strip()
        if not user_input:
            list_sizes = [100, 1000, 10000]  # Valores por defecto
        else:
            list_sizes = [int(x) for x in user_input.split()]
        
        # Número de repeticiones por prueba
        repetitions = int(input("Número de pruebas por tamaño (default: 5): ") or "5")
        
    except ValueError:
        print("Error: Ingresa números válidos")
        return
    except KeyboardInterrupt:
        print("\nOperación cancelada")
        return
    
    # Ejecutar benchmark
    print(f"\nEjecutando {repetitions} pruebas para cada tamaño...")
    run_benchmark(list_sizes, repetitions)
    
    print("\n=== FIN DEL BENCHMARK ===")

if __name__ == "__main__":
    main()
