#!/bin/bash

# COMANDOS BÁSICOS (DIRECTORIOS Y FICHEROS)
pwd # Devuelve la ruta absoluta del directorio en el que se encuentra la shell
# cd es "Change Directory", sirve para cambiar la shell a un directorio 
cd .            # El directorio . hace referencia al directorio en el que ya estás
cd ..           # El directorio .. hace referencia al directorio de nivel superior
cd ../../../ruta/relativa/de/directorio
cd ruta/relativa/de/directorio
cd /ruta/absoluta/de/directorio
mkdir nuevo     # Crea directorio llamado nuevo en el directorio actual, equivalente a mkdir ./nuevo
mkdir ../nuevo  # Crea directorio llamado nuevo en el directorio superior
rmdir nuevo     # Elimina el directorio nuevo. Ojo, sólo funciona cuando están vacíos
touch fichero   # Crea un nuevo fichero vacío (empty) en el directorio actutual
nano fichero    # Accede a herramienta nano para editar el contenido del fichero
cat fichero     # Muestra como salida de comando el contenido del fichero
rm fichero      # Elimina el fichero
rm -r ruta/directorio # Elimina recursivamente (-r) todo lo que contiene un directorio, éste incluido
# ls ("list") muestra el contenido de un directorio, tanto sus ficheros como subdirectorios
ls  
ls .
ls ..
ls /ruta/directorio
ls -l   # Contenido en forma de listado
ls -a   # Incluye en la salida del comando los archivos ocultos
ls -la  # Combina los parámetros de listado y de archivos ocultos

# COMANDOS DE SHELL/TERMINAL
clear # Limpia la terminal
exit # Sale de la sesión actual (si se ha iniciado sesión en un usuario saldrá de ésta, si no, cerrará la terminal)
history # Muestra el histórico de comandos de ese usuario/sesión

# ADMINISTRACIÓN
su # Inicio de sesión de root en la shell
sudo $comando # Llama al comando con privilegios de administrador
sudo su # Accede al usuario root mediante sudo, es decir, sin indicar la contraseña de root sino la del usuario que está en sudoers
passwd # Cambia la clave del usuario iniciado en la shell
passwd $usuario # Cambia la clave del usuario pasado (hay que tener permisos sobre ese usuario para ello)
poweroff # Apaga el sistema
reboot # Reinicia el sistema
shutdown now # Apaga el ordenador inmediatamente (shutdown envía señal al demonio init para indicarle el apagado)
shutdown 14:30 # Programa apagado para las 14:30
shutdown -r now # Reinicia el ordenador inmediatamente
shutdown -r +1 "El sistema se apagará" # Programación de reinicio en un minuto con mensaje
shutdown -c # Cancela todas las programaciones de shutdown
halt # Apagado de sistema del tipo "detención". Detiene todas las funciones de la CPU pero mantiene encendido el PC (útil para realizar mantenimientos de bajo nivel)

# METACOMANDOS
whatis $comando # (¿qué es?) muestra ayuda sobre un comando desconocido
man $comando    # Muestra el manual del comando pasado
cmp
comm
diff
cut