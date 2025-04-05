
```markdown
# 🎥 Video Translator

![Banner](https://img.shields.io/badge/Status-Actively%20Developed-brightgreen)  
**Traduce y sincroniza el audio de tus videos de inglés a español con facilidad.**

---

## 🌟 Descripción

**Video Translator** es una herramienta poderosa y fácil de usar que transforma tus videos al traducir automáticamente el audio de inglés a español y sincronizarlo con el contenido visual. Utiliza tecnologías avanzadas como Whisper para la transcripción, Google Translate para la traducción y gTTS para generar una voz en español natural. El resultado es un nuevo video con el audio traducido, listo para compartir o disfrutar.

Perfecto para creadores de contenido, educadores, o cualquier persona que desee hacer sus videos accesibles en español sin esfuerzo manual.

---

## ✨ Características

- **Transcripción Automática**: Convierte el audio en texto usando Whisper de OpenAI.
- **Traducción Precisa**: Traduce de inglés a español con Google Translate.
- **Sincronización Inteligente**: Ajusta el audio generado para alinearse con el video original.
- **Instalación Sencilla**: Instala FFmpeg y todas las dependencias de Python automáticamente.
- **Limpieza Completa**: Elimina todos los archivos intermedios, dejando solo el video final.
- **Portátil**: Guarda el video traducido en el mismo directorio que el original.

---

## 🚀 Requisitos

- **Sistema Operativo**: Windows (para la instalación automática de FFmpeg).
- **Privilegios**: Ejecución como administrador (para instalar FFmpeg).
- **Internet**: Necesario para descargar FFmpeg y usar servicios de traducción.

---

## 🛠️ Instalación

### 1. Instala Python (si no lo tienes)
- Descarga Python 3.8 o superior desde [python.org](https://www.python.org/downloads/).
- Asegúrate de marcar "Add Python to PATH" durante la instalación.
- Verifica con:
  ```bash
  python --version
  ```

### 2. Clona el Repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 3. Ejecuta el Script
- Abre una terminal como administrador (en Windows, busca "cmd" o "PowerShell", haz clic derecho y selecciona "Ejecutar como administrador").
- Corre el script:
  ```bash
  python video_translator.py
  ```
- El script instalará FFmpeg y las dependencias de Python si no están presentes.

> **Nota**: Reinicia tu terminal o computadora después de la primera ejecución para que los cambios en el PATH surtan efecto.

---

## 🎬 Uso

1. **Selecciona un Video**: Cuando ejecutes el script, se abrirá un cuadro de diálogo. Elige el video que deseas traducir (formatos soportados: `.mp4`, `.mkv`, `.avi`, `.mov`).
2. **Espera el Proceso**: El script transcribirá, traducirá y generará un nuevo video automáticamente.
3. **Encuentra el Resultado**: El video traducido aparecerá en el mismo directorio que el original con el sufijo `_espanol` (ejemplo: `mi_video_espanol.mp4`).

---

## 📋 Ejemplo

**Entrada**: `tutorial.mp4` (un video en inglés de 5 minutos).  
**Salida**: `tutorial_espanol.mp4` (el mismo video con audio en español sincronizado).  

---

## 🛠️ Tecnologías Utilizadas

- **Whisper (OpenAI)**: Transcripción de audio a texto.
- **Google Translate (via deep-translator)**: Traducción de inglés a español.
- **gTTS**: Generación de voz en español.
- **FFmpeg**: Procesamiento de audio y video.
- **Python**: Lenguaje principal del script.

---

## ⚙️ Notas Importantes

- **Conexión a Internet**: Requerida para descargar FFmpeg y usar Google Translate.
- **Duración del Video**: Videos largos pueden tardar más en procesarse, dependiendo de tu hardware.
- **Precisión**: Para mejores resultados en la transcripción, considera usar el modelo `medium` de Whisper (cambia `load_model("base")` a `load_model("medium")` en el código, aunque será más lento).

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el script:
1. Haz un fork del repositorio.
2. Crea una rama (`git checkout -b feature/nueva-funcion`).
3. Haz tus cambios y haz commit (`git commit -m "Agregué nueva función"`).
4. Sube tus cambios (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

---

## 📬 Contacto

Si tienes preguntas o necesitas ayuda, abre un issue en este repositorio o contacta al mantenedor en [tu_email@example.com](mailto:tu_email@example.com).

---

## 🌐 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE). Siéntete libre de usarlo y modificarlo según tus necesidades.

---

**¡Disfruta traduciendo tus videos con Video Translator!**  
_Creado con ❤️ para la comunidad._
```


