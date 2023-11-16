# ParcialMutantes
* Nombre y Apellido: Angelo Gabino Terranova
* Legajo: 51652 
* Email: gabino44terranova@gmail.com

## El proyecto trata de:

El proyecto trata de desarrollar un sistema de verificacion de secuencias. Donde se valida si existe el de ADN de un "Mutante" o no, mediante:

- Analizar una matriz de ADN de 6x6, compuesta por las bases nitrogenadas A, T, C, y G.
- Donde una secuencia de ADN se considera mutante si hay más de una secuencia de cuatro letras iguales en cualquier dirección (horizontal, vertical u oblicua).

El código debe realizar tres funciones principales: recopilar y validar las secuencias de ADN del usuario, analizar la matriz en busca de secuencias repetidas y determinar si la muestra corresponde a un mutante basándose en este análisis.

## Como se resuelve:

Para la de detección de mutantes en secuencias de ADN, se estructura en torno a tres funciones principales: "mutante", "ingresar_secuencias", y "main":

- Función ingresar_secuencias: entrada de datos del usuario. Solicita al usuario que ingrese seis secuencias de ADN, cada una compuesta por seis caracteres que representan las bases nitrogenadas (A, T, C, G). Durante este proceso, la función verifica que cada secuencia tenga la longitud correcta y contenga solo los caracteres válidos. Esto asegura que los datos de ADN ingresados sean adecuados para el análisis posterior.

- Función mutante: recibe la matriz de ADN ingresada y la examina en busca de secuencias mutantes. Lo hace iterando a través de las filas, columnas y diagonales de la matriz, buscando secuencias de cuatro bases nitrogenadas idénticas consecutivas. Si encuentra más de una de estas secuencias en cualquier dirección, determina que el ADN pertenece a un mutante. Este enfoque de búsqueda exhaustiva garantiza que todas las posibles secuencias mutantes sean identificadas.

- Función main: incia el proceso llamando a ingresar_secuencias para recopilar la matriz de ADN del usuario. Luego, pasa esta matriz a la función mutante para realizar el análisis. Basándose en el resultado devuelto por mutante, main informa al usuario si la secuencia de ADN analizada pertenece a un mutante o no, proporcionando un mensaje apropiado en cada caso.

## Como correrlo:

1. Para ejecutar el código en Visual Studio Code (VS Code), primero se debe instalar tanto VS Code como Python, asegurándote de agregar Python al PATH durante la instalación. 
2. Luego, abre VS Code y agrega la extensión de Python. 
3. Crea o abre un archivo .py y pega el código en él.
4. Ejecuta el script usando el botón de ejecución (triángulo verde) en la parte superior derecha del editor.

## CASOS DE PRUEBA:

Si se carga:

ATGCGA
CAGTGC
TTATGT
AGAAGG
CCCTTA
TCACCG

El resultado es "¡SE HA DETECTADO UN MUTANTE!".

Y si se carga:

CGTAGC
ATGCGA
TTATGT
AGAAGG
CCCATA
TCACTG

El resultado es que NO es mutante.