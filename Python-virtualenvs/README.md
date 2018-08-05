# Python Virtual Environments and pip

Un tema fundamental a la hora de trabajar con python es el saber usar los ambientes virtuales y su sistema de paquetes. Y esta es mi documentacion al respecto.

## Porque necesitamos ambientes virtuales ?

**Python**, como la mayoria de lenguajes modernos, tiene su propia manera de descargar, guardar, y resolver paquetes ([modulos](https://en.wikipedia.org/wiki/Modular_programming)). Mientas esto da muchas ventajas existen muchas **decisiones interesantes** con respecto al guardado de **paquetes**, las cuales pueden traer algunos problemas, generalmente por el como y donde estan guardados.

## Donde se localizan los paquetes en Python ?

Existen unas cuantas locaciones comunes donde los paquetes de python pueden ser instalados en nuestro sistema. [Referencia de la definicion de un venv ](https://docs.python.org/3/library/venv.html#venv-def).
Por ejemplo la mayoria de los paquetes del sistema estan guardados en un directorio secundario de la ruta almacenada en [sys.prefix](https://docs.python.org/3/library/sys.html#sys.prefix).
El siguiente ejemplo es en el shell de python (Linux - Elementary):
```console
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
>>> import sys
>>> sys.prefix
'/usr'
```
Ahora, esta ruta es donde se han instalado todos los paquetes por defecto de python(o built-in), porque estamos partiendo del supuesto de que acabamos de instalar **python** en el sistema y solo tenemos los paquetes por defecto. 
Una vez entendido esto, tenemos que tener en cuenta que en **python** un topico muy relevante es el manejo de 
**third party packages**(paquetes de terceros), porque para instalarlos **python** tiene un **administrador de paquetes** "por defecto" por asi decirlo, y este es **PIP**. 
NOTA: para ver los paquetes globales consultar [getsitepackages](https://docs.python.org/3/library/site.html#site.getsitepackages). 

Como en este caso no es necesariamente un tutorial de como instalar pip dejare unos links con la info que yo creo necesaria para hacer esto (en Linux aunque para windows no varia mucho).
- [instalar pip en ubuntu y un poco de teoria](http://www.kacharreando.com/ubuntu/gestor-pip/)
- [pip + basic commands](https://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/)
- [Para descargar el codigo get-pip](https://bootstrap.pypa.io/get-pip.py)
- [Documentacion oficial](https://packaging.python.org/tutorials/installing-packages/)
- [Pypi - indice de paquetes en python](https://pypi.org/) : aqui encontraran la mayoria de paquetes en python, y en caso de que quieran compartir sus propios programas deberian subirlos aqui.

Ahora una vez aclarado, que python tiene su propio sistema de control de paquetes y que estos deben ser guardadon en algun lado, vamos a ver donde estan situados en general. 
```console
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
>>> import site
>>> site.getsitepackages()
['/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.5/dist-packages']
``` 
Pero, porque estas cosas nos deberian importar?
Esto nos importa porque por defecto cualquier instalacion de un **paquete de terceros** acabara siendo instalada de manera **global** y en esa ubicacion. Junto con todos los demas paquetes por defecto.

Ahora, en [Python](https://www.python.org/) existen dos versiones **2.x** y **3.x** las cuales suelen tener sutiles y aveces importantes diferencias, por lo cual no siempre un paquete hecho en la version **2.x** va a funcionar si lo corremos con la version **3.x**. Entonces al tener que actualizar nuestra version de **python** tendriamos el inconveniente que tendriamos que aceptar que no podriamos usar varios paquetes, por el hecho de que no son compatibles entre versiones. Pues aqui entran los **ambientes virtuales** para solucionar este problema de manera muy elegante.

## Que son los ambientes virtuales? (virtualenvs)

El objetivo principal de un ambiente virtual, es crear un entorno aislado para los proyectos de **Python**. Esto significa que cada proyecto va a tener sus **propias dependencias** independientes de los atributos globales que existan en el sistema.

Por ejemplo, el sistema puede tener python 3.5 y pero un paquete fue hecho en la version 3.3, entonces el paquete virtual puede ser creado con determinada version de python independiente de que de manera global tenga una version.    

Lo bueno acerca de estos ambientes virtuales es que podemos tener cuantos queramos dentro de nuestro sistema. Pues estos son carpetas que contienen unos cuantos **scripts**.
La mayoria de los links acerca los ambientes virtuales estan en las referencias. Y una que otra que pondre aqui. [venv module from the standard library](https://docs.python.org/3/library/venv.html).
NOTA: UN problema que podria surgir seria una confusion entre el pip de python2 y python3.
```console
$ pip install virtualenv
```
Otra herramienta interesante es el **pyvenv** [pyvenv vs virtualenv](https://www.reddit.com/r/learnpython/comments/4hsudz/pyvenv_vs_virtualenv/)

Para trabajar con esto haremos lo siguiente.
```console
$ mkdir python-virtual-environments && cd python-virtual-environments
$ python3 -m venv env
```
Esto nos creara una carpeta llamada **env** la cual contendra los scripts necesarios para que el ambiente virtual funcione. Ahora el beneficio de que hallamos usado **venv** es que nos obliga a escojer una version especifica de python3.

Desde **Python3.3 hasta 3.4** se recomienda que para crear un ambiente virtual se use el comando **pyvenv**.

Los archivos creados son los siguientes:
```console
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.5
│   ├── pip
│   ├── pip3
│   ├── pip3.5
│   ├── python -> python3.5
│   ├── python3 -> python3.5
│   └── python3.5 -> Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
├── include
├── lib
│   └── python3.5
│       └── site-packages
└── pyvenv.cfg
```
### Y que es lo que contiene en especifico ? 
- "bin" .- Archivos que interactuan con el ambiente virtual.
- "include" .- **C hearders** que compilan los paquetes de Python. 
- "lib" .- Una copia de la version de Python junto con la carpeta "**site packages**" donde esta instalada cada dependencia.

Ademas hay copias de, o [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) hacia algunas herramientas de python y a sus ejecutables como tal. Estos archivos son usados para estar seguro de que todo el **codigo de Python** y los demas comandos sean **ejecutados dentro del contexto del ambiente actual**, asi es como el aislamiento del ambiente global es realizado. 

Más interesante es el activar scripts en el directorio "bin". Estas secuencias de comandos se utilizan para configurar el **shell** para usar el ejecutable de Python del entorno y sus paquetes de sitio de forma predeterminada.

Para utilizar los paquetes / recursos de este entorno de forma aislada, debe "activarlo". Para hacer esto, solo ejecuta:
```console
$ source env/bin/activate

# y esto te apareceria o algo parecido
(env) $
```
Luego de uqe activamos el ambiente virtual, podemos ver que el **prompt** ha cambiado.

En caso de que queramos desactivarlo usaremos:
```console
(env) $ deactivate
# y deberia salir esto
$
```
Esto indica que ya esta fuera del ambiente virtual y tendrias acceso a los **modulos virtuales**.


Ahora un pequeño extra (yo no lo sabia hasta que lo lei hace un rato :v), vamos a instalar **bcrypt** para hashear una contraseña:
```console
$ pip -q install bcrypt
# no olviden el sudo porque es una instalacion global
$ python -c "import bcrypt; print(bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()))"
# devuelve esto
$ b'$2b$12$NrUcB6NRDUURkMGav8d3iu4jVIbSXe1gfherj5jMFi5g2pGcvr36m'
``` 

## Como funciona un ambiente virtual ?

Entonces, que significa exactamente "activar" un entorno? Saber que pasa debajo del capó puede ser muy importante para un desarrollador, especialmente cuando necesites entender ejecucion de ambientes, resolucion de dependencias, etc.

Para explicar como esto funciona, primera verifiquemos las ubicaciones de los diferentes ejecutables de Python. 
Con el entorno "deactivado" ejecutemos:
```console
$ which python3
/usr/bin/python3
```
Ahora lo activaremos y correremos el comando
```console
(venv1) $ which python3
/home/cris19/Studying/Python3/studying_python/Python-virtualenvs/python-virtual-environments/venv1/bin/python3
# en este caso esa es mi ruta, desde home hasta llegar al fichero que contiene el ambiente virtual
```
Ahora notamos que luego de la activacion del ambiente estamos consiguiendo diferentes rutas para los ejecutables de python. Porque la variable de entorno $PATH fue modificada.

Ahora probaremos ver la ruta con el ambiente deactivado y activado.
```console
$ echo $PATH
/home/cris19/Downloads/google-cloud-sdk/bin:/home/cris19/bin:/home/cris19/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/go/bin

# en mi caso sale asi

# ahora lo activamos
(venv1) $ echo $PATH
home/cris19/Studying/Python3/studying_python/Python-virtualenvs/python-virtual-environments/venv1/bin:/home/cris19/Downloads/google-cloud-sdk/bin:/home/cris19/bin:/home/cris19/.
# sale asi
```

En el ejemplo anterior, nuestro ambiente virtual "bin" esta ahora al inicio del **path**(ruta). Esto quiere decir que este sera el primer directorio que sera buscado cuando se corra un ejecutable en la terminal. Por lo tanto, el **Shell** utiliza la instancia de **python** de nuestra entorno virtual en lugar de la version de todo el sistema.

Esto deja algunas preguntas:
- Cual seria entonces la diferencia entre estos dos ejecutables?
- Como es capaz el ejecutable de python del entorno virtual de usar algo que no sea el **system site-packages**?

Esto puede ser explicado por como python arranca y donde esta ubicado en el sistema. Actualmente no hay ninguna diferencia entre esos dos ejecutables. *Son sus ubicacion de directorios lo que importa*.

Cuando Python es puesto en marcha, este "mira" en el **path** por un **binario**(el cual, en el ambiente virtual es actualmente una copia, o un symlink de, el binario del sistema de python). Acontinuacion, establece la ubicacion del **sys.prefix** y **sys.exec_prefix**  basados en esta ubicacion, omitiendo la parte "**bin**" del **path**.

El **path** ubicado en **sys.prefix**





## Glosario: 
- [Referencia para la definicion - eng][https://docs.python.org/3/library/venv.html#venv-def)
- [Modulos - programacion modular](https://en.wikipedia.org/wiki/Modular_programming)

## Referencias:
- [Python virtualenv primer](https://realpython.com/python-virtual-environments-a-primer/)
- [Documentation Oficial Python.org](https://docs.python.org/3/tutorial/venv.html)
- [Guide virtualenvs](https://docs.python-guide.org/dev/virtualenvs/)
- [Esp - wiki archlinux](https://wiki.archlinux.org/index.php/Python/Virtual_environment_(Espa%C3%B1ol))
- [Esp - Tutorial Python Virtualenv](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)
- [Documentation virtualenv.pypa](https://virtualenv.pypa.io/en/stable/)  
- [Pip - Pypi](https://pypi.org/project/pip/)
- [Documentation oficial pip](https://docs.python.org/3/installing/index.html)
- []()
- []()
- []()

