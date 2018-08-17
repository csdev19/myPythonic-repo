# Echo Server

Aqui esta el server, **echo-server.py**:

```python
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind( (HOST, PORT) )
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
```

Repasemos cada llamada **API** y veamos que esta pasando.

**socket.socket()** crea un objeto socket que soporta el [context manager type](https://docs.python.org/3/reference/datamodel.html#context-managers), entonces podemos usarlo en un [with statement](https://docs.python.org/3/reference/compound_stmts.html#with). No es necesario llamar a **s.close()**:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    pass # Use the socket object without calling s.close()
```

Los argumentos pasados a [socket()](https://docs.python.org/3/library/socket.html#socket.socket) especifican la [address family](https://realpython.com/python-sockets/#socket-address-families) y tipo de socket.AF_INET es la familia de internet para [IPv4](https://en.wikipedia.org/wiki/IPv4).
SOCK_STREAM es el tipo de socket para [TCP](https://realpython.com/python-sockets/#tcp-sockets), el protocolo que puede ser usado para transportar nuestros mensajes en la red.

**bind()** es usado para asociar el **socket** con una interfaz de red especifica y un numero de puerto: 

```python
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# ... 

s.bind( (HOST, PORT) )
```

Los valores pasados hacia **bind()** depende de la [familia de direcciones](https://realpython.com/python-sockets/#socket-address-families) del socket. En este ejemplo, usamos **socket.AD_INET(IPv4)**. Entonces este espera una **tupla** de dos elementos: (host, port).

### Host
**Host** puede ser un **hostname**, **direccion IP**, o **un string vacio**. Si la direccion IP es usada, **host** deberia ser un string de direccion **IPv4-formatted**. La **direccion IP 127.0.0.1** es el estandar de la direccion **IPv4** para la interfaz [loopback](https://en.wikipedia.org/wiki/Localhost), por lo tanto, solo procesos en el host que podria conectarse al servidor. Si es que pasamos como argumento un string vacio, el servidor **aceptara conexiones de todas las discponibles en la interfaz IPv4**

### Port

**Port** suele se un integer desde **1-65535** (0 es resevado). Es el numero de puerto [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_ports) para aceptar conexiones de clientes. Algunos sistemas pueden requerir **privilegios de superusuario** es el puerto es <**1024**.

Aqui una nota para usar hostnames con **bind()**: 

“If you use a hostname in the host portion of IPv4/v6 socket address, the program may show a non-deterministic behavior, as Python uses the first address returned from the DNS resolution. The socket address will be resolved differently into an actual IPv4/v6 address, depending on the results from DNS resolution and/or the host configuration. For deterministic behavior use a numeric address in host portion.”[Link](https://docs.python.org/3/library/socket.html)

Se discutira mas adelante en [using hostnames](https://realpython.com/python-sockets/#using-hostnames), pero vale la pena mencionarlo aqui. Por ahora, solo entender esto cuando usemos hostname, podremos ver diferentes resultados dependiendo de que retorne desde el nombre de la resolucion del proceso.

Esto podria ser cualquier cosa. La primera vez que corres tu aplicacion, podria ser la **direccion 10.1.2.3**. La siguiente vez seria una direccion diferente, **192.168.0.1**. La tercera vez, podria ser **172.16.7.8** y asi.

Continuando con el ejemplo del servidor, **listen()** habilita a un servidor para **accept()** (aceptar) conexion. Esto hace que un socket **escuche("listenning")**:
```python
s.listen()
conn, addr = s.accept()
```

**listen()** tiene un parametro "**backlog**"(reserva). El cual especifica el numero de conexiones **no aceptadas** que el sistema permitira antes de rechazar una nueva conexion. **Desde Python 3.5**, es opcional. Si no especificamos, se escojera un **backlog por defecto**.

Si es servidor recibe demasiadas solicitudes de conexiones simultaneamente, incrementar el valor del **backlog**(retraso) podria ayudar estableciendo la longitud maxima de conexiones pendientes en la cola. *El valor maximo depende del sistema*. Por ejemplo en **Linux**, podemos ver [/proc/sys/net/core/somaxconn](https://serverfault.com/questions/518862/will-increasing-net-core-somaxconn-make-a-difference/519152).

**accept()** [blocks (bloquea)](https://realpython.com/python-sockets/#blocking-calls) y espera una conexion entrante. Cuando un cliente se conecta, retorna un **nuevo objeto socket** representando la conexion y un tupla sosteniendo la direccion del cliente. La **tupla** contenera (**host, port**) para conexiones **IPv4** o (**host, port, flowinfo, scopeid**) para **IPv6**. Ver [Socket Address Families](https://realpython.com/python-sockets/#socket-address-families) en la seccion de referencia para detalles en los **valores de las tuplas**.

Una cosa que es imprescindible comprender es que ahora tenemos un **nuevo objeto socket** de **accept()**. Esto es importante desde que el **socket** que usaremos para comunicarnos con el cliente. Es distinto del socket de escucha que el de servidor esta utlizando para aceptar nuevas conexiones: 

```python
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
```

Despues de obtener el **socket del cliente (conn)** de **accept()**, un bucle infinito es usado para repetir las [blocking calls](https://realpython.com/python-sockets/#blocking-calls) hacia **conn.recv()**. Esto lee cualquier dato que el cliente envia y **echoes** (lo repite) usando **conn.sendall()**.

Si **conn.recv()** retorna un objeto [bytes](https://docs.python.org/3/library/stdtypes.html#bytes-objects) vacio, **b ''**, entonces el cliente cierra la conexion y el bucle se termina. La sentencia **with** es usada con **conn** para cerrar automaticamente el **socket** al final del bloque.
