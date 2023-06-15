# Rocketbot Stop Framework
  
Módulo para Rocketbot Stop Framework  

*Read this in other languages: [English](Manual_StopFramework.md), [Português](Manual_StopFramework.pr.md), [Español](Manual_StopFramework.es.md)*
  
![banner](imgs/Banner_StopFramework.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Login NOC
  
Inicie sesión en NOC utilizando unda de las opciones, API Key, archivo noc.ini o credenciales.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Servidor|URL del servidor a donde se conecta|https://roc.myrb.io/|
|Seleccione un metodo para conectarse al Orquestador|Opciones para iniciar sesión en R.O.C, se puede usar las credenciales del usuario, API Key o seleccionando archivo noc.ini|API Key|
|Asignar resultado a Variable|Variable donde se almacenara el estado de la conexion, devuelve True si es exitosa o False en el caso contrario|Variable|

### ¿Debe detenerse?
  
Verifica si el framework debe detenerse
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del proceso a revisar|Variable donde debe ingresarse el id del proceso a revisar si debe detenerse o no|J1H8K5DQ4XEW3M9R|
|Instancia del proceso|Variable donde debe ingresarse la instancia del proceso|a2f64d5d9988c|
|Asignar resultado a Variable|Variable donde se almacenara True o False dependiendo de si debe detenerse o no|Variable|
