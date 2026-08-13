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

En Simulated Annealing, cuando la temperatura es muy alta se tiene un nivel de exploración mayor. Esto significa que el algoritmo puede aceptar algunos estados que quizá sean peores, ya que la misma temperatura hace que la probabilidad de aceptarlos sea alta. De este modo, se exploran más opciones en el tablero y se evita que el programa se quede estancado en un mínimo local al principio.iento. 

### 5 ¿Qué ocurre si la temperatura disminuye demasiado rápido?

Si la temperatura baja demasiado rápido, pasamos directamente a la etapa de explotación. Como la temperatura ya estaría muy baja, no se tendría en cuenta la probabilidad de aceptar nuevos estados que sean peores. Básicamente, el algoritmo pierde la oportunidad de explorar bien el espacio y es muy probable que se quede atrapado en un mínimo local, terminando por funcionar igual que un Hill Climbing normal.

### 6 ¿Cómo cambiaría el tamaño del espacio de búsqueda para 8 reinas?

El espacio de búsqueda crecería muchísimo en tamaño. Para 4 reinas teníamos 256 estados posibles ($4^4$), pero para 8 reinas pasaríamos a tener más de 16 millones de opciones ($8^8$). Por este cambio tan grande, nos tocaría aumentar parámetros como la temperatura inicial y la cantidad de iteraciones, dado que al ser un espacio más amplio, necesitamos que los algoritmos hagan muchas más pruebas para poder obtener un buen resultado.

### 7 ¿Cuál de los tres algoritmos fue más confiable en los experimentos?

De los tres algoritmos, el más confiable fue el Random Restart según los resultados obtenidos en el punto 10:

Hill Climbing       : 34/100
Random Restart      : 100/100
Simulated Annealing : 98/100

El Random Restart es el más confiable porque, al tener varias oportunidades de reiniciar desde diferentes puntos, logra saltarse los estancamientos. De modo que esto asegura encontrar una solución, aunque el Simulated Annealing también demostró ser una opción muy buena casi logrando el 100.