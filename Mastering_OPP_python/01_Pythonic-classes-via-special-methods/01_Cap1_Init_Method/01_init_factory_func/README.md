# Leveraging __init__() via a factory function

Podemos crear un mazo entero de cartas mediante la funcion fabrica. Esto es mejor que enumerar las 52 cartas, en **Python**, tenemos dos enfoques comunes para las fabricas de la siguiente manera:
- Definimos una funcion que crea objetos de las clases requeridas.
- Definimos una clase que tienen metodos para crear objetos. Este es el patron de diseño **full factory** (fabrica completa)

En **Python**, una clase no es **REQUERIDA**. Esta es simplemente buena idea cuando hay fabricas relacionadas que son complejas. Una de las fortalezas de **Python** es que no estamos forzados a usar una **jerarquia** de clases cuando una **funcion simple** podria funcionar igual de bien. 

Podemos siempre **reescribir** una funcion para que sea  un objeto apropiadamente llamado si surge la necesidad.
Desde un objeto invocable, podemos refactorizarlo en una jerarquia de clases para nuestras **fabricas**.

La ventaja de la definicion de clases en general es guardar codigo y **REUSARLO** mediante la herencia. 
La funcion de una **clase "factory"** (o creadora) es envolver(wrapp) la jerarquia objetivo de la clase y la complejidad de la construccion de un objeto. Si tenemos una clase creadora, podemos agregar **subclases** a esta clase cuando extengamos la jerarquia de la clase objetivo. Esto nos da una clases polimorficas de fabrica; las diferentes definiciones de clases fabrica tienen la  misma firma del metodo y puede ser usado indistintamente.

Este polimorfismo de nivel de clase puede ser muy util con lenguajes esticamente compilados como **java** o **c++**. El compilador puede resolver los detalles de la clase y los metodos cuando generamos codigo.

Si las definiciones de fabrica alternativas no reutilizan ningun codigo, entonces la jerarquia de clase no sera de mucha utilidad en **python**. Podemos simplemente usar funciones que hagan las mismas tareas.

Lo siguiente es **una funcion fabrica** para nuestras **subclases Card**:
```python
def card(rank, suit):
    if rank == 1: return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = { 11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else: 
        raise Exception('Rank out of range')
```

Esta funcion crea una **clase Card** (instanciaria la clase) basado en **un rango numerico** (rank) y un objeto **simbolo para la carta** (suit). Ahora podemos crear cartas de una manera mas simple. Hemos **encapsulado la tarea de construccion** en una simple funcion de fabrica, permitiendo que una aplicaion se construya sin saber precisamente como funciona la jerarquia de clases y el diseño polimorfico.

El siguiente ejemplo demuestra como podemos construir un maso de cartas con esta funcion de fabrica:
```python
deck = [card(rank, suit)
    for rank in range(1, 14)
        for suits in (Club, Diamond, Heart, Spade)]
``` 

Esto enumera todos los **ranks** y los **suits** para crear un maso de 52 cartas.

## Faulty factory design and the vague else clause

Note que la estructura de la instruccion **if** en la funcion **card()**. No usamos un **else** que lo atrapara todo dentro del proceso, nosotros enraizamos una excepsion. El uso de un **else** que atrapae todo esta sujeto a un pequeño debate.

Por un lado, se puede argumentar que la condicion que pertenece a una clausula **else** nunca debe dejarse de enunciar porque puede ocultar sutiles errores de diseño.
Por otro lado, algunas condiciones son muy obvias. Es importante evitar una clausula vaga **else**.
Considere la siguiente variante en esta definicion de funcion de fabrica:
```python
def card2(rank, suit):
    if rank == 1: return AceCard('A', suit)
    elif 2 <= rank < 11: return NumberCard(str(rank), suit)
    else: 
        name = { 11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
``` 
Lo siguiente es lo que pasaria cuando intentemos construir un maso:
```
deck2 = [card2(rank, suit) 
    for rank in range(13) 
        for suit in (Club,Diamond, Heart, Spade)]
```
Funciona ? Que pasaria si la condicion **if** fuera mas compleja ?

Algunos programadores pueden entender esta declaracion **if** de un vistazo. Otros lucharan por determinar si todos los casos son propiamente exclusivos. Para la progoramacion avanzada en **Python**, no debemos dejar que el lector deduzca las condiciones que se aplican a la clausula **else**. Para decirlo simple, deberia ser **explicito**.

## Simplicity and consistency using elif sequences

Nuestra funcion fabrica, **card()**, es una mixtura de dos patrones de diseño de fabrica muy comunes:
- Una secuencia de **if-elif** (machine learning xdxd)
- Un mapeo

Por simplicidad, es mejor enfocarse solo en una de estas tecnicas que en ambos. Siempre podemos reemplazar un **mapping**(mapeo) con condiciones **elif**. (Si, siempre. sin embargo, lo contrario de esto no siempre es verdad; convertir condiciones **elif** a **mapeos** puede ser desafiante.) 

El siguiente es una fabrica de **Card** con **mapping**:
```python
def card3(rank, suit):
    if rank == 1: return AceCard( 'A', suit )
    elif 2 <= rank < 11: return NumberCard( str(rank), suit )
    elif rank == 11: return FaceCard('J', suit )
    elif rank == 12: return FaceCard('Q', suit )
    elif rank == 13: return FaceCard('K', suit )
    else:
    raise Exception("Rank out of range")
```
Nosotros escribimos la funcion fabrica **card()**. El mapea fue transformado en clausulas **elif** adicionales. Esta funcion tiene la ventaja que es mas consistente que su version enterior.

CAPITULOS INTERNOS:
- [Simplicity using mapping and class objects](url)