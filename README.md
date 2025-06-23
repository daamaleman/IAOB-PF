# Algoritmos de Ordenamiento y Búsqueda 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Activo-brightgreen)

Este repositorio implementa y analiza algoritmos de ordenamiento (**Bubble Sort**, **Quick Sort**) y búsqueda (**Lineal**, **Binaria**) en Python 🐍, basado en el documento *"Implementación de Algoritmos de Ordenamiento y Búsqueda"* (18 de Junio de 2025). Incluye scripts para medir rendimiento 📊, visualizar procesos 🎥 y recomendar algoritmos 🤔.

---

## 📋 Contenido

### 1. `benchmark_sorting_basic.py` ⏱️
Compara tiempos de ejecución de Bubble Sort y Quick Sort para listas de 100, 1000 y 10000 elementos.

- **Uso**:
  ```bash
  python benchmark_sorting_basic.py
  ```
- **Entrada**: Tamaños de lista (ej. `100 1000`) y número de pruebas.
- **Salida**: Tiempo promedio en segundos 🕒.
- **Ejemplo**:
  ```plaintext
  Tamaños de lista: 100 1000
  Número de pruebas: 5
  == Bubble Sort ==
  100 elem → media 0.00234 s
  1000 elem → media 0.14567 s
  == Quick Sort ==
  100 elem → media 0.00112 s
  1000 elem → media 0.01045 s
  ```

### 2. `bubble_animation_basic.py` 🎬
Visualiza Bubble Sort con una animación de barras usando Matplotlib 📈.

- **Uso**:
  ```bash
  python bubble_animation_basic.py
  ```
- **Entrada**: Tamaño de lista (máx. 100) e intervalo (ms).
- **Salida**: Animación gráfica 🎞️.
- **Dependencia**: `matplotlib`
- **Ejemplo**:
  ```plaintext
  Tamaño de la lista: 20
  Intervalo entre cuadros (ms): 100
  ```

### 3. `search_cli_basic.py` 🔍
Ejecuta Búsqueda Lineal o Binaria en una lista de números.

- **Uso**:
  ```bash
  python search_cli_basic.py
  ```
- **Entrada**: Lista, algoritmo (L/B) y número a buscar.
- **Salida**: Índice o "No encontrado" 🚫.
- **Ejemplo**:
  ```plaintext
  Lista de números: 5 2 8 1 9
  Algoritmo (L=lineal, B=binario): B
  Número a buscar: 8
  Índice encontrado: 3
  ```

### 4. `memory_profiler_basic.py` 💾
Mide el pico de memoria de Bubble Sort y Quick Sort.

- **Uso**:
  ```bash
  python memory_profiler_basic.py
  ```
- **Entrada**: Tamaño de lista y algoritmo (B/Q).
- **Salida**: Memoria en KiB 📏.
- **Dependencia**: `tracemalloc`
- **Ejemplo**:
  ```plaintext
  Tamaño de lista: 1000
  Algoritmo (B=bubble, Q=quick): Q
  Pico de memoria: 128.5 KiB
  ```

### 5. `algorithm_recommender_basic.py` 🧠
Recomienda Bubble Sort (≤100 elementos), Quick Sort (>10000) o Búsqueda Binaria (lista ordenada).

- **Uso**:
  ```bash
  python algorithm_recommender_basic.py
  ```
- **Entrada**: Número de elementos y si está ordenada (s/n).
- **Salida**: Algoritmo recomendado ✅.
- **Ejemplo**:
  ```plaintext
  Número de elementos: 50
  ¿Lista ordenada? (s/n): n
  Algoritmo recomendado: Bubble Sort
  ```

---

## 🛠️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/daamaleman/IAOB-PF.git
   ```
2. **Instala dependencias**:
   ```bash
   pip install matplotlib
   ```

---

## ⚙️ Requisitos

- **Python**: 3.x 🐍
- **Bibliotecas**:
  - `matplotlib` (para animaciones) 📊
  - `tracemalloc` (incluido en Python estándar)

---

## 📝 Conclusiones

Basado en el análisis del documento:
- **Bubble Sort**: Simple, ideal para listas pequeñas, pero lento para datos grandes (O(n²)) 😴.
- **Quick Sort**: Eficiente en promedio (O(n log n)), sensible al peor caso ⚡.
- **Búsqueda Lineal**: Fácil, pero ineficiente para listas grandes (O(n)) 🐢.
- **Búsqueda Binaria**: Rápida en listas ordenadas (O(log n)) 🏎️.

Estos scripts permiten validar estas conclusiones mediante pruebas empíricas y visualizaciones interactivas.

---

## 📄 Licencia

[MIT License](LICENSE) - Siéntete libre de usar, modificar y compartir este proyecto.

---

## 🌟 Contribuciones

¡Las contribuciones son bienvenidas! 🙌 Abre un *issue* o envía un *pull request* para mejorar el código o añadir funcionalidades.