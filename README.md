# Física II - Serway & Jewett: Ejercicios Resueltos

Este repositorio contiene la estructura estandarizada y modular en LaTeX para organizar, redactar y compilar las resoluciones de los ejercicios del libro **Física para Ciencias e Ingeniería (Volumen 1 / 2) de Serway & Jewett**.

La sección actual activa es la de **Termodinámica** (4 capítulos).

---

## 📂 Estructura del Directorio

El proyecto está diseñado bajo un paradigma modular altamente escalable. Cada ejercicio cuenta con su propia carpeta dedicada, lo que facilita enormemente la gestión de esquemas, figuras (`.png`, `.pdf`), scripts de cálculo y la resolución en LaTeX.

```text
fisica_ii_serway/
├── main.tex                         # Archivo general que compila todo el libro
├── README.md                        # Documento de guía y uso
└── termodinamica/                   # Bloque temático de Termodinámica
    ├── capitulo_06/                 # Capítulo 6: Temperatura
    │   ├── capitulo_06.tex          # Contenido del capítulo 6 (incluido en main.tex)
    │   └── capitulo_06_standalone.tex # Archivo para generar el PDF dedicado del Capítulo 6
    ├── capitulo_07/                 # Capítulo 7: Primera ley de la termodinámica
    │   ├── capitulo_07.tex          # Contenido del capítulo 7 (incluido en main.tex)
    │   ├── capitulo_07_standalone.tex # Archivo para generar el PDF dedicado del Capítulo 7
    │   ├── piense_01/               # Ejercicio 1 (Piense, dialogue y comparta)
    │   │   └── ejercicio.tex        # LaTeX de la pregunta y resolución
    │   ├── piense_02/               # Ejercicio 2 (Piense, dialogue y comparta)
    │   │   └── ejercicio.tex
    │   ├── prob_7_1_01/             # Problema Sección 7.1, Ejercicio 1
    │   │   └── ejercicio.tex
    │   ├── prob_7_2_02/             # Problema Sección 7.2, Ejercicio 2
    │   │   └── ejercicio.tex
    │   └── ...                      # Resto de problemas con su estructura dedicada
    ├── capitulo_08/                 # Capítulo 8: Teoría cinética de los gases
    │   ├── capitulo_08.tex
    │   └── capitulo_08_standalone.tex
    └── capitulo_09/                 # Capítulo 9: Segunda ley de la termodinámica
        ├── capitulo_09.tex
        └── capitulo_09_standalone.tex
```

---

## 🛠️ Cómo Compilar los Documentos

### Opción 1: Archivo General (`main.tex`)
Este archivo compilará **todos** los capítulos juntos en un único libro unificado con índice analítico.
- Configura tu editor de LaTeX o compila utilizando:
  ```bash
  pdflatex main.tex
  ```

### Opción 2: PDF Dedicado por Capítulo
Cada capítulo tiene un archivo ejecutable dedicado con el sufijo `_standalone.tex` (ej. `capitulo_07_standalone.tex`).
Para generar el PDF exclusivo de un capítulo específico:
1. Abre el archivo `capitulo_XX_standalone.tex`.
2. Compílalo directamente.
3. Se generará un PDF estilizado de artículo independiente para ese capítulo específico.
   ```bash
   cd termodinamica/capitulo_07
   pdflatex capitulo_07_standalone.tex
   ```

---

## 📝 Agregar Nuevos Ejercicios

Para agregar un ejercicio al Capítulo 7, por ejemplo:
1. Crea una nueva carpeta en `termodinamica/capitulo_07/` con la nomenclatura correspondiente (ej. `prob_7_2_09`).
2. Crea el archivo `ejercicio.tex` en su interior y escribe el enunciado utilizando `\item`.
3. Agrégalo en `termodinamica/capitulo_07/capitulo_07.tex` usando la directiva:
   ```latex
   \subimport{prob_7_2_09/}{ejercicio.tex}
   ```
