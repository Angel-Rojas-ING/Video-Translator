## 🚀 Instalación Paso a Paso

### 1️⃣ Instala Python (si no lo tienes)
- **Descarga**: Visita [python.org](https://www.python.org/downloads/) y descarga Python 3.8 o superior.
- **Instala**: Durante la instalación, marca la casilla **"Add Python to PATH"**.
- **Verifica**: Abre una terminal y ejecuta:
  ```bash
  python --version
  ```
  Deberías ver algo como `Python 3.x.x`.

### 2️⃣ Clona el Repositorio
Abre una terminal y ejecuta:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 3️⃣ Ejecuta el Script como Administrador
- **Windows**: Busca "cmd" o "PowerShell", haz clic derecho y selecciona **"Ejecutar como administrador"**.
- Corre el script:
  ```bash
  python video_translator.py
  ```
- **Qué hará el script**:
  - Verifica si Python está instalado.
  - Instala FFmpeg si no está presente (descarga y agrega al PATH).
  - Instala dependencias de Python (`openai-whisper`, `deep-translator`, `gtts`, `tk`).

> 💡 **Nota**: Reinicia tu terminal o computadora después de la primera ejecución para que los cambios en el PATH surtan efecto.

---

## 🎬 Cómo Usarlo

1. **Selecciona tu Video**:
   - Al ejecutar el script, se abrirá un cuadro de diálogo.
   - Elige un video en formatos soportados: `.mp4`, `.mkv`, `.avi`, `.mov`.

2. **Espera el Proceso**:
   - El script realizará:
     1. Extracción del audio.
     2. Transcripción con Whisper.
     3. Traducción a español.
     4. Generación de audio sincronizado.
     5. Creación del video final.

3. **Obtén el Resultado**:
   - El video traducido aparecerá como `{nombre_del_video}_espanol.mp4` en el mismo directorio del original.

### 📋 Ejemplo Visual
```
Entrada: tutorial.mp4 (5 minutos en inglés)
↓
Procesamiento: [Transcripción → Traducción → Síntesis de voz → Sincronización]
↓
Salida: tutorial_espanol.mp4 (5 minutos con audio en español)
```

---

## ⚙️ Detalles Técnicos

### Tecnologías Utilizadas
- **Whisper (OpenAI)**: Transcripción precisa con marcas de tiempo para sincronización.
- **Google Translate (deep-translator)**: Traducción rápida y confiable.
- **gTTS (Google Text-to-Speech)**: Voz en español natural y ajustable.
- **FFmpeg**: Herramienta esencial para procesamiento de audio y video.
- **Python 3.8+**: Lenguaje base, con bibliotecas integradas como `tkinter`.

### Flujo del Proceso
1. **Extracción**: FFmpeg extrae el audio del video.
2. **Transcripción**: Whisper convierte el audio en texto segmentado.
3. **Traducción**: Deep-translator traduce cada segmento a español.
4. **Síntesis**: gTTS genera audio para cada segmento, ajustado a su duración original.
5. **Sincronización**: FFmpeg concatena los segmentos y los combina con el video.
6. **Limpieza**: Todos los archivos temporales se eliminan automáticamente.

---

## 🔧 Personalización

Puedes ajustar el script editando `video_translator.py`:
- **Modelo de Whisper**: Cambia `load_model("base")` a `load_model("medium")` para mayor precisión (más lento).
  ```python
  model = whisper.load_model("medium")
  ```
- **Directorio de Salida**: Modifica `output_dir` para guardar el video en otra ubicación.
  ```python
  output_dir = "C:/ruta/personalizada"
  ```

---

## 🌍 Contribuir

¡Tu ayuda es bienvenida! Para contribuir:
1. Haz un fork del repositorio.
2. Crea una rama:
   ```bash
   git checkout -b feature/nueva-funcion
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -m "Agregué nueva función"
   ```
4. Sube tu rama:
   ```bash
   git push origin feature/nueva-funcion
   ```
5. Abre un Pull Request en GitHub.

### Ideas para Contribuir
- Soporte para otros idiomas de entrada/salida.
- Mejora de la voz con otras APIs de TTS.
- Interfaz gráfica opcional.

---

## 📬 Soporte y Contacto

- **Issues**: Abre un issue en este repositorio si encuentras problemas o tienes sugerencias.
- **Correo**: Contacta al mantenedor en [tu_email@example.com](mailto:tu_email@example.com).

---

## 📜 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Siéntete libre de usarlo, modificarlo y distribuirlo según tus necesidades.

---

<div align="center">
  <h2>🎉 ¡Traduce tus videos y comparte tu contenido con el mundo!</h2>
  <p><em>Creado con ❤️ para la comunidad global.</em></p>
</div>
```


