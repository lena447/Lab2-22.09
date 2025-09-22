#Double-Degree Array
def sum_of_neighbors_degrees():
    # Чтение входных данных
    with open('/Users/user/downloads/rosalind_ddeg-3.txt', 'r') as f:
        data = f.read().split()
    
    # Первые два числа: количество вершин и ребер
    n = int(data[0])
    m = int(data[1])
    
    # Построение списка смежности
    graph = [[] for _ in range(n + 1)]
    
    # Обработка ребер
    for i in range(2, 2 + 2 * m, 2):
        u = int(data[i])
        v = int(data[i + 1])
        graph[u].append(v)
        graph[v].append(u)
    
    # Вычисление степеней вершин
    degrees = [0] * (n + 1)
    for i in range(1, n + 1):
        degrees[i] = len(graph[i])
    
    # Вычисление суммы степеней соседей для каждой вершины
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        total = 0
        for neighbor in graph[i]:
            total += degrees[neighbor]
        result[i] = total
    
    # Формирование результата (вершины с 1 по n)
    return ' '.join(str(result[i]) for i in range(1, n + 1))

# Выполнение
print(sum_of_neighbors_degrees())