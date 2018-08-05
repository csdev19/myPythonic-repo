# The __init__() Method

El metodo **__init__()** es profundo por dos razones. La inicializacion es el primer gran paso en la vida de un objeto; todo objeto debe ser  inicializado adecuadamente para funcionar de manera adecuada. La segunda razon es que los valores de los **argumentos** para **__init__()** pueden tomar muchas formas.

Porque estos tienen muchas maneras de proporcionar valores de argumento a **__init__()** pueden tomar muchas formas. Echemos un vistaso a varios de ellos. Queremos maximizar la claridad, para esto necesitamos definir una **inicializacion** que caracterize adecuadamente el dominio del problema.

Sin embargo, antes de poder acceder al metodo **__init__**, debemos analizar la jerarquia de clases implicita en Python, echando un vistazo, brevemente, a la clase llamada **object**. Esto establecera el escenario para comparar el comportamiento por defecto con diferentes tipos de comportamientos que nosotros queremos para nuestras propias clases.  

En este capitulo, nosotros veremos diferentes formas de inicializacion para objetos simples (por ejemplo, jugar cartas). Despues de esto, podremos echar un vistazo a objetos mas complejos, como manos que involucran colecciones y jugadores que involucran estrategias y estados.

## The implicit superclass - object 

Cada definicion de una clase en Python tiene una superclase implicita(en otras palabras heredan de): la clase **object**. Es una definicion de clase muy simple que hace casi nada. Podemos crear **instancias** de la clase padre **object**, pero nosotros no podemos hacer mucho con ello porque muchos de los **metodos especiales** simplemente levantan excepiones.

Cuando nosotros definimos nuestras propias clases, **object** es la clase padre (superclass). El siguiente es un ejemplo de definicion de clase que simplemente extiende la superclase **object** con un nuevo nombre:
```python
class x:
    pass
```
Las siguientes son las respuestas de la consola
```console
>>> X.__class__
<class  'type'>
>>> X.__class__.__base__
<class 'object'>
```

Podemos ver que una clase es un objeto de la clase llamada **type** y esta **clase base** para nuestra nueva clase es la clase llamada **object**.

Como podemos ver en este metodo, echamos un vistaso al comportamiento por defecto heredado de **object**. En algunos casos, el comportamiento del metodo especial de la **superclase** sera exactamente lo que nosotros queremos. En otros casos, nosotros necesitaremos reescribir el **metodo especial**.

## The base class object __init__() method

Fundamental para el ciclo de vida de un objeto es su creacion, inicializacion, y destruccion. Nosotros aplazaremos la creacion y destruccion a un capitulo posterior en metodos especiales mas avanzados y solo nos enfocaremos en la **inicializacion** por ahora.

La superclase padre de todas las demas (**object**), tiene como implementacion por defecto el metodo **__init__()** que equivale a pasar ("pass" palabra reservada). Nosotros no estamos obligados a implementar **__init__()**. Si es que no queremos implementarla, entonces no se crearan variables de instancion cuando se crea el objeto. En algunos casos, este comportamiento por defecto es aceptable.

Nosotros podemos siempre agregar atributos a un objeto que es una subclase de la clase base, **object**. Considere la siguiente clase que requiere dos variables de instancia pero nos las inicializa:
```python
class Rectangle:
    def area(self):
        return self.length * self.width
```

La clase **Rectangle** tiene un metodo que usa dos atributos para retornar un valor. Los atributos no fueron inicializados en ningun lado. Esto es **ILEGAL** en Python. *Esta es una extraña forma de especificar valores para los atributos*, pero es valido.
Desde la consola con la instancia de la clase **Rectangle** ya hecha:
```console
>>> r = Rectangle()
>>> r.length, r.width = 12, 4
>>> r.area()
104
```
Mientras esto es ilegal, es un recurso potencial para una gran confusion, lo cual es una buena razon para cubrirlo.

Sin embargo, este tipo de diseño otorga flexibilidad, por lo que podria haber ocasiones en que no necesitaremos establecer todos los atributos en el metodo **__init__()**. Caminamos por una linea muy fina aqui. Un atributo opcional es un tipo de subclase que no es declarada formalmente como una **subclase**. Estamos creando **polimorfismo** de manera que podria conducir confunsion y un uso inapropiado de complejas declaraciones **if**. Mientras que los atributos no inicializados pueden ser utiles, estos podrian ser un sintoma de un mal diseño. 

El poema (texto sagrado xdxd) **Zen of Python** (import this) ofrece el siguiente aviso:

Un metodo **__init__()** deberia hacer que las 
"*Explicit is better than implicit*"
variables de instancia sean explicitas (mas obvias)


## Implementing __init__() in a superclass
Nosotros inicializamos un objeto implementando el **metodo __init__()**. Cuando un objeto es creado, Python primero crea un objeto vacio y luego llama el metodo **__init__()** para ese objeto nuevo. Esta funcion de metodo generalmente crea las variables de instancia del objeto y realiza cualquier otro proceso de una sola vez.

Las siguientes son algunas definiciones de ejemplo de una jerarquia de clase de una **carta (Card)**. Definiremos una clase padre llamada **Card** y tres subclases que son variaciones del tema basico de la carta. Tenemos 2 variables de instancia que han sido seteadas directamente desde los **valores de los argumentos** y dos variablesque son calculadas por el metodo incializador:
```python
class Card:
    def __init__(self, rank, suit):
        self.suit = suit 
        self.rank = rank 
        self.hard, self.soft = self._points()

class NumberCard (Card):
    def _points (self):
        return int(self.rank), int(self.rank)

class AceCard (Card):
    def _points (self):
        return 1, 11
class FaceCard (Card):
    def _points (self):
        return 10, 10
```
En este ejemplo nosotros factorizamos el metodo **__init__()** dentro de la clase padre poruqe es una inicializamos comun en la superclase, **Card**, que aplica en todas las otras 3 subclases **NumberCard**, **AceCard** y **FaceCard**.

Esto muestra un diseño comun de polimorfismo. Todas las subclases tienen una implementacion unica del metodo **_points()**. Todas las subclases tienen firmas identicas: estas tienen los mismo metodso y atributos. Objetos de estas tres subclases pueden ser usadas indistintamente en una aplicacion.

Si nosotros simplemente usamos caracteres para trajes, podremos crear instancias de **Cards** como se muestra en el siguiente codigo:
```python
cards = [ 
    AceCard('A', '♠'), 
    NumberCard('2','♠'), 
    NumberCard('3','♠'),
]
```
Nosotros enumeramos la clase, el rango y el traje de varias cartas en una lista. A la larga, necesitaremos una funcion de creacion mas inteligente para instanciar cartas(**Card**); enumrando las 52 cartas y de esta manera es muy tediosa y tiende a errores. Antes de llegar a las funciones de creacion, debemos mirar otras tareas.

*** Nota : por traje nos referimos a el simbolo de la carta, ej. trebol, espadas, cocos, etc***

## Using __init__() to create manifest constans

Nosotros podemos definir una clase para los trajes de nuestras cartas. En **blackjack**, ls trajes no importan asi que un caracter cualquiera puede funcionar.

Nosotros usamos la construccion del traje como un ejemplo para crear **objetos constantes**. En muchos cases, nuestra aplicacion puede tener un pequeño dominio de objetos que pueden ser definidos como una coleccion de constantes. Un dominio estatico de objetos puede ser parte de implementar un patron de diseño de **Estrategia** o de un **Estado**.

En algunos casos, nosotros podriamos tener una serie constante de objetos creados en una inicializacion o archivo de configuracion, o  nosotros podriamos querer crear objetos constantes con los parametros de la linea de comandos. Nosotros regresaremos a los detalles del diseño de la inicializacion y el diseño de arranque en el capitulo 16, *Coping with the Command Line*.

Python no tiene un mecanisma simple y formal para definir un objeto como inmutable. Veremos las tecnicas para asegurar la inmutabilidad en el capitulo 3, *Attribute Access, Propoerties and Descriptors*. En este ejemplo, tiene sentido que para los atributos de los trajes de las cartas sean inmutables.

Lo siguiente es una clase que usaremos para construir cuatro constantes:

```python
class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
```
El siguiente es el dominio de "constantes" que vamos a construir alrededor de esta clase:
```python
Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
```
Ahora nosotros podemos crear cartas como se ve en el siguente pedazo de codigo:
```python
cards = [
    AceCard('A', Spade), 
    NumberCard('2', Spade), 
    NumberCard('3', Spade), ]
```
Por ejemplo, este pequeño metodo, esta no es una gran mejora en comparacion con el unico traje de caracter. En casos mas complejos, puede haber una lista pequeña de objetos de tipo **Strategy** o **State** que pueden ser creados del a manera vista. Esto puede hacer que el patron **Strategy** o **State** trabajen de manera eficiente **reusando** objetos desde una pequeña y **estatica** piscina de constantes.

Tenemos que reconocer que en **Python** estos objetos no son tecnicamente **contantes**, son **mutables**. Hay mucho beneficios en hacer codigo extra para hacer estos objetos verdaderamente inmutables. 


CAPITULOS INTERNOS: 
- [Leveraging __init__() via a factory function](url)
- [Simple composite objects](url)

