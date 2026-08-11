# Explicación de las actividades 1 y 2

## Actividad 1: Selección por ruleta

La selección por ruleta es una forma de elegir individuos de una población de acuerdo con su capacidad de adaptación, medida por el fitness.

### 1. ¿Qué hace la función `roulette_selection`?
Esta función toma una población y elige un individuo probabilísticamente.

- Primero calcula el fitness de cada individuo.
- Luego suma todos los valores de fitness para obtener el fitness total.
- Con ese total, genera un valor aleatorio llamado `spin`.
- Recorre la población acumulando fitness hasta encontrar el individuo que corresponde a ese valor aleatorio.

### 2. ¿Por qué se usa?
Porque permite que los individuos con mejor fitness tengan más probabilidad de ser elegidos, pero sin eliminar por completo a los demás.

### 3. ¿Qué pasa si todos tienen fitness cero?
En ese caso, no existe una ventaja clara para ningún individuo. Por eso la función devuelve un elemento aleatorio de la población.

### 4. Ejemplo de lógica
Si un individuo tiene un fitness alto, ocupa una mayor porción de la "ruleta" y, por lo tanto, tiene más posibilidades de ser seleccionado.



## Actividad 2: Cruce uniforme

El cruce uniforme es una técnica para combinar dos padres y generar dos hijos.

### 1. ¿Qué hace la función `uniform_crossover`?
Esta función recibe dos padres y genera dos hijos.

- Si la probabilidad de cruce no se cumple, los hijos son copias exactas de los padres.
- Si el cruce sí ocurre, cada posición del cromosoma se decide aleatoriamente:
  - con un 50% de probabilidad, el hijo toma el gen del padre 1;
  - con el otro 50%, toma el gen del padre 2.

### 2. ¿Por qué es útil?
Porque mezcla información de ambos padres de una manera más dispersa que el cruce de un punto.
Esto ayuda a explorar más soluciones posibles durante la evolución.

### 3. ¿Qué representa cada hijo?
Cada hijo conserva partes de ambos padres, lo que permite que la población genere nuevas combinaciones y no se limite a copiar simplemente una estructura fija.



## Relación con los algoritmos genéticos

Estas dos actividades son partes fundamentales del algoritmo genético:

- La selección por ruleta decide quiénes participan en la reproducción.
- El cruce uniforme combina la información genética de esos individuos para crear nuevas soluciones.

En conjunto, permiten que el algoritmo evolucione hacia mejores soluciones, mezclando exploración y explotación.


