#Pythonic Classes via Special Methods

Python expone una gran parte de sus mecanismos internos a traves de sus **metodos especiales (dunder methods)**. La cual es omnipresente en Python. Una funcion como **len()** explota el metodo especial **__len__()**.
Lo que significa que tenemos una ordenada interfaz publica (**len(x)**) que funciona cualquier tipo de clase. El **polimorfismo en Python** esta basado en que toda clase pueda responder a la **funcion len()**.
Cuando nosotros definimos una clase, nosotros podemos (y deberiamos) incluir estos **metodos especiales** para mejorar la integracion entre nuestra clase y el resto de **Python**.

**Parte 1**, *Pythonic Classes Via Special Methods*, se extendera en lo basico de las tecnicas de la **programacion orientada a objetos** para crear **clases** que son mas *Pythonicas*. Cualquier clase que podria ser capaz de integrar sin problemas con otras partes de Python. Un ajuste cercano con otras partes de Python nos permitira usar muchas funciones del lenguaje y de la biblioteca estandar, y los clientes de nuestros *paquetes y modulos* podrian tener mas confianza al usarlos y tendran mas exitos para mantenerlos y extenderlos.

En cierto modo, nuestras clases pueden aparecer como extensiones de Python. Queremos que nuestras clases sean mas como las **clases nativas en python**, que las distincionos entre: **el lenguaje**, **libreria estandar** y **nuestra aplicacion** sean minimisadas.

**Python** usa un largo numero de **metodos especiales**. Estos caen en las siguientes pocas  categorias discretas:

- **Attribute Acess:** Estos metodos especiales implementan lo que se ve como un "**objeto.atributo**" en una expresion, "**objeto.atributo**" en la "lado izquierdo" de una asignacion, un "**objeto.atributo**" en una instruccion "*del*".
- **Callables**: Este metodo especial implementa que lo que vemos como una funcion que es aplicado a los argumentos, al igual que las **funciones pre-fabricadas** como **len()**.
- **Collections**: Estos **metodos especiales** implementan numerosas caracteristicas de colecciones. Esto envuelve los metodos como: **sequence[index]**, **mapping[key]** y **some_set|another_set**.
- **Numbers**: Estos **metodos especiales** nos proveen de **operadores aritmeticas** y **operadores de comparacion**. Nosotros podemos usar estos metodos para expandir el dominio de numeros con los que Python funciona.
- **Contexts**: Estos son **dos metodos especiales** que definen un iterador. Estos no es escencial desde que las funciones generadoras manejan esta caracteristica de manera elegante. Sin embargo, vamos a echar un vistaso a como podemos diseñar nuestros propios iteradores.    

Algunos de estos **metodos especiales** fueron introducidos en *Python 3 Object Oriented Programming*. Nosotros veremos estos topicos y introduciremos algunos metodos adicionales que se ajustan a un tipo de categoria *basica*.

Includo dentro de esta categoria basica, nosotros tendremos que hondar en estos topicos por descubrir.
Nosotros empezaremos con los *verdaderamente basicos metodos especiales*. Hay algunos metodos que son especialmente bastante avanzados que son lanzados dentro de la categoria basica porque no parecen pertenecer a ningun otro lado.

El metodo **__init__()** permite una gran libertad en proveer valores inciales a un objeto. En el caso de un objeto **inmutable**, esta es la definicion escencial de una instancia, y la claridad se vuelve muy importante. En este capitulo, nosotros revisaremos numerosos alternativas de diseños para este metodo.















