echo # Video Translator > README.md
echo. >> README.md
echo ![Banner](https://img.shields.io/badge/Status-Actively%20Developed-brightgreen) >> README.md
echo **Traduce y sincroniza el audio de tus videos de inglés a español con facilidad.** >> README.md
echo. >> README.md
echo ## Descripción >> README.md
echo. >> README.md
echo **Video Translator** es una herramienta poderosa y fácil de usar que transforma tus videos al traducir automáticamente el audio de inglés a español y sincronizarlo con el contenido visual. Utiliza tecnologías avanzadas como Whisper para la transcripción, Google Translate para la traducción y gTTS para generar una voz en español natural. El resultado es un nuevo video con el audio traducido, listo para compartir o disfrutar. >> README.md
echo. >> README.md
echo Perfecto para creadores de contenido, educadores, o cualquier persona que desee hacer sus videos accesibles en español sin esfuerzo manual. >> README.md
echo. >> README.md
echo ## Características >> README.md
echo. >> README.md
echo - **Transcripción Automática**: Convierte el audio en texto usando Whisper de OpenAI. >> README.md
echo - **Traducción Precisa**: Traduce de inglés a español con Google Translate. >> README.md
echo - **Sincronización Inteligente**: Ajusta el audio generado para alinearse con el video original. >> README.md
echo - **Instalación Sencilla**: Instala FFmpeg y todas las dependencias de Python automáticamente. >> README.md
echo - **Limpieza Completa**: Elimina todos los archivos intermedios, dejando solo el video final. >> README.md
echo - **Portátil**: Guarda el video traducido en el mismo directorio que el original. >> README.md
echo. >> README.md
echo ## Requisitos >> README.md
echo. >> README.md
echo - **Sistema Operativo**: Windows (para instalación automática de FFmpeg). >> README.md
echo - **Privilegios**: Ejecución como administrador (para instalar FFmpeg). >> README.md
echo - **Internet**: Necesario para descargar FFmpeg y usar servicios de traducción. >> README.md
echo. >> README.md
echo ## Instalación >> README.md
echo. >> README.md
echo ### 1. Instala Python (si no lo tienes) >> README.md
echo - Descarga Python 3.8 o superior desde [python.org](https://www.python.org/downloads/). >> README.md
echo - Asegúrate de marcar "Add Python to PATH" durante la instalación. >> README.md
echo - Verifica con: >> README.md
echo ```bash >> README.md
echo python --version >> README.md
echo ``` >> README.md
echo. >> README.md
echo ### 2. Clona el Repositorio >> README.md
echo ```bash >> README.md
echo git clone https://github.com/tu_usuario/tu_repositorio.git >> README.md
echo cd tu_repositorio >> README.md
echo ``` >> README.md
echo. >> README.md
echo ### 3. Ejecuta el Script >> README.md
echo - Abre una terminal como administrador (en Windows, busca "cmd" o "PowerShell", haz clic derecho y selecciona "Ejecutar como administrador"). >> README.md
echo - Corre el script: >> README.md
echo ```bash >> README.md
echo python video_translator.py >> README.md
echo ``` >> README.md
echo - Si FFmpeg no está instalado, el script lo instalará. >> README.md
echo - Las dependencias de Python se instalarán automáticamente. >> README.md
echo. >> README.md
echo > **Nota**: Reinicia tu terminal o computadora después de la primera ejecución para que los cambios en el PATH surtan efecto. >> README.md
echo. >> README.md
echo ## Uso >> README.md
echo. >> README.md
echo - Selecciona un video cuando se abra el cuadro de diálogo. >> README.md
echo - El script generará `{nombre_del_video}_espanol.mp4` en el mismo directorio del video original. >> README.md
echo. >> README.md
echo ## Ejemplo >> README.md
echo. >> README.md
echo **Entrada**: `tutorial.mp4` (un video en inglés de 5 minutos).  >> README.md
echo **Salida**: `tutorial_espanol.mp4` (el mismo video con audio en español sincronizado).  >> README.md
echo. >> README.md
echo ## Tecnologías Utilizadas >> README.md
echo. >> README.md
echo - **Whisper (OpenAI)**: Transcripción de audio a texto. >> README.md
echo - **Google Translate (via deep-translator)**: Traducción de inglés a español. >> README.md
echo - **gTTS**: Generación de voz en español. >> README.md
echo - **FFmpeg**: Procesamiento de audio y video. >> README.md
echo - **Python**: Lenguaje principal del script. >> README.md
echo. >> README.md
echo ## Notas Importantes >> README.md
echo. >> README.md
echo - **Conexión a Internet**: Requerida para descargar FFmpeg y usar Google Translate. >> README.md
echo - **Duración del Video**: Videos largos pueden tardar más en procesarse, dependiendo de tu hardware. >> README.md
echo - **Precisión**: Para mejores resultados en la transcripción, considera usar el modelo `medium` de Whisper (cambia `load_model("base")` a `load_model("medium")` en el código, aunque será más lento). >> README.md
echo. >> README.md
echo ## Contribuir >> README.md
echo. >> README.md
echo ¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script: >> README.md
echo 1. Haz un fork del repositorio. >> README.md
echo 2. Crea una rama (`git checkout -b feature/nueva-funcion`). >> README.md
echo 3. Haz tus cambios y haz commit (`git commit -m "Agregué nueva función"`). >> README.md
echo 4. Sube tus cambios (`git push origin feature/nueva-funcion`). >> README.md
echo 5. Abre un Pull Request. >> README.md
echo. >> README.md
echo ## Contacto >> README.md
echo. >> README.md
echo Si tienes preguntas o necesitas ayuda, abre un issue en este repositorio o contacta al mantenedor en [tu_email@example.com](mailto:tu_email@example.com). >> README.md
echo. >> README.md
echo ## Licencia >> README.md
echo. >> README.md
echo Este proyecto está bajo la [Licencia MIT](LICENSE). Siéntete libre de usarlo y modificarlo según tus necesidades. >> README.md
echo. >> README.md
echo **¡Disfruta traduciendo tus videos con Video Translator!** >> README.md
echo _Creado con ❤️ para la comunidad._ >> README.md
