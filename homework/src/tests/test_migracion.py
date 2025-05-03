# import os
# import subprocess


# def test_migracion():
#     # Ejecutar el __main__.py de homework
#     result = subprocess.run(
#         ["python", "-m", "homework", "data/input", "data/output"],
#         capture_output=True,
#         text=True,
#     )

#     # Verificar que el script se ejecutó correctamente
#     assert result.returncode == 0, f"Error en la ejecución: {result.stderr}"

#     # Verificar que el archivo de salida existe
#     if not os.path.exists("data/output/results.tsv"):
#         raise FileNotFoundError("El archivo results.tsv no existe.")

#     # Leer y verificar el contenido del archivo de salida
#     results = {}
#     with open("data/output/results.tsv", "r", encoding="utf-8") as f:
#         lines = f.readlines()
#     for line in lines:
#         key, value = line.strip().split("\t")
#         results[key] = value

#     assert results.get("computational", 0) == "3"
#     assert results.get("analytics", 0) == "5"