# Algoritmo: Bubble Sort
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort_steps(number_list):
    animation_frames = [number_list.copy()]
    n = len(number_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
                animation_frames.append(number_list.copy())
    return animation_frames

if __name__ == "__main__":
    total_elements = int(input("Tamaño de la lista (máx 100): "))
    frame_interval_ms = int(input("Intervalo entre cuadros (ms): "))

    # Genera una permutación aleatoria de 0..total_elements-1
    initial_values = random.sample(range(total_elements), total_elements)
    frames_sequence = bubble_sort_steps(initial_values)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(total_elements), frames_sequence[0])

    def update_bars(current_frame):
        for rect, height in zip(bar_rects, current_frame):
            rect.set_height(height)
        return bar_rects

    animation.FuncAnimation(
        fig,
        update_bars,
        frames=frames_sequence,
        interval=frame_interval_ms,
        repeat=False
    )
    plt.show()
