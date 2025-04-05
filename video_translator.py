import os
import sys
import requests
import zipfile
import subprocess
import shutil
from pathlib import Path
import tempfile
from tkinter import Tk, filedialog, messagebox

# URL de descarga de FFmpeg
FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

def check_python():
    """Verifica si Python está instalado."""
    try:
        subprocess.run([sys.executable, "--version"], check=True, capture_output=True, text=True)
        print(f"Python está instalado: {sys.version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Python no está instalado o no se encuentra en el PATH.")
        print("Por favor, instala Python 3.8 o superior desde https://www.python.org/downloads/")
        print("Luego, vuelve a ejecutar este script.")
        return False

def download_file(url, dest):
    """Descarga un archivo desde una URL."""
    print(f"Descargando {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Descarga completada.")

def extract_zip(zip_path, extract_to):
    """Extrae un archivo ZIP."""
    print(f"Extrayendo {zip_path} a {extract_to}...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print("Extracción completada.")

def add_to_path(directory):
    """Agrega un directorio al PATH del sistema."""
    print(f"Agregando {directory} al PATH del sistema...")
    current_path = os.environ.get("PATH", "")
    if directory not in current_path:
        cmd = f'[Environment]::SetEnvironmentVariable("Path", "{current_path};{directory}", "User")'
        subprocess.run(["powershell", "-Command", cmd], check=True)
    print("PATH actualizado.")

def verify_ffmpeg():
    """Verifica si FFmpeg está instalado."""
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
        print("FFmpeg está instalado correctamente:")
        print(result.stdout.splitlines()[0])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("FFmpeg no está instalado o no se encuentra en el PATH.")
        return False

def is_admin():
    """Verifica si el script se ejecuta con privilegios de administrador."""
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        print("No se pudo verificar los privilegios de administrador. Asumiendo que no es admin.")
        return False

def install_ffmpeg():
    """Instala FFmpeg si no está presente."""
    if verify_ffmpeg():
        print("FFmpeg ya está configurado.")
        return

    if not is_admin():
        print("Este script necesita privilegios de administrador para instalar FFmpeg.")
        print("Por favor, ejecuta este script como administrador.")
        sys.exit(1)

    install_dir = os.path.join(os.environ["USERPROFILE"], "ffmpeg")
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    zip_path = os.path.join(install_dir, "ffmpeg.zip")
    try:
        download_file(FFMPEG_URL, zip_path)
    except Exception as e:
        print(f"Error al descargar FFmpeg: {e}")
        sys.exit(1)

    try:
        extract_zip(zip_path, install_dir)
    except Exception as e:
        print(f"Error al extraer FFmpeg: {e}")
        sys.exit(1)

    extracted_dir = next((d for d in os.listdir(install_dir) if d.startswith("ffmpeg-")), None)
    if not extracted_dir:
        print("No se encontró el directorio extraído de FFmpeg.")
        sys.exit(1)
    
    bin_dir = os.path.join(install_dir, extracted_dir, "bin")
    try:
        add_to_path(bin_dir)
    except Exception as e:
        print(f"Error al actualizar el PATH: {e}")
        sys.exit(1)

    os.remove(zip_path)
    if verify_ffmpeg():
        print("FFmpeg se instaló y configuró correctamente.")
    else:
        print("La instalación falló. Por favor, verifica manualmente.")
    print("Nota: Reinicia tu terminal o computadora para que los cambios en el PATH surtan efecto.")

def install_python_dependencies():
    """Instala las dependencias de Python necesarias."""
    dependencies = [
        "openai-whisper",
        "deep-translator",
        "gtts",
        "tk"
    ]
    print("Instalando dependencias de Python...")
    for dep in dependencies:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", dep], check=True, capture_output=True, text=True)
            print(f"{dep} instalado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al instalar {dep}: {e.stderr}")
            sys.exit(1)
    print("Todas las dependencias de Python instaladas.")

def traducir(texto):
    """Traduce texto de inglés a español."""
    try:
        from deep_translator import GoogleTranslator
        max_length = 5000
        if len(texto) > max_length:
            partes = [texto[i:i + max_length] for i in range(0, len(texto), max_length)]
            traducido = ""
            for i, parte in enumerate(partes):
                print(f"Traduciendo parte {i + 1} de {len(partes)}...")
                traducido += GoogleTranslator(source='en', target='es').translate(parte)
            return traducido
        else:
            return GoogleTranslator(source='en', target='es').translate(texto)
    except Exception as e:
        return f"[ERROR DE TRADUCCIÓN: {e}]"

def generar_audio_segmentado(segments, duration_original, output_dir):
    """Genera y concatena segmentos de audio en español."""
    audio_files = []
    total_duration = 0
    for i, segment in enumerate(segments):
        start = segment['start']
        end = segment['end']
        texto = traducir(segment['text'])
        print(f"Segmento {i}: {start}s - {end}s: {texto}")

        from gtts import gTTS
        tts = gTTS(text=texto, lang='es', slow=False)
        temp_audio = os.path.join(output_dir, f"temp_segment_{i}.mp3")
        tts.save(temp_audio)

        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", temp_audio]
        result = subprocess.run(cmd, capture_output=True, text=True)
        duration_audio = float(result.stdout.strip())

        target_duration = end - start
        speed_factor = duration_audio / target_duration
        adjusted_audio = os.path.join(output_dir, f"adjusted_segment_{i}.mp3")
        if 0.5 <= speed_factor <= 2.0:
            cmd = ["ffmpeg", "-i", temp_audio, "-filter:a", f"atempo={speed_factor}", "-y", adjusted_audio]
        else:
            sample_rate = 44100
            adjusted_rate = sample_rate / speed_factor
            cmd = ["ffmpeg", "-i", temp_audio, "-filter:a", f"asetrate={adjusted_rate},atempo=1.0", "-y", adjusted_audio]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error al ajustar segmento {i}: {result.stderr}")

        audio_files.append((adjusted_audio, start))
        total_duration = max(total_duration, end)
        os.remove(temp_audio)

    concat_file = os.path.join(output_dir, "concat_list.txt")
    output_audio = os.path.join(output_dir, "audio_en_espanol.mp4")
    with open(concat_file, "w") as f:
        last_end = 0
        for audio, start in sorted(audio_files, key=lambda x: x[1]):
            if start > last_end:
                silence_duration = start - last_end
                silence_file = os.path.join(output_dir, f"silence_{start}.mp3")
                cmd = ["ffmpeg", "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=mono", "-t", str(silence_duration), "-y", silence_file]
                subprocess.run(cmd, capture_output=True, text=True)
                f.write(f"file '{silence_file}'\n")
            f.write(f"file '{audio}'\n")
            last_end = start + get_audio_duration(audio)

    cmd = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_file, "-c:a", "aac", "-y", output_audio]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error al concatenar audio:", result.stderr)
        return None, audio_files, concat_file

    print(f"Audio en español concatenado guardado en: {output_audio}")
    final_audio_duration = get_audio_duration(output_audio)
    print(f"Duración del audio final: {final_audio_duration} segundos (objetivo: {duration_original} segundos)")
    return output_audio, audio_files, concat_file

def seleccionar_video():
    """Abre un cuadro de diálogo para seleccionar un video."""
    root = Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        title="Selecciona un video",
        filetypes=[("Videos", "*.mp4 *.mkv *.avi *.mov")]
    )
    return filepath

def get_audio_duration(audio_path):
    """Obtiene la duración de un archivo de audio."""
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())

def get_video_duration(video_path):
    """Obtiene la duración del video."""
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())

def main():
    # Verificar si Python está instalado
    if not check_python():
        sys.exit(1)

    # Instalar FFmpeg
    install_ffmpeg()

    # Instalar dependencias de Python
    install_python_dependencies()

    # Importar dependencias después de instalarlas
    import whisper
    from tkinter import Tk, filedialog, messagebox
    from deep_translator import GoogleTranslator
    from gtts import gTTS

    # Procesar video
    video_path = seleccionar_video()
    if not video_path:
        messagebox.showinfo("Info", "No se seleccionó ningún video.")
        return

    video_file = Path(video_path)
    output_dir = video_file.parent  # Usar el directorio del video de entrada
    output_video = os.path.join(output_dir, f"{video_file.stem}_espanol{video_file.suffix}")

    duration_original = get_video_duration(video_path)
    print(f"Duración del video original: {duration_original} segundos")

    print("🎬 Extrayendo audio...")
    tmp_dir = tempfile.gettempdir()
    audio_path = os.path.join(tmp_dir, "temp_audio.wav")
    cmd = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", "-y", audio_path]
    print("FFmpeg Command:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFmpeg failed with error:", result.stderr)
        messagebox.showerror("Error", "Fallo al extraer audio.")
        return

    print("🧠 Transcribiendo con Whisper...")
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path, language="en", verbose=False)
        segments = result["segments"]
        print(f"Número de segmentos transcritos: {len(segments)}")
    except Exception as e:
        print(f"Whisper Error: {e}")
        messagebox.showerror("Error", "Fallo al transcribir audio.")
        os.remove(audio_path)
        return

    print("\n🗣️ Generando y sincronizando audio en español...")
    output_audio, audio_files, concat_file = generar_audio_segmentado(segments, duration_original, output_dir)
    if not output_audio:
        messagebox.showerror("Error", "Fallo al generar audio en español.")
        os.remove(audio_path)
        for audio, _ in audio_files:
            os.remove(audio)
        os.remove(concat_file)
        return

    print("🎥 Creando video con audio en español...")
    cmd = ["ffmpeg", "-i", video_path, "-i", output_audio, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", "-y", output_video]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error al crear video:", result.stderr)
        messagebox.showerror("Error", "Fallo al crear el video final.")
        os.remove(audio_path)
        os.remove(output_audio)
        for audio, _ in audio_files:
            os.remove(audio)
        os.remove(concat_file)
        return

    print(f"Video con audio en español creado en: {output_video}")
    final_duration = get_video_duration(output_video)
    print(f"Duración del video final: {final_duration} segundos")

    # Limpiar todos los archivos intermedios
    os.remove(audio_path)
    os.remove(output_audio)
    for audio, _ in audio_files:
        os.remove(audio)
    with open(concat_file, "r") as f:
        for line in f:
            if "silence" in line:
                os.remove(line.split("'")[1])
    os.remove(concat_file)
    print("Todos los archivos intermedios eliminados.")

    messagebox.showinfo("Listo", "Video con audio en español creado y archivos intermedios eliminados.")

if __name__ == "__main__":
    main()
