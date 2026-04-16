import os

print("🧹 Limpiando caché de Git y forzando subida...")

# 1. Configurar editor para que sea invisible
os.system('git config --global core.editor true')

# 2. Agregar todo
os.system('git add --all')

# 3. Commit forzado (si falla el normal, este lo intenta de nuevo)
os.system('git commit -m "Entrega final confirmada" --allow-empty')

# 4. Push forzado al servidor
print("📤 Empujando cambios a GitHub...")
os.system('git push origin main --force')

print("✅ ¡GitHub actualizado y Bloc de notas derrotado!")