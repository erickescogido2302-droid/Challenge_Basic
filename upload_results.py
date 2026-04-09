import os

# Este script automatiza el envío de resultados a GitHub
print("🚀 Iniciando la subida de resultados a GitHub...")

os.system("git add .")
os.system("git commit -m 'Resultados del challenge' ")
os.system("git push origin main")

print("✅ ¡Resultados subidos exitosamente!")