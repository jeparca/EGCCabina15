# EGCCabina15
Repositorio para la cabina de votación administrador por todos los coordinadores de todos los subsistemas de Agora@US

Para el correcto funcionamiento del subsistema que ha sido adaptado a Jython, el cual generará un WAR que se ejecutará bajo un servidor Tomcat, hace falta tener un entorno con:

- Jython 2.7
- Django 1.8.3
- Django-Jython 1.8.0b3
- Django Rest Framework 2.4.3
- Django Cors Headers 0.13
- Requests 2.4.3

Además, para la generación del WAR hace falta tener un entorno basado en Linux (por distintos fallos que presenta Jython) con Java 7.
Primero hay que añadir al classpath la liberia para sqlite: export CLASSPATH="$CLASSPATH:/path/to/driver.jar"
El comando para la generación es: jython manage.py buildwar