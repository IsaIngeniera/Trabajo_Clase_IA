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


## Actividad 3

Para evolucionar una **frase objetivo** en lugar de una cadena binaria, cambiamos tres piezas del algoritmo, dejando intacta la lógica general (selección, cruce, elitismo):

1. **Cromosoma**: en vez de una lista de bits, cada individuo es una lista de caracteres (letras y espacio). Se genera eligiendo caracteres al azar de un alfabeto.
2. **Fitness**: ya no contamos unos, sino el número de posiciones donde el carácter del individuo coincide con el de la frase objetivo. El óptimo se alcanza cuando el fitness es igual a la longitud de la frase.
3. **Mutación**: en OneMax invertíamos un bit (0↔1). Aquí no existe un "opuesto" natural, así que la mutación **reemplaza** el carácter por otro elegido al azar del alfabeto.

El **cruce de un punto** y la **selección por torneo** se reutilizan tal cual, porque ambos operan sobre listas genéricas sin importar qué representen sus elementos (bits o caracteres). Con esto se concluye que:  los operadores de selección y cruce son independientes de la representación, mientras que la codificación del cromosoma, el fitness y (en este caso) la mutación sí dependen del problema.


##  Actividad 4

El **elitismo** copia directamente al mejor individuo de la generación actual hacia la siguiente. Esto garantiza que el mejor fitness registrado **nunca puede empeorar** de una generación a otra: en el peor caso se mantiene igual (si nadie más lo supera), pero jamás disminuye.

Sin elitismo, **toda** la nueva población —incluido el lugar donde vivía el mejor individuo— se genera por selección, cruce y mutación. Aunque la selección por torneo tiende a favorecer a los individuos más aptos, no hay ninguna garantía de que el mejor individuo sobreviva intacto: puede no ser elegido como padre, puede perder su buena combinación de genes al cruzarse, o puede ser dañado por la mutación. Por eso el mejor fitness de la población **sí puede bajar** de una generación a la siguiente cuando no hay elitismo.

En la práctica esto significa:

- **Con elitismo**: convergencia más rápida y estable, la curva de "mejor fitness" es monótona no decreciente. Riesgo: puede favorecer convergencia prematura si el "elite" domina la población.
- **Sin elitismo**: la curva de "mejor fitness" puede tener caídas temporales (oscila), y en promedio se necesitan más generaciones para alcanzar el óptimo, aunque también se mantiene algo más de diversidad genética al no proteger siempre a los mismos individuos.

 De acuerdo a lo ejecutado podemos responder la siguiente pregunta: 

 el mejor fitness **puede disminuir** de una generación a otra cuando no hay elitismo, porque nada protege al mejor individuo de perderse en el proceso de selección/cruce/mutación. Con elitismo, la curva de mejor fitness es monótona no decreciente por construcción. La diferencia suele ser más notoria con poblaciones pequeñas o tasas de mutación altas, donde es más fácil que el mejor individuo "se pierda" entre generaciones.


