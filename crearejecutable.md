```bash
pip install pyinstaller
```

```bash
# Les genera un unico archivo en la carpeta dist
pyinstaller --windowed --onefile clase4.py

```

```bash
# Agregamos un icono a nuestra aplicacion
pyinstaller --windowed --onefile –icon=./logo.ico archivo.py
```