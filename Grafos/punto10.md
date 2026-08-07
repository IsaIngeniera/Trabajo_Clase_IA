# Trabajo_Clase_IA

Comparación.

| Algoritmo | Tipo de Frontier | Prioridad | Camino | Costo | Orden de expansión |
|--------------|---------|--------------------------|-----------|-----|-----|
| **DFS** | Pila | LIFO | A → C → E → H | 6 | A → C → E → H |
| **BFS** | Cola | FIFO | A → B → D → H | 5 | A → B → C → D → E → H |
| **UCS** | Cola de Prioridad | (g(n)) | A → B → E → H | 5 | A → C → B → E → D → H |
| **GBF** | Cola de prioridad | (h(n)) | A → C → E → H | 6 | A → C → E → H |
| **A*** | Cola de Prioridad | (g(n) + h(n)) | A → B → E → H | 5 | A → C → B → E → D → H |


¿Qué algoritmos garantizan el camino de menor número de aristas?
**BFS (Búsqueda en Anchura)**. Al expandir los nodos nivel por nivel, asegura encontrar siempre el camino con la menor cantidad de pasos (aristas) hacia el objetivo.

¿Qué algoritmos garantizan el camino de menor costo?
**UCS (Búsqueda de Costo Uniforme)** y **A*** (siempre y cuando la heurística utilizada sea admisible, es decir, nunca sobreestime el costo real).

¿Por qué GBF puede encontrar un camino subóptimo?
Porque GBF (Greedy Best-First Search) basa sus decisiones de expansión únicamente en la función heurística $h(n)$, que estima la distancia al objetivo, ignorando por completo el costo real acumulado $g(n)$. Esto puede llevarlo a elegir caminos que parecen estar más cerca del objetivo pero que tienen un alto costo en sus aristas.

¿Qué ocurre con A* si (h(n)=0) para todos los nodos?
La función de prioridad $f(n) = g(n) + h(n)$ se convierte simplemente en $f(n) = g(n)$. En este caso, el algoritmo A* se comporta exactamente igual que la **Búsqueda de Costo Uniforme (UCS)**.

¿Qué efecto tiene el orden de los vecinos en DFS y BFS?
En **DFS**, el orden en que se agregan los vecinos a la pila determina la rama del grafo que se explorará en profundidad primero, lo que puede cambiar drásticamente el camino encontrado y el orden de expansión.
En **BFS**, todos los nodos a un mismo nivel de profundidad serán visitados antes de pasar al siguiente nivel, por lo que el orden no impide encontrar el camino más corto en aristas. Sin embargo, el orden afectará qué nodo dentro del mismo nivel es explorado primero, lo cual determinará cuál camino se escoge en caso de haber múltiples caminos con la misma cantidad de aristas.
