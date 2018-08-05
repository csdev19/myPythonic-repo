# Simplicity using mapping and class objects

En algunos casos, podemos usar **mapping** por sobre una cadena de condiciones **elif**. Es posible encontrar condiciones que son tan complejas que una **cadena** de condiciones **elif** es la unica manera de expresarlas. Mientras tanto, para casos simples, un **mapeo** suele funcionar mejor y es mas legible.

Desde que **class** es **el primer objeto clase**, podemos facilmente **mapear** desde el parametro **rank** a la clase que debe ser construida.

Lo siguiente es una fabrica de **Card** que usa solo **mapping**:
```python
def card4(rank, suit):
    class_ = {
        1: AceCard, 11: FaceCard, 
        12: FaceCard, 13: FaceCard
        }.get(rank, NumberCard)
    return class_(rank, suit)
```
Nosotros **mapeamos** el objeto **rank** a una **clase**. Luego, aplicamos la **clase** hacia los valores **rank** y **suit** para construir la instancia final de **Card**.

Podemos usar tambien una clase **defaultdict**. Sin embargo, no es mas simple que un mapeo trivial estatico. Se ve como el siguiente codigo:
```python
defaultdict( lambda: NumberCard, {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard} )
```  

Note que el *default* de una clase **defaultdict** debe ser una funcion con *zero* argumentos. Nosotros usamos un constructor **lambda** para crear una funcion que encapsula alrededor de una constante. Esta funcion, sin embargo, tiene una clara deficiencia. Carece de la transicion de 1 a "A" y 13 a "K" que ya teniamos en las versiones anteriores. Cuando nosotros intentamos agregar esta **caracteristica**(feature), corremos hacia un poblema.

Necesitariamos cambiar el **mapeo** para proveer tanto para la **subclase Card** tan bien como la version **string** del objeto **rank**. Que podemos hacer para este **mapeo de dos partes**?. Hay 4 soluciones comunes:
- Podemos hacer dos mapeos en **paralelo**. No es algo recomendable, pero se mustrea para ver que lo indeseable acerca de esto.
- Podemos mapear hacia **dos tuplas**. Esto tiene alguna desventajas.
- Podemos mapear hacia una **funcion partial()**. La funcion **partial()**(parcial) es una caracteristica del **modulo functools**.
- Podemos considerar modificar nuestra definicion de clases para ajustar la legibilidad con este tipo de mapeo. Veremos esta alternativa en la siguiente seccion de **pushing __init__()** en la definicion de subclases.

Veremos esto con estos ejemplos:

## Two parallel mappings

Con el siguiente codigo:
```python
class_= {1: AceCard, 11: FaceCard, 
        12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
rank_str = {1:'A', 11:'J', 
            12:'Q', 13:'K'}.get(rank,str(rank))
return class_(rank_str, suit)
```
Esto no es deseable. Envuelve la repeticion de una secuencia llaves de mapeo : 1, 11, 12 y 13. La repeticion es mala porque las estructuras paralelas no parecen quedarse asi luego de que el software es **actualizado**.

NOTA: **Don't use parallel structures**
Two parallel structures should be replaced with tuples or some kind of proper collection.

## Mapping to a tuple of values
Con el siguiente codigo:
```python
class_, rank_str = {
    1: (AceCard,'A'),
    11: (FaceCard,'J'),
    12: (FaceCard,'Q'),
    13: (FaceCard,'K'),
}.get(rank, (NumberCard, str(rank)))
return class_( rank_str, suit )
```
Esto es razonablemente complaciente. No es mucho codigo para ordenar los casos de las cartas. Veremos como puede ser modificado o expandido, en caso de uqe necesitemos alterar la **jerarquia de Card** para agregar **subclases de Card** adicionales.

Esto hace sentir que es disparejo para mapear un valor **rank** a una clase objeto y solo uno de los dos argumentos para ser inicializado. Parece mas sensato asignar el **rank** hacia una **clase simple** o un **objeto de funcion** sin el desorden de proporcionar algunos de los argumentos.

## The partial function solution

En lugar de mapear una función de dos tuplas y uno de los argumentos, podemos crear una función **parcial()**. Esta es una función que ya tiene algunos (pero no todos) de sus
argumentos proporcionados. Usaremos la función **partial()** de la **biblioteca functools** para crear una parte de una clase con el argumento **rank**.

Lo siguiente es un **mapeo** desde **rank** hacia una funcion **partial()** que puede ser usada para construccion de objetos.
```python
from functools import partial
part_class= {
    1: partial(AceCard,'A'),
    11: partial(FaceCard,'J'),
    12: partial(FaceCard,'Q'),
    13: partial(FaceCard,'K'),
}.get(rank, partial(NumberCard, str(rank)))
return part_class( suit )
``` 

El mapeo asocia un objeto de **rank** con una función **parcial()** que se asigna a **part_class**. Esta función **parcial()** se puede aplicar al objeto del **suit** para crea el objeto final. El uso de funciones **parciales()** es una técnica común para
programación funcional. Funciona en esta situación específica en la que tenemos una función en lugar de un método de objeto. 
En general, sin embargo, las funciones **parciales()** no son útiles para la gran parte de la programacion orientada a objetos. En lugar de crear funciones **parciales()**, simplemente podemos actualizar el
método de una clase para aceptar los argumentos en diferentes combinaciones. Una funcion **parcial()** es  similar a crear una interfaz fluida para la construcción de objetos.

## Fluent APIs for factories

En algunos casos, nosotros diseñamos clases donde hay un orden definido para la utilizacion de metodos. Evaluando metodos secuencialmente es como crear una funcion **partial()**.

Podriamos tener **x.a().b()** en una notacion de objeto. Podemos pensarlo como **x(a, b)**. La funcion **x.a()** es un tipo de funcion **parcial()** que esta esperando por **b()**. Podemos pensar en esto como si fuera **x(a)(b)**.

La idea aqui es que **Python** ofrece dos alternativas para manejar un estado. POdemos actualizar un objeto o crear una **funcion parcial()** que es de cierta manera con estado. Debido a esta equivalencia, podemos reescribir una funcion **parcial()**








