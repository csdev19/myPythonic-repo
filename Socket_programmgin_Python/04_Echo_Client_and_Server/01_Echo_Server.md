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

















