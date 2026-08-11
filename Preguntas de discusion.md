# PREGUNTAS DE DISCUSIÓN

### 1 ¿Por qué Hill Climbing puede fallar aunque exista una solución?

Falla porque no tiene visión global ni memoria. Si llega a un estado en el tablero donde mover cualquier reina resulta en un costo igual o peor, el algoritmo se detiene automáticamente. Si ese estado de detención tiene un costo mayor a cero, significa que el algoritmo quedó "atrapado" y falló en encontrar la solución real, ya que es incapaz de hacer un movimiento que empeore el costo temporalmente para salir de ahí.

### 2 ¿Qué diferencia existe entre una meseta y un mínimo local?

La diferencia radica en su estructura tridimensional (evaluando costo vs. estados): 

**Mínimo local:** Es un estado donde todos los vecinos tienen un costo estrictamente mayor (peor) que el estado actual. Es como estar en el fondo de un pozo que no es el más profundo; cualquier paso que des te obliga a subir.

**Meseta:** Es un área donde el estado actual y sus vecinos tienen exactamente el mismo costo. Es como estar en una llanura plana; el algoritmo se detiene (o vaga sin rumbo) porque no tiene una "pendiente" que le indique en qué dirección está la mejora.

### 3 ¿Por qué Random Restart mejora la probabilidad de encontrar una solución?

Aumenta la probabilidad de encontrar una solución porque, al reiniciar el algoritmo desde una posición aleatoria diferente, se "rompe" el estado de estancamiento. Esto obliga al algoritmo a explorar diferentes regiones del espacio de búsqueda. A mayor número de reinicios, mayor es la probabilidad estadística de que al menos uno de esos estados iniciales aleatorios caiga en una ruta directa hacia la solución global (costo 0).

### 4 ¿Qué ocurre en Simulated Annealing cuando la temperatura es muy alta?

### 5 ¿Qué ocurre si la temperatura disminuye demasiado rápido?
### 6 ¿Cómo cambiaría el tamaño del espacio de búsqueda para 8 reinas?
### 7 ¿Cuál de los tres algoritmos fue más confiable en los experimentos?