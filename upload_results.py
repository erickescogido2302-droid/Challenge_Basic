import os

# Usamos comillas dobles escapadas para que Windows no se confunda con los espacios
os.system("git add .")
os.system("git commit -m \"Resultados del challenge\"")
os.system("git push origin main")