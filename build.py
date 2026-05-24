#!/usr/bin/env python3
import os
import subprocess
import shutil
import argparse

base_dir = "/home/ignacio/personas/fisica_ii_serway"
output_dir = os.path.join(base_dir, "pdfs")

targets = {
    "main": {
        "tex_path": os.path.join(base_dir, "main.tex"),
        "working_dir": base_dir,
        "dest_name": "Fisica_II_Completo.pdf",
        "description": "Libro completo (Capítulos 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 y 13)"
    },
    "capitulo_01": {
        "tex_path": os.path.join(base_dir, "mecanica/capitulo_01/capitulo_01_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mecanica/capitulo_01"),
        "dest_name": "Capitulo_01_Fisica_y_Medicion.pdf",
        "description": "Capítulo 1 Standalone (Física y medición)"
    },
    "capitulo_02": {
        "tex_path": os.path.join(base_dir, "mecanica/capitulo_02/capitulo_02_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mecanica/capitulo_02"),
        "dest_name": "Capitulo_02_Mecanica_de_Fluidos.pdf",
        "description": "Capítulo 2 Standalone (Mecánica de fluidos)"
    },
    "capitulo_03": {
        "tex_path": os.path.join(base_dir, "mecanica/capitulo_03/capitulo_03_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mecanica/capitulo_03"),
        "dest_name": "Capitulo_03_Movimiento_Oscilatorio.pdf",
        "description": "Capítulo 3 Standalone (Movimiento oscilatorio)"
    },
    "capitulo_04": {
        "tex_path": os.path.join(base_dir, "mecanica/capitulo_04/capitulo_04_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mecanica/capitulo_04"),
        "dest_name": "Capitulo_04_Movimiento_Ondulatorio.pdf",
        "description": "Capítulo 4 Standalone (Movimiento ondulatorio)"
    },
    "capitulo_05": {
        "tex_path": os.path.join(base_dir, "mecanica/capitulo_05/capitulo_05_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mecanica/capitulo_05"),
        "dest_name": "Capitulo_05_Sobreposicion_y_Ondas_Estacionarias.pdf",
        "description": "Capítulo 5 Standalone (Sobreposición y ondas estacionarias)"
    },
    "capitulo_06": {
        "tex_path": os.path.join(base_dir, "termodinamica/capitulo_06/capitulo_06_standalone.tex"),
        "working_dir": os.path.join(base_dir, "termodinamica/capitulo_06"),
        "dest_name": "Capitulo_06_Temperatura.pdf",
        "description": "Capítulo 6 Standalone (Temperatura)"
    },
    "capitulo_07": {
        "tex_path": os.path.join(base_dir, "termodinamica/capitulo_07/capitulo_07_standalone.tex"),
        "working_dir": os.path.join(base_dir, "termodinamica/capitulo_07"),
        "dest_name": "Capitulo_07_Primera_Ley.pdf",
        "description": "Capítulo 7 Standalone (Primera ley de la termodinámica)"
    },
    "capitulo_08": {
        "tex_path": os.path.join(base_dir, "termodinamica/capitulo_08/capitulo_08_standalone.tex"),
        "working_dir": os.path.join(base_dir, "termodinamica/capitulo_08"),
        "dest_name": "Capitulo_08_Teoria_Cinetica.pdf",
        "description": "Capítulo 8 Standalone (Teoría cinética de los gases)"
    },
    "capitulo_09": {
        "tex_path": os.path.join(base_dir, "termodinamica/capitulo_09/capitulo_09_standalone.tex"),
        "working_dir": os.path.join(base_dir, "termodinamica/capitulo_09"),
        "dest_name": "Capitulo_09_Segunda_Ley.pdf",
        "description": "Capítulo 9 Standalone (Máquinas térmicas, entropía y segunda ley)"
    },
    "capitulo_10": {
        "tex_path": os.path.join(base_dir, "optica/capitulo_10/capitulo_10_standalone.tex"),
        "working_dir": os.path.join(base_dir, "optica/capitulo_10"),
        "dest_name": "Capitulo_10_Naturaleza_de_la_Luz.pdf",
        "description": "Capítulo 10 Standalone (Naturaleza de la luz y leyes de la óptica geométrica)"
    },
    "capitulo_11": {
        "tex_path": os.path.join(base_dir, "optica/capitulo_11/capitulo_11_standalone.tex"),
        "working_dir": os.path.join(base_dir, "optica/capitulo_11"),
        "dest_name": "Capitulo_11_Formacion_de_las_Imagenes.pdf",
        "description": "Capítulo 11 Standalone (Formación de las imágenes)"
    },
    "capitulo_12": {
        "tex_path": os.path.join(base_dir, "optica/capitulo_12/capitulo_12_standalone.tex"),
        "working_dir": os.path.join(base_dir, "optica/capitulo_12"),
        "dest_name": "Capitulo_12_Optica_Ondulatoria.pdf",
        "description": "Capítulo 12 Standalone (Óptica ondulatoria)"
    },
    "capitulo_13": {
        "tex_path": os.path.join(base_dir, "moderna/capitulo_13/capitulo_13_standalone.tex"),
        "working_dir": os.path.join(base_dir, "moderna/capitulo_13"),
        "dest_name": "Capitulo_13_Fisica_Atomica.pdf",
        "description": "Capítulo 13 Standalone (Física atómica)"
    },
    "entropia": {
        "tex_path": os.path.join(base_dir, "termodinamica/capitulo_09/seccion_entropia_standalone.tex"),
        "working_dir": os.path.join(base_dir, "termodinamica/capitulo_09"),
        "dest_name": "Seccion_Entropia.pdf",
        "description": "Compendio de Entropía (Secciones 9.6, 9.7 y 9.8)"
    }
}

def compile_latex(tex_path, working_dir, dest_name):
    print(f"\n🚀 Compilando: {os.path.basename(tex_path)}...")
    
    # Run pdflatex (2 passes for TOC and hyperref to build successfully)
    for pass_num in range(1, 3):
        print(f"   Paso {pass_num}/2...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(tex_path)],
            cwd=working_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )
        
        if result.returncode != 0:
            print(f"❌ Error al compilar {os.path.basename(tex_path)}:")
            # If log file exists, print the last 20 lines to help diagnose
            log_path = tex_path.replace(".tex", ".log")
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8", errors="ignore") as log:
                    lines = log.readlines()
                    print("".join(lines[-20:]))
            return False
            
    # Locate the generated PDF
    pdf_name = os.path.basename(tex_path).replace(".tex", ".pdf")
    generated_pdf = os.path.join(working_dir, pdf_name)
    
    if os.path.exists(generated_pdf):
        os.makedirs(output_dir, exist_ok=True)
        destination = os.path.join(output_dir, dest_name)
        shutil.copy2(generated_pdf, destination)
        print(f"✅ ¡Éxito! PDF guardado en: pdfs/{dest_name}")
        return True
    else:
        print("❌ Error: No se encontró el archivo PDF resultante.")
        return False

def clean_temp_files():
    print("\n🧹 Limpiando archivos auxiliares de LaTeX...")
    extensions = [".aux", ".log", ".out", ".toc", ".pdf"]
    for target in targets.values():
        wdir = target["working_dir"]
        tex_file = os.path.basename(target["tex_path"])
        base_name = tex_file.replace(".tex", "")
        
        for ext in extensions:
            temp_file = os.path.join(wdir, base_name + ext)
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Automatizador de compilación para Física II (Serway)")
    parser.add_argument("--target", choices=list(targets.keys()) + ["all"], default="all",
                        help="Compilar un objetivo específico o 'all' (por defecto)")
    parser.add_argument("--clean", action="store_true", help="Limpiar archivos temporales de LaTeX")
    
    args = parser.parse_args()
    
    # Check if pdflatex is installed
    if not shutil.which("pdflatex"):
        print("❌ Error: 'pdflatex' no está instalado en este sistema. Por favor instala TexLive o similar.")
        return

    if args.clean:
        clean_temp_files()
        print("✨ Limpieza completada.")
        return

    if args.target == "all":
        print("📚 Iniciando compilación de todos los objetivos...")
        success_count = 0
        for name, spec in targets.items():
            if compile_latex(spec["tex_path"], spec["working_dir"], spec["dest_name"]):
                success_count += 1
        
        # Cleanup temp files after compilation
        clean_temp_files()
        
        print(f"\n🎉 ¡Proceso finalizado! Compilados exitosamente: {success_count}/{len(targets)}")
        if success_count > 0:
            print(f"📂 Encuentra todos tus PDFs en la carpeta: {output_dir}")
    else:
        spec = targets[args.target]
        if compile_latex(spec["tex_path"], spec["working_dir"], spec["dest_name"]):
            clean_temp_files()

if __name__ == "__main__":
    main()
