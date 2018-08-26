# Python's Instance, Class and Static Methods Desmitificados

## Tabla de contenidos

- [Instance, Class and Static Methods - Una revision general]()
    - [Instance Methods]()
    - [Class Methods]()
    - [Static Methods]()
- [Vamos a verlos en accion]()
- [Fabricas de deliciosa Pizza con @classmethod]()
- [Cuando usar Static Methods]()
- [Puntos Claves]()


En este tutorial vamos intentar desmitificar que pasa detras de [class methods (metodos de clase)](https://docs.python.org/3/library/functions.html#classmethod), [static methods (metodos estaticos)](https://docs.python.org/3/library/functions.html#staticmethod), y los metodos de instanciacion regular.

Si tu desarrollas una comprension intuitiva de sus diferencias, podras ser capas de escribir **python orientado a objetos** que transmite lo que quieres decir de manera clara y facil de mantener a largo plazo.


## Intance, Class and Static Methods - Una revision general

Vamos a empezar por escribir una clase (de Python3) que contiene ejemplos simples para estos tres tipos de metodos:

```python
class MiClase:
    def metodo(self):
        return 'metodo de instancia llamado', self

    @classmethod
    def metodoDeClase(cls):
        return 'metodo de clase llamado', cls

    @staticmethod
    def metodoEstatico():
        return 'metodo estatico llamado'
```

### Intance Methods (Metodos de instancia)

El primer **metodo** en **MiClase**, llamado **metodo**, es un **metodo de instancia regular**. Eso es lo basico, tipo sencillo que se usara la mayor parte del tiempo. Podemos ver que este **metodo** toma un **parametro**, **self**, el cual apunta a una instancia de **MiClase** cuando el metodo es llamado (por supuesto los metodos de instancia pueden aceptar mas de un solo parametro).

Mediante el **parametro self**, los **metodos de instancia** pueden acceder libremente a **atributos y metodos** del mismo objeto. Esto les da muchisimo poder cuando debemos modificar el estado de un objeto.

No solo puede modificar el estado de un objeto, **los metodos de instancia** pueden tambien **acceder a la clase en sí**  a traves del atributo **self.__class__**. Esto significa que los metodos de instancia tambien pueden modificar el estado de la clase.

### Class Methods (Metodos de clase)

Vamos a comparar esto con el segundo metodo, **MiClase.metodoDeClase**. Hemos marcado este metodo con un decorador de **@classmethod** para marcarlo como un **metodo de clase**.

En lugar de aceptar un parametro **self**, **un metodo de clase** toma un parametro **cls**, que **apunta a la clase** -- y no a la instancia del objeto -- cuando el metodo es llamado.

Porque el metodo de clase **solo tiene acceso** a este argumento **cls**, este no puede modificar el estado de la instancia del objeto. Eso podria requerir acceso a **self**. Sin embargo, **un metodo de clase**puede modificar el estado de la clase que se aplica entre todas las instancia de la clase.

### Static Methods (Metodos estaticos)

El tercer metodo, **Miclase.metodoEstatico** fue marcado con un decorador **@staticmethod** para denotar que es un **metodo estatico**.

Este tipo de metodo no tome ni el parametro **self* o el **cls** (pero por supuesto que es libre de aceptar un numero arbitrario de parametros).

Por lo tanto un **metodo estatico** no puede modificar el estado del objeto ni el estado de la clase. Los metodos estaticos estan retringidos en cuanto a los datos a los que pueden acceder, y son principalmente una forma de ponerle un **namespace** a sus metodos.


## Vamos a verlos en accion!

Yo se que esta discusion ha sido mas que nada **teorice** hasta este punto. Y yo creo que es importante que se desarrollo un entendimiento intuitivo para como estos tipos de metodos difieren en la partica. Vamos a ver unos ejemplos concretos ahora.

Vamos a echar un vistaso a como estos metodos se comportan en accion cuando queremos llamarlos. Empezaremos creando una instancia de la clase y luego llamaremos tres diferentes metodos sobre esta.

**MiClase** se configuro de tal forma para que cada implementacion de metodos retorne una tupla conteniendo informacion para que rastreemos lo que esta sucediendo -- y que partes de la clase o el metodo del objeto puede acceder.

### Aqui esta lo que pasa cuando nosotros llamamos un **intance method**:

```python
>>> obj = MiObjeto()
>>> obj.metodo()
('metodo de instancia llamado', <example.MiClase object at 0x7efdb5fa5470>)
```

Esto confirma que **metodo** (el metodo de instancia) a accesado a la instancia del objeto (escrito como **example.Miclase**) mediante el argumento **self**.

Cuando el **metodo** es llamado, Python reemplaza el argumento **self** con la **instancia del objeto**, **obj**. Podemos ignorar la **azucar sintactica**( **syntactic sugar** lo vamos a llamar asi mejor) de la sintaxis **de llama punto** ( **obj.method()** ) y pasando el **objeto de instancia** manualmente para obtener el mismo resultado:

```python
>>> MiClase.metodo(obj)
('metodo de instancia llamado', <__main__.MiClase object at 0x7fe620869f28>)
```

Pueden adivinar que pasaria si intentamos llamar al metodo si no llamamos primero a una instancia?

Por cierto, los **metodos de instancia** pueden acceder a la **clase** como tal a traves del atributo **self.__class__**. Esto hace que **el metodo de instancia** sea poderoso en terminos de restriccion de accesos - estos pueden modificar el estado de la instancia de un objeto y en la clase como tal.

### Vamos a intentar con **class method** acontinuacion:
```python
>>> obj.metodoDeClase()
('metodo de clase llamado', <class '__main__.MiClase'>)
```

Llamando **classmethod()** nos muestra que no tiene acceso al objeto **< MiClase instance >**, pero si al objeto **< class MiClase >**, representando la clase en si (todo en python es un objeto, incluso las clases como tales).

Date cuenta como **Python** automaticamente pasa la clase como primer argumento a la funcion cuando llamamos **MiClase.metodoDeClase()**. Llamando un metodo en **Python** a traves de la **sintaxis punto** desencadenando este comportamiento. El parametro **self** en el metodo de instancia trabaja de la misma manera.


### Vamos a llamar al **static method** ahora:
```python
>>> obj.staticmethod()
'metodo estatico llamado'
```

Viste como llamamos al **staticmethod** sobre el objeto y fuimos capaces de hacerlo exitosamente ? Algunos desarroladores se sorprenden cuando aprenden que es posible **llamar un metodo estatico** sobre una instancia de objeto.

Dentras de escenas **Python** simplemente fuerza las restricciones de acceso al no pasar de argumentos **self** o **cls** cuando un metodo estatico el llamado usando la sintaxis punto.

Esto confirma que los **metodos estaticos** nunca podran tener acceso a la instancia del objeto o al estado de la clase. Estos trabajaran como **funciones regulares** pero pertenece al **namespace** de clase (y al de cualquier instancia).

Ahora, vamos a que pasa cuando intentamos llamar a estos metodos en la clase como tal - sin crear una instancia del objeto antes:

```python
>>> MiClase.metodoDeClase()
('metodo de clase llamado', <class '__main__.MiClase'>)
>>> MiClase.metodoEstatico()
'static method called'
>>> MiClase.metodo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: metodo() missing 1 required positional argument: 'self'
```

Somos capaces de llamar el **classmethod()** y al **staticmethod()** bastante bien, pero cuando intentamos llamar el metodo de instancia **metodo()** nos lanza un error de tipo **TypeError**.

Y esto es de esperar - esta vez no creamos una instancia de objeto y intentamos llamar una **funcion de instancia** directamente en la clase **blueprint** como tal. Esto significa que no hay forma de que **Python** complete el argumento **self** y por lo tanto la llamada falla.

Esto deberia hacer la diferencia entre estos 3 tipos de metodos mas clara. Pero para no dejarlo solo asi. En las siguientes dos secciones vamos a ver 2 ejemplos mas practicos para saber cuando usar estos **tipos de metodos especiales**.

Vamos a basar los ejemplos en esta **clase Pizza**:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

>>> Pizza(['cheese', 'tomatoes'])
Pizza(['cheese', 'tomatoes'])
```
**NOTA**: este codigo de ejemplo y los que estan mas adelante en el tutorial usan [Python 3.6 f-strings](https://dbader.org/blog/python-string-formatting) para construir el **string** que retorna **__repr__**. En **Python2** y versiones de **Python3** antes de **3.6** podriamos usar una expresion de formacion de **string** distinta, por ejemplo:

```python
def __repr__(self):
    return 'Pizza(%r)' % self.ingredients
```

## Delicius Pizza factories with @classmethod

Si tu has sido expuesto a la pizza en el mundo real tu deberias saber que hay muchas deliciosas variaciones disponibles.

```python
Pizza(['mozzarella', 'tomatoes'])
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
Pizza(['mozzarella'] * 4)
```

Los italianos descubrieron su taxonomía de la pizza hace siglos, por lo que estos deliciosos tipos de pizzas tienen sus propios nombres. Haríamos bien en aprovechar eso y darles a los usuarios de nuestra clase de Pizza una mejor interfaz para crear los objetos de pizza que anhelan.

Uno buena y limpia forma de hacer esto es usando un **metodo de clase** como una [factory functions](https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)) para los diferentes tipos de pizzas podemos crear:

```
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
```

Noten como estamos usando el argumento **cls** en los metodos de factoria **marguerita y prosciutto** en lugar de llamar el cosntructor **Pizza** directamente.

Este es un truco que podemos usar para seguir el principio [Don't Repeat Yourself (DRY)](https://en.wikipedia.org/wiki/Don't_repeat_yourself). Si es que nosotros decidimos renombrar esta clase en algun punto no debemos recordar actualizar el nombre del constructor en todos los demas **classmethods factory functions**.

Ahora, que podemos hacer con estos **factory methods** ? vamos a probarlos:

```python
>>> Pizza.margherita()
Pizza(['mozzarella', 'tomatoes'])

>>> Pizza.prosciutto()
Pizza(['mozzarrella', 'tomatoes', 'ham'])
```

Como tu puedes ver, podemos usar las **factory functions** para crear nuevos objetos **Pizza** que son configurados de la manera que nosotros queremos. Estos usan el mismo constructor **__init__** internamente y simplemente provee un shortcut para recordar todos los varios ingredientes.

Otra manera de ver este usa pero **metodos de clase** es cuando nos permiten definir constructores alternativos para nuestras clases.

Python permite un metodo __init__ por clase. Usando **metodos de clase** es posible agregar constructores alternativos como sean necesarios. Esto puede hacer la interface para nuestras clases **autodocumentativas** (hasta cierto punto) y simplificar su uso.

## Cuando usar Static Methods

Es un poco mas dificil tener un buen ejemplo aqui.

```python
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
```

Ahora que es lo que cambiamos aqui ? Primero, modificamos el constructor y **__repr__** para aceptar como argumento extra el **radio**.

Y tambien agregamos un **metodo de instancia area()** que calcula y retorna el area de la pizza (esto podria ser un buen candidato para una **@property** - pero este es solo un ejemplo).

En lugar de calcular el area directamente dentro del **area()**, usando la conocida formula del area del circulo, la descomponemos en un metodos estatico **circle_area()**.

Vamos a probarlo:

```python
>>> p = Pizza(4, ['mozzarella', 'tomatoes'])
>>> p
Pizza(4, ['mozzarella', 'tomatoes'])
>>> p.area()
50.26548245743669
>>> Pizza.circle_area(4)
50.26548245743669
```

Seguro, esto es un ejemplo un poco simplista, pero ayuda a explicar algunos de los beneficios que los **metodos estaticos** proveen.

Como hemos aprendido, **metodos estaticos** no pueden accesar a la clase o al estado de la instancia porque no toman de argumento **cls o self**. Esa es una gran limitacion - pero es una buena señal para mostrar como un metodo en particular es independiente de todo lo que le rodea.

En el ejemplo anterior, es que claro que **circle_area()** no puede modificar la clase o la instancia de la clase en ninguna forma. (seguro, siempre podremos trabajar esto con una variable global pero ese no es el punto aqui).

Ahora, porque esto es util ?

Marcando un metodo como uno estatico no es solo una sugrenecia de que un metodo no modificara la clase o el estado de la instancia; esta restriccion tambien se aplica por al **runtime de Python**.

Tecnicas como estas nos permite comunicar claramete las partes acerca de la arquitectura de nuestra clase etonces este nuevo trabajo de desarrollo es mas naturalmente guiado para pasar dentro de estos limites establecidos. Por supuesto, esto podria ser bastante facil desafiar estas restricciones. Pero en la practica suelen ayudar a evitar modificaciones accidentales que van en contra del diseño original.

Puesto de otra forma, usando **metodos estaticos** y **metodos de clase** son formas de comunicar la intencicon del desarrollador mientras aplica esta intencion lo suficiente para evitar la mayoria de errores y **bugs** que podrian romper el diseño.

Se aplica con moderacion y cuando tiene sentido, escribir algunos de sus metodos de esa manera puede proporcionar beneficios de mantenimiento y hacer que sea menos probable que otros desarrolladores utilicen sus clases de forma incorrecta.

**Metodos estaticos** tambien tienen beneficios cuando empezamos a escribir codigo de testeo. Porque el metodo **circle_area()** es completamente independiente del resto de la clase es mucho mas facil de testear.

Nosotros no tenemos que preocuparnos acerca de configurar una instancia de clase completa antes podemos testear el metodo en un **unit test**. Podemos simplemente disparar como si estuvieramos probando una funciona regular. Nuevamente, esto hace que el mantenimiento futuro sea mas facil.

## Key Takeaways

- Metodos de instancia necesitan una clase instanciada y pueden accesar a la instancia a traves de **self**.
- Metodos de clase no necesitan una clase instanciada. Estos no pueden acceder a la instancia (self) pero tienen acceso a la clase como tal via **cls**.
- Metodos estaticos no tienen acceso a la clase **cls** o **self**. Estos trabajan como expresiones regulares pero extendiendo el namespace de la clase.
- Metodos estaticos y de clase comunican y (hasta cierto grado) impoenen la intencion del desarrollador sobre el diseño de clase. Esto puede tener beneficios en el mantenimiento.


## Referencia

- Este repo esta basado en la pagina REAL PYTHON [instance class and static methods](https://realpython.com/instance-class-and-static-methods-demystified/)
