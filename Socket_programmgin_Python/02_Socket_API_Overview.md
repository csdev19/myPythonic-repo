# Socket API Overview

El [modulo socket](https://docs.python.org/3/library/socket.html) de **Python** provee una interfaz de la [API de sockets de Berkeley](https://en.wikipedia.org/wiki/Berkeley_sockets). Este es el [modulo](https://www.iaa.csic.es/python/Iniciacion_Python_Modulos.pdf) que vamos a usar en este tutorial. 

Las **principales funciones y metodos** de la API de sockets son:

- socket()
- bind()
- listen()
- accept()
- connect()
- connect_ex()
- send()
- recv()
- close()

**Python** provee una API consistente y conveniente que **mapea** directamente estas **llamadas del sistema**, osea sus homologos en *C*. Veremos como estas son usadas juntas en la siguiente seccion.

Como parte de esta **libreria estandar**, Python cuenta con clases que se crean usando este tipo de **funciones de bajo nivel** de sockets. Aunque esto no sera cubierto en este tutorial (talvez investigue por mi cuenta luego), veremos el [modulo socketserver](https://docs.python.org/3/library/socketserver.html), un [framework](https://es.wikipedia.org/wiki/Framework) para **servidores de red** (network servers). HExisten mucho **modulos** disponibles que implementan [protocolos](https://es.wikipedia.org/wiki/Familia_de_protocolos_de_internet) de alto nivel como [HTTP](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto) y [SMTP](https://www.ibm.com/support/knowledgecenter/es/ssw_i5_54/rzair/rzairemcommnd.htm). Para un repaso rapido ver [Internet protocols and support ](https://docs.python.org/3/library/internet.html) es de Python.

