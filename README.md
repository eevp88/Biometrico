=====

Dispositivo  identificador de personas con RFID y Biometria.

INTRODUCCION
===============

En la búsqueda de soluciones más eficientes y a bajo costo, conocer de componentes
electrónicos como sensores (luminosidad, humedad, temperatura, etc.), micro
controladores, servo motores, pantallas LCD, entre otros, son herramientas poderosas
debido a las diferentes problemáticas que pueden dar solución, integrar estas tecnologías
dan un gran valor agregado a cualquier tipo proyecto, permitiendo solucionar en el
ambiente del usuario diferentes problemáticas de manera útil y efectiva.
Para lograr que este dispositivo interactúe con el ambiente donde está inmerso y se
comunique con una base de datos de manera local o de forma remota a través de Internet se
hace necesario el desarrollo de piezas de software, capaz de procesar la información
recolectada, ya sea en tiempo real o cuando sea necesario, dando de esta manera las
funcionalidades necesaria para cubrir las necesidades demandadas.
Para realizar este proyecto se utilizara plataformas de Open Hardware, lo que nos
brinda la libertada de construir un dispositivo capaz integrar cualquier tipo de sensor
estándar, lo cual nos permite generar el conocimiento para manipular cualquier tipo de
sensor.


OBJETIVOS GENERALES Y ESPECIFICOS
==================================== 
  Objetivo General
------------------------------------
Construir un dispositivo capas de cuantificar y controlar el flujo de personas de algún
espacio físico y con esto gestionar su mantención de mejor manera. El dispositivo debe ser
capaz de integrar distintos sensores de reconocimientos (RFID y lector biométrico),
comunicarse con un servidor para poder guardar la información en una base de datos y
generar algunos reportes.

  Objetivos Específicos
-------------------------------------
  1. Estudiar las diferentes tecnologías de Open Hardware relevantes para este
     proyecto, incluyendo sensores (RFID y lector biométrico) y micro
     controlador.
    
  2. Definir arquitectura del sistema que permita la escalabilidad e integración
     con otros sistemas, definiendo estándares de comunicación entre otros.
    
  3. Seleccionar la plataforma de Open Hardware y sensores atingentes al
     proyecto, diseñar piezas de software que permita comunicar el dispositivo
     con la base de datos.
   
  4. Modelar e implementar la base de datos que permita manipular la
     información eficientemente.
   
  5. Entender nuevas tecnologías de programación web para implementar un
     prototipo de software de administrador de espacios.
     
  6. Realizar pruebas evaluación del funcionamiento del sistema.


ESTADO ACTUAL DEL PROYECTO
============================

  El proyecto esta en la fase de estudio de  plataformas Open Hardware(sensor biometrico esta dando problemas con la captura de la imagen de  la huella dactilar no esta implementada la funcion para arduino ethernet y mega trabajo en eso)
  Descartada la plataforma Arduino para la extracion de la imagen, estudiando y trabajando en la plataforma BeagleBone Black(espero llegar al objetivo).
