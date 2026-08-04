# Trabajo_Clase_IA

Comparación.

| Algoritmo | Tipo de Frontier | Prioridad | Estados explorados | Costo | ¿Óptimo? |
|--------------|---------|--------------------------|-----------|-------|----------|
| **DFS** | Pila | LIFO | 118 | 80 | No |
| **BFS** | Cola | FIFO | 106 | 28 | Sí |
| **UCS** | Cola de Prioridad | (g(n)) | 106 | 28 | Sí |
| **GBF** | Cola de prioridad | (h(n)) | 33 | 32 | No |
| **A*** | Cola de Prioridad | (g(n) + h(n)) | 59 | 28 | Sí |

¿Qué algoritmos garantizan el camino de menor número de aristas?
BFS garantiza el camino con menor número de pasos cuando todas las aristas cuestan lo mismo, como ocurre en `maze1`. **UCS** también lo garantiza aquí porque cada movimiento tiene costo 1.

¿Qué algoritmos garantizan el camino de menor costo?
UCS garantiza el camino de menor costo si los costos son no negativos. **A*** también lo garantiza cuando la heurística es admisible; en este laberinto devuelve el costo óptimo.

¿Por qué GBF puede encontrar un camino subóptimo?
Porque Greedy Best-First Search decide solo con h(n) y no toma en cuenta el costo acumulado g(n). Eso puede llevarlo a seguir una ruta que parece cercana a la meta, pero que termina siendo más cara que otra ruta mejor.

¿Qué ocurre con A* si (h(n)=0) para todos los nodos?
Si h(n)=0 para todos los nodos, **A*** se convierte en UCS, porque la prioridad queda solo en g(n). En el notebook de grafos equivaldría al algoritmo de costo uniforme.

¿Qué efecto tiene el orden de los vecinos en DFS y BFS?
El orden de neighbors() afecta mucho a DFS porque la pila expande primero el último vecino agregado. En **BFS** también cambia el orden de expansión entre nodos del mismo nivel, pero no cambia el hecho de que encuentra el camino con menos pasos.
