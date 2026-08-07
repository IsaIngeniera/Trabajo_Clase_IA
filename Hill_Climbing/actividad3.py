import random
import numpy as np
import matplotlib.pyplot as plt

SEED = 8
random.seed(SEED)
np.random.seed(SEED)

## para que se de la aleatoriedad
# la funcion objetvio es manhattan
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#HAY QUE TENER EN CUENTA QUE UN HOSPITAL ES UNA TUPLA, UN ARRGELO DE DOS ELEMENTOS, 
#ENTONCES SI RECORREMOS HOSPITALS, RECORREMOS TUPLAS

#el costo total es la sumatoria de las distancias minimas de cada casa con el hospital
def total_cost(houses, hospitals):
    return sum(
        min(
            manhattan(house, hospital) for hospital in hospitals # empezamos desde lo interno,
            #se consigue la distancia manhattan de casa con hospital
            # se recorre primero el hospital, entonces para una sola casa sacamos la distancia
            #con cada hospital
            )
               for house in houses)
#despues de esa distancia se saca la distanica minima de esa casa con el hospital, 
#ahora despues de consguir eso minimo, recorremos la otra casa


def plot_state(height, width, houses, hospitals, title=None):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(-0.5, width - 0.5)
    ax.set_ylim(height - 0.5, -0.5)
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(True)

    if houses: #se guardan las coordenadas de las casas con zip
        hr, hc = zip(*houses)
        ax.scatter(hc, hr, marker='s', s=110, label='Casas') #para ponerlas en la grafica
    if hospitals:
        rr, cc = zip(*hospitals)
        ax.scatter(cc, rr, marker='P', s=180, label='Hospitales')

    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))
    ax.set_title(title or f'Costo = {total_cost(houses, hospitals)}') #el titulo de
    #la grid es el costo total por eso sacamos la funcion de costo aqui.
    plt.tight_layout()
    plt.show()


#DEFINE LAS VARIABLES DE ALTURA, NUMERO DE CASAS Y HOSPITALES

HEIGHT, WIDTH = 10, 16
NUM_HOUSES = 18
NUM_HOSPITALS = 3

    #RECORRE LAS CELDAS PERO ANTES CREA UNA TUPLA CON LAS COORDENADAS DEL MAPA

all_cells = [(r, c) for r in range(HEIGHT) for c in range(WIDTH)]
# AQUI SE ELIGEN LAS UBICACIONES DE LAS CASAS EN LA CELDA
houses = set(random.sample(all_cells, NUM_HOUSES))
#SE CONSIGUEN LAS CELDAS DISPONIBLES, LAS QUE NO TIENEN CASAS 
available = list(set(all_cells) - houses)
#CON ESAS CELDAS DISPONIBLES ELEGIMOS LAS UBC DEL HOSPITAL
initial_hospitals = set(random.sample(available, NUM_HOSPITALS))


#SE UTILIZA LA DEF DE ESTADO. 
plot_state(HEIGHT, WIDTH, houses, initial_hospitals,
           title=f'Estado inicial — costo {total_cost(houses, initial_hospitals)}')

#osea que la dfefnicion de estado es la que coge las ubciaciones de house y hosp las pone en el grid y ya? 

#VECINOS!
#lo que hace es que mira si el siguiente movimiento es valido, y lo guarda en vecinos
def neighbors_of_state(height, width, houses, hospitals):
    neighbors = [] #arreglo donde se guarda vecinos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-2, 0), (2, 0), (0, -2), (0, 2),
             (1,1), (-1,1), (1,-1),(-1,-1)] #los mov que puede hacer 

    for hospital in hospitals:#primer for recorre los hospitales
        for dr, dc in moves: #recorre los movimientos, fila y columna
            #se guarda en candidato 
            candidate = (hospital[0] + dr, hospital[1] + dc)
            #UN HOSPITAL ES UNA TUPLA, TIENE (FILA, COLUMNA)
            #sumamos el valor de la fila y el valor de la columna con esa tupla

            #RESTRICCIONES
            #PRIMERO VER SI NO SE SALE DE LOS LIMITES DEL GRID
            if not (0 <= candidate[0] < height and 0 <= candidate[1] < width):
                continue
             #DESPUES VER SI ESE LUGAR AL QUE SE MUEVE ESTA OCUPADO POR UNA CASA O HOSP
            if candidate in houses or candidate in hospitals:
                continue
             # SINO, SE REALIZA ESTO:
             #primero se hace una copia de hospitals en new_state, para poder modificarla sin
             #dañar al og hospital
            new_state = set(hospitals)
            #ahora new_state tiene las ubcs de los hospitals, y elimina al hospital que
            #estamos reocrriendo ahora
            new_state.remove(hospital)
            #añadimos el candidato a la lista de ubcs de hospitals que copiamos
            new_state.add(candidate)
            #se añade a la lista de neighbors la lista de ubicaciones de hospital con el candidato ya agregado
            neighbors.append(new_state)

    return neighbors


"""
Actualmente un hospital solo se mueve una celda.
 Crea un vecindario que permita movimientos de hasta dos celdas.
 ¿Mejora el resultado? ¿Cuánto aumenta el número de vecinos evaluados?

 RTA: Al crear diferentes movimientos hasta 2 celdas, se generan mas del doble de vecinos que 
 un movimiento de solo una 1 celda, aumentando mas el procesamiento del codigo. Por otro lado, 
 el resultado no mejora significativamente. 
"""

neighbors = neighbors_of_state(HEIGHT, WIDTH, houses, initial_hospitals)
print('Número de vecinos:', len(neighbors))
print('Costo actual:', total_cost(houses, initial_hospitals))
print('Mejor costo vecino:', min(total_cost(houses, n) for n in neighbors))



def hill_climbing(height, width, houses, num_hospitals, initial_state=None,
                  max_iterations=200, rng=None):
    rng = rng or random.Random()
    available = list(
        set(
            (r, c) for r in range(height) #fila, por cada una unidad de fila, se recorren
            #las columnas

            for c in range(width) #columna
            # recorre cada celda, reocrriendo fila y columna
            ) - houses # ahora con la lista de todas las celdas, restamos el conjunto de casas
            #para obetner las celdas que estan vacias
        )
    current = set(initial_state) if initial_state is not None else set(rng.sample(available, num_hospitals))
    # guarda el estado inicial, sino lo crea con la lista available
    history = [total_cost(houses, current)] #va guardando los costos totales de las distancias que sumamos antes 
    states = [set(current)] #ubicaciones del hospital

    for _ in range(max_iterations): #loop que solo termina si se sale del rango de las iteraciones 
        neighbors = neighbors_of_state(height, width, houses, current) #conseguimos los vecinos 
        if not neighbors: # si no se presentan vecinos es porque ya ese punto es el mas alto.
            break

        costs = [total_cost(houses, n) for n in neighbors] #se consigue el costo total de cada lista de ubicaciones que 
        #guarda vecinos
        best_cost = min(costs) #se consigue el costo minimo
        current_cost = history[-1] #se consigue el costo que ahora tenemos, que es el utlimo elemento que tenemos en history

        if best_cost >= current_cost: #IMPORTANT!, HACEMOS LA COMPARACION
            #Si best cost es mayor que el cost que tenemos ahora,significa que ya tenemos el costo menos grande
            break
        #SINO, 
        best_neighbors = [n for n, c in 
                          #AQUI RECORREMOS CADA TUPLA Y ELEGIMOS N, que es el vecino 
                          
                          zip(neighbors, costs)
                          #LO QUE HACE ZIP, ES UNIR DOS LISTAS DEL MISMO TAMAÑO EN TUPLAS
                          #EJ: (VECINO1,COSTO DE ESE VECINO)


                           #Solo lo escogemos SI el costo es el mejor, el que escogimos antes
                            if c == best_cost

                            ] #LO GUARDAMOS EN UNA LISTA PQ NO SABEMOS SI HAY DIFERENTES COSTOS MEJORES, 
        current = set(rng.choice(best_neighbors))  #AQUI SI HAY MAS DE UNO LO ELIGUE AL AZAR
        history.append(best_cost) #AL HISTORY PONEMOS EL COSTO MEJOR
        states.append(set(current)) #EN ESTADOS PONEMOS EL LA UBICACION DEL HOSPITAL, STATES TIENE TODOS LOS
        # ESTADOS DE HOSPITALS QUE HEMOS HECHO

    return current, history, states

#HACEMOS EL HILL CLIMBING AQUI
solution, history, states = hill_climbing(
    HEIGHT, WIDTH, houses, NUM_HOSPITALS,
    initial_state=initial_hospitals,
    rng=random.Random(SEED)
)
#IMPRIMIMOS LOS RESULTADOS
print('Costo inicial:', history[0])
print('Costo final:', history[-1])
print('Iteraciones con mejora:', len(history) - 1)
plot_state(HEIGHT, WIDTH, houses, solution,
           title=f'Hill Climbing — costo final {history[-1]}')


#GRAFICA QUE NOS MUESTRA LA ITERACION Y EL COSTO DE CADA PASO

plt.figure(figsize=(7, 4))
plt.plot(range(len(history)), history, marker='o')
plt.xlabel('Iteración')
plt.ylabel('Costo')
plt.title('Evolución del costo')
plt.grid(True)
plt.show()

def random_restart(height, width, houses, num_hospitals, restarts=30, seed=0):
    master_rng = random.Random(seed)
    runs = []
    best = None

    for restart in range(restarts):
        run_seed = master_rng.randrange(10**9)
        solution, history, _ = hill_climbing(
            height, width, houses, num_hospitals,
            rng=random.Random(run_seed)
        )
        record = {
            'restart': restart,
            'solution': solution,
            'initial_cost': history[0],
            'final_cost': history[-1],
            'iterations': len(history) - 1
        }
        runs.append(record)
        if best is None or record['final_cost'] < best['final_cost']:
            best = record

    return best, runs

best, runs = random_restart(HEIGHT, WIDTH, houses, NUM_HOSPITALS, restarts=40, seed=SEED)
print('Mejor costo:', best['final_cost'])
print('Reinicio ganador:', best['restart'])
plot_state(HEIGHT, WIDTH, houses, best['solution'],
           title=f'Random Restart — mejor costo {best["final_cost"]}')




final_costs = [run['final_cost'] for run in runs]
plt.figure(figsize=(8, 4))
plt.plot(final_costs, marker='o')
plt.axhline(min(final_costs), linestyle='--', label='Mejor costo')
plt.xlabel('Reinicio')
plt.ylabel('Costo final')
plt.title('Variabilidad entre reinicios')
plt.legend()
plt.grid(True)
plt.show()
     