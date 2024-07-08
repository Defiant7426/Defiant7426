import requests

def get_leetcode_stats(username): # Función para obtener las estadísticas de LeetCode
    url = f"https://leetcode-stats-api.herokuapp.com/{username}" # URL de la API
    response = requests.get(url) # Realizar petición GET a la API
    return response.json() # Devolver respuesta en formato JSON

def update_readme(stats): # Función para actualizar el README.md con las estadísticas
    with open("README.md", "r") as file: # Abrir el archivo README.md en modo lectura
        readme_content = file.read() # Leer el contenido del archivo

    # Delimitadores para identificar la sección de estadísticas
    start_delimiter = "<!--START_LEETCODE_STATS-->"
    end_delimiter = "<!--END_LEETCODE_STATS-->"

    # Crear la nueva sección de estadísticas
    new_stats = f"""
{start_delimiter}
### LeetCode Stats
- **Total Problems Solved:** {stats['totalSolved']}
- **Easy Problems Solved:** {stats['easySolved']}
- **Medium Problems Solved:** {stats['mediumSolved']}
- **Hard Problems Solved:** {stats['hardSolved']}
{end_delimiter}
"""

    # Actualizar el contenido del README.md con las nuevas estadísticas
    updated_readme = readme_content.split(start_delimiter)[0] + new_stats + readme_content.split(end_delimiter)[1]

    with open("README.md", "w") as file: # Abrir el archivo README.md en modo escritura
        file.write(updated_readme) # Escribir el contenido actualizado en el archivo

username = "Defiant7426"  # Reemplaza con tu nombre de usuario de LeetCode
stats = get_leetcode_stats(username) # Obtener las estadísticas de LeetCode
update_readme(stats) # Actualizar el README.md con las estadísticas
