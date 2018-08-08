# Background (Historia)

Los **Sockets** tienen una larga historia. Su uso se originó con [ARPANET](https://en.wikipedia.org/wiki/Network_socket#History) en 1971 y más tarde se convirtió en API en el sistema operativo Berkeley Software Distribution (BSD) lanzado en 1983 llamado [sockets de Berkeley](https://en.wikipedia.org/wiki/Berkeley_sockets).

Cuando Internet despegó en la década de 1990 con la World Wide Web, también lo hizo la programación en red. Los servidores web y los navegadores no fueron las únicas aplicaciones que aprovecharon las redes recién conectadas y el uso de **sockets**. Las aplicaciones **cliente-servidor** de todos los tipos y tamaños se utilizaron ampliamente.

Hoy, aunque los protocolos subyacentes utilizados por la API de socket han evolucionado a lo largo de los años, y hemos visto otros nuevos, la API de bajo nivel se ha mantenido igual.

El tipo más común de aplicaciones de socket son aplicaciones cliente-servidor, donde un lado actúa como el servidor y espera las conexiones de los clientes. Este es el tipo de aplicación que voy a cubrir en este tutorial. Más específicamente, veremos la API de socket para [Internet sockets](https://en.wikipedia.org/wiki/Berkeley_sockets), a veces llamados conectores de Berkeley o BSD. También hay [sockets de dominio Unix](https://en.wikipedia.org/wiki/Unix_domain_socket), que solo se pueden usar para comunicarse entre procesos en el mismo host.