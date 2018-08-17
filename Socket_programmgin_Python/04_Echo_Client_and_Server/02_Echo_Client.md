# Echo Client

Ahora vamos a ver el cliente, **echo-client.py**:

```python
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
```

En comparacion al servidor, el cliente es bastante simple. Este crea un **objeto socket**, que se conecta al servidor y llama a  **s.sendall()** para enviar este mensaje. Para finalizar, llama a **s.recv()** para leer lo que se recibe del servidor y luego imprimirlo.
