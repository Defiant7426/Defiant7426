import requests

def get_leetcode_stats(username): # Función para obtener las estadísticas de LeetCode
    url = f"https://leetcode-stats-api.herokuapp.com/{username}" # URL de la API
    response = requests.get(url) # Hace una petición GET a la URL
    return response.json() # Devuelve el contenido de la respuesta en formato JSON

def update_readme(stats): # Función para actualizar el README.md
    readme_template = """
### LeetCode Stats
- **Total Problems Solved:** {total_solved}
- **Easy Problems Solved:** {easy_solved}
- **Medium Problems Solved:** {medium_solved}
- **Hard Problems Solved:** {hard_solved}
"""

    readme_content = readme_template.format( # Rellena el template con los datos de la API
        total_solved=stats['totalSolved'],
        easy_solved=stats['easySolved'],
        medium_solved=stats['mediumSolved'],
        hard_solved=stats['hardSolved']
    )

    with open("README.md", "w") as readme_file: # Abre el archivo README.md en modo escritura
        readme_file.write(readme_content) # Escribe el contenido en el archivo

username = "Defiant7426"
stats = get_leetcode_stats(username)
update_readme(stats)
