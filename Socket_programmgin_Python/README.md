# Socket Programming in Python

## Table of Contents

- [Background]()
- [Socket API Overview]()
- [TCP Sockets]()
- [Echo Client and Server]()
    - [Echo Server]()
    - [Echo Client]()
    - [Running the Echo Client and Server]()
    - [Viewing Socket State]()
- [Communication Breakdown]()
- [Handling Multiple Connections]()
- [Multi-Connection Client and Server ]()
    - [Multi-Connection Server]()
    - [Multi-Connection Client]()
    - [Running the Multi-Connection Client and Server]()
- [Application Client and Server]()
    - [Application Protocol Header]()
    - [Sending an Application Message]()
    - [Application Message Class]()
    - [Running the Application Client and Server]()
- [Troubleshooting]()
    - [ping]()
    - [netstat]()
    - [Windows]()
    - [Wireshark]()
- [Reference]()
    - [Python Documentation]()
    - [Errors]()
    - [Socket Address Families]()
    - [Using Hostnames]()
    - [Blocking Calls]()
    - [Closing Connections]()
    - [Byte Endianness]()
- [Conclusion]()


## Introduction


### Que son los SOCKETS ? (SOCKET = ENCHUFE)

[Socket de internet](https://es.wikipedia.org/wiki/Socket_de_Internet), Socket designa un concepto abstracto por el cual dos programas (posiblemente situados en computadoras distintas) pueden intercambiar cualquier flujo de datos, generalmente de manera fiable y ordenada.

El término socket es también usado como el nombre de una interfaz de programación de aplicaciones ([API](https://ed.team/blog/que-es-una-api)) para la [familia de protocolos de Internet](https://es.wikipedia.org/wiki/Modelo_TCP/IP) o [TCP/IP](https://es.wikipedia.org/wiki/Modelo_TCP/IP), provista usualmente por el sistema operativo.

Los sockets de Internet constituyen el mecanismo para la entrega de paquetes de datos provenientes de la tarjeta de red a los procesos o hilos apropiados. Un socket queda definido por un par de [direcciones IP](https://es.wikipedia.org/wiki/Direcci%C3%B3n_IP) local y remota, un protocolo de transporte y un par de números de puerto local y remoto. 

Para mas informacion consultar los links. 

### Definition Initial

Ahora, **Sockets** y **Socket API** es usado para **enviar mensajes** a traves de la red (**network**). Estos proveen de [inter-process communication(IPC)](https://en.wikipedia.org/wiki/Inter-process_communication) o en español [Comunicación entre procesos](https://es.wikipedia.org/wiki/Comunicación_entre_procesos). La red puede ser una red local lógica para la computadora, o una que está físicamente conectada a una red externa, con sus propias conexiones a otras redes. El ejemplo más obvio es Internet, a la que se conecta a través de su [ISP](https://es.wikipedia.org/wiki/Proveedor_de_servicios_de_Internet).

Este **tutorial** tiene 3 diferentes iteraciones para construir un **socket server** y un **client(cliente)** con **Python**:

1. Empezaremos el tutorial observando un **simple socket server** y **client(cliente)**.
2. Una vez hayamos visto la **API** y como las cosas funcionan en el ejemplo inicial, veremos una version mejorada que maneja **multiples conexiones simultaneamente**.
3. Finalmente, podremos avanzar hasta construir un servidor de ejemplo y un cliente que tengan las funciones como una completa aplicacion de **socket**, con sus propios y customizadas cabeceras y contenido.

Al final de este tutorial, podremos entender como usar las principales funciones y metodos, de los [modulos Socket](https://docs.python.org/3/library/socket.html) de Python para escribir nuestras propias aplicaciones **cliente-servidor**. Esto incluye el como usar una **clase personalizada** para enviar mensajes y datos entre puntos finales (**endpoints**) sobre los cuales podemos construir y utilizar para nstras propias aplicaciones.

**Networking** y **Sockets** son temas grandes. Literamente se han escrito varios volumenes acerca de estos. Si es la primera vez que lees sobre **sockets** o **networking**, es normal que te pierdas o que sientas frustracion. 

Tambien es mi primera vez en este tema, asi que vamos a seguir por este viaje juntos XD. Tratare de documentar todo lo que encuentre cuando me pierda o no entienda nada, veamos que resulta de esto.



## Creditos: 

- [REAL PYTHON - SOCKETS](https://realpython.com/python-sockets/#background)
- 
