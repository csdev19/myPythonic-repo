# TCP Sockets

Como podran ver, vamos a crear un objeto **socket** usando **socket.socket()** y especificando el tipo de socket como **socket.SOCK_STREAM**. Cuando hacemos esto, el **protocolo por defecto** que es usado es el [protocolo de control de transmicion](https://es.wikipedia.org/wiki/Protocolo_de_control_de_transmisi%C3%B3n) o [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol). Esto es algo bueno que este por defecto y probablemente es lo que queremos.

Porque deberiamos usar **TCP** ? 
- **Es confiable**: Los paquetes **caidos** por la red son detectados y retransmitidos por el remitente.
- **Tiene un orden en la entrega de datos**: Los datos son leidos por la aplicacion en el orden en que fueron escritas por el remitente.

En constrate, los sockets del [protocolo de datagramas de usuario](https://es.wikipedia.org/wiki/Protocolo_de_datagramas_de_usuario)([UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol)) creados con **socket.SOCK_DGRAM** no son confiables, y los datos leidos por el receptor pueden estar desordenados por las escrituras del remitente.

Porque esto es importante ?  La red es el mejor esfuerzo de sistema de delivery. No hay garantia que tus datos puedan alcazar su destino o que puedas recibir lo que se te ha enviado.

Los dispositivos de red (por ejemplo, **routers** y **switches**), tiene un **ancho de banda finito dispoible** y sus propias limitaciones inherentes al sistema. Tienen **CPU**, **memoria**, **buses** y **buffers** de paquetes de interfaz, justo como nuestros clientes y servidores. **TCP** alivia tener que preocuparse por la [perdida de paquetes](https://en.wikipedia.org/wiki/Packet_loss), los datos que llegan fuera de orden, y muchas otras cosas que invariablemente suceden cuando se esta comunicando a traves de una red.

En el diagrama del siguiente [link](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg), vamos a ver la secuencia de llamadas a la API de **socket** y flujo de datos para **TCP**.
[Fuente - internet socket basic diagram](https://commons.wikimedia.org/wiki/File:InternetSocketBasicDiagram_zhtw.png)

La columna **izquierda** representa al servidor. Y en la **derecha** el lado del cliente.

Empezando desde **columna superior izquierda**, podemos notar que las llamadas **API** que realiza el servidor para configurar un socket de "listening" (escucha).

- socket()
- bind()
- listen()
- accept()

Un **socket de escucha** es justamente lo que suena. Escucha las conexiones de los clientes. Cuando un cliente se conecta, el servidor llamada **accept()** para aceptar, o completar la conexion.

El cliente llamada **connect()** para estableces conexion con el servidor (si es bastante redundante, aunque me gusta llamarlo intuitivo) e iniciar un **handshake** de 3 vias. El paso de **handshake** es importante, ya que garantiza que cada lado de la conexion sea alcanable en la red, en otras palabras el cliente puede llegar al servidor y viceversa. Puede ser que solo un **host**, **cliente** o **servidor** puede llegar al otro.

En el medio de esta seccion de ida y vuelta, donde los datos son intercambiados entre el cliente y el servidor usando llamadas a **send()** y **recv()**.

En la parte inferior, el cliente y el servidor **close()** (cierran) sus respectivos **sockets**.
