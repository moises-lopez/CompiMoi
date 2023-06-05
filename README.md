
# Quick Reference

## Instalación:

Descargar repositorio y descomprimir en una carpeta, asegurarse de tener python instalado y asignado en el path de la terminal
-   Agregar archivo txt a carpeta de test
-   Abrir una terminal
-   Navegar por la terminal a la carpeta donde se encuentra main.py
    
-   Correr el comando `python main.py archivo.txt`
    
-   La terminal correrá el archivo.txt, primero desplegará los cuádruplos generados y después le ejecución del programa.

CompiMoi sigue una estructura de programación convencional. Primero se define el nombre del programa, luego variables globales, módulos y al final una Main Function.

  

-   Todos los programas deben de empezar con la palabra reservada ‘Programa’ seguido del nombre del programa con un punto y coma.
    
-   Después se pueden definir variables globales, las variables siguen la siguiente estructura: var {tipo} id, id2, id3; Siendo los tipos posibles: int, float, boolean, string.
    
-   Por el momento nuestro programa se vería así

```
	Program Test
	var  int  a,b,c;
    var  float  a,b,c;
```

```
	Function  int  printVariable(int  aux){
		print(aux);
	}
```

  

-   Después se pueden o no declara módulos, los módulos contienen la siguiente estructura

-   De este ejemplo se puede apreciar que las funciones pueden tener un tipo de retorno como las variables, o bien se pueden dejar como void, los parámetros también pueden tener tipo, y podemos ver un ejemplo de print
    
-   A continuación se pueden declarar uno o más módulos, y al final un Main, que no es nada más que una función con algunos cambios, por ejemplo esta no recibe parámetros ni ocupa declarar un tipo de retorno

```
	Main(){
		var  int  aux;
		aux  =  0;
		print(aux);
	}
```

-   Estatutos no lineales: se cuenta con estructuras como while, y If-Elses, su estructura sería como la común en distintos lenguajes de programación: Aquí unos ejemplos
    

  
```
	var  boolean  found;
	found  =  True;
	while(found){
		found  =  False;
	};
	if(found){
		print("HOLA");
	}else{
		print("ADIOS");
	};
```



-   Leer de terminal

```
	var int a;
	read(a);
```
-   Inicializar array y asignar valor
    
```
	var  int  A[0  1,  2,  3];
	A[1,2]  =  10;

```
   

-   Los arrays contienen métodos especiales, contienen el método print() que imprime linealmente la matriz/array y los vectores de una dimensión contienen el método square que elevan al cuadrado cada elemento del vector
    

  ```
		var  int  A[0  1,  2,  3];
		A[1,2]  =  10;
		A.square();
		A.print();

  ```



  

Para más información favor de consultar sección de sintaxis.

##Bitácora
###Primer Avance
Se tomó tarea de little duck y se agregaron cosas extras:\
Sintaxis de funciones, parámetros de funciones, primera parte de arrays.\
Se cambió la forma que lee un archivo, ya acepta tabuladores, saltos de linea y espacios\
Por el momento chequea de buena manera el archivo de prueba que se incluye\

###Segundo Avance
Se agregó generación de cuádruplos para expresiones\
Cubo semántico\
Pila de operadores, operandos, tipos\
Y mucho research sobre cómo añadir puntos neurálgicos para analizar semánticamente\

###Tercer Avance
Se terminó y optimizó directorio de funciones\
Se agregó reglas semánticas faltantes de módulos y variables globales\
Se agregaron variables de current_type, current_function etc\

###Cuarto Avance
Se empezó semántica y generación de código de módulos,\
Se terminó de implemntar directorio de funciones para módulos\
Research de máquina virtual\

###Quinto Avance
Se terminó generación de código de módulos y de estatutos no lineales\
Se hizo primer draft de memoria virtual que está funcionando\
Se toman en cuenta constantes y se guardan en memoria virtual, se usa su dirección para operaciones

### Sexto Avance
Se terminó máquina virtual para expresiones, estatutos no lineales, functiones\
Se agregó acceso y declaración de Arrays\
Se terminó memoria de execución dise;o
