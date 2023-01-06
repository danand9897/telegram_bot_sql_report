# Telegram Bot Sql Report
## Instalación 
### Python

1. Descarga e instala python 3.9 (recomendado) desde el sitio oficial: https://www.python.org/downloads/
2. Abre la consola de comandos de tu sistema operativo (en Windows, puedes buscar "cmd" en el menú de Inicio).
3. Verifica que tienes instalada la versión correcta de Python, escribiendo: python3 --version
4. Si quieres usar un entorno virtual (recomendado), instala el módulo virtualenv: python3 -m pip install virtualenv
5. Crea un nuevo entorno virtual: python3 -m virtualenv nombre_de_mi_entorno
6. Activa el entorno virtual: en Windows: nombre_de_mi_entorno\Scripts\activate.bat
en Linux o MacOS: source nombre_de_mi_entorno/bin/activate
8. Ya estás listo para instalar este proyecto en Python con la versión 3.9.

### Git
1. Descarga e instala Git desde https://git-scm.com/downloads.
2. Abre una consola o terminal de comandos.
3. Haz clic derecho en una carpeta donde quieras clonar el repositorio y selecciona "Abrir ventana de comandos aquí" o "Abrir PowerShell aquí".
4. Escribe el comando "git clone" seguido de la URL del repositorio que quieres clonar. Por ejemplo, usando este repositorio:
git clone https://github.com/danand9897/telegram_bot_sql_report.git
5. Presiona Enter para clonar el repositorio.
6. El repositorio se clonará a una carpeta con el mismo nombre del repositorio en la ubicación actual. Si quieres clonar el repositorio a una ubicación específica, puedes especificarla después de la URL, separándolas con una barra diagonal. Por ejemplo:
git clone https://github.com/danand9897/telegram_bot_sql_report.git C:\rutadeseada\

### Esta aplicación (telegram_bot_sql_report)
1. Clonar el repositorio del proyecto en su computadora.
2. Crear un entorno virtual en su computadora. Esto se puede hacer con el comando "python -m venv nombre_entorno_virtual" en la consola de comandos o en la terminal.
3. Activar el entorno virtual con el comando "source nombre_entorno_virtual/bin/activate" (en Linux o Mac) o "nombre_entorno_virtual\Scripts\activate.bat" (en Windows).
4. Instalar las dependencias del proyecto con el comando "pip install -r requerimientos.txt". Esto instalará todas las librerías necesarias para que la aplicación funcione.
5. Ejecutar la aplicación con el comando "flask run". Por defecto, la aplicación se ejecuta en el puerto 5000, pero si dicho puerto está ocupado utilice el comando "flask run -p 5001" donde el último valor puede modificar por el puerto de su preferencia.
6. Estás listo para utilizar esta aplicación.
#### Es importante tener en cuenta que el entorno virtual debe ser creado y activado en la misma carpeta donde se encuentra el archivo "requerimientos.txt".