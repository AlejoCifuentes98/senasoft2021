
# Encuentra el Error

El logo que hicimos para el proyecto es:
![](https://github.com/AlejoCifuentes98/senasoft2021django/blob/frontend/static/img/logblancoblanco.png?raw=true)

##Que es CardBug
CardBug es un juego web de cartas que trata de adivinar quien fue culpable del del error, por eso se llama CardBug(Card es carta en ingles y Bug es error en ingles), es un juego casual de 4 jugadores 
##Que arquitectura
La arquitectura es cliente servidor

##Requerimientos
- asgiref==3.4.1
- Django==3.2.8
- Pillow==8.4.0
- pytz==2021.3
- sqlparse==0.4.2

##Como instalar
- Primero escribir esta line en el cmd: 
 docker build --tag Juego-CardBug
- despues que descargue las imagenes poner la siguiente linea:
 docker run --publish 8000:8000 Juego-CardBug
