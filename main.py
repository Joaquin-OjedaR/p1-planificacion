def leer_recursos(nombre_archivo: str):
    recursos = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
            
            partes = linea.strip().split(",")

            recursos.append({
                "numero": partes[0],
                "categorias": partes[1:], 
                "tiempo": 0
            })

    return recursos

def leer_tareas(nombre_archivo: str):
    tareas = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
           
            nom, horas, categoria = linea.strip().split(",")
            tareas.append({
                "numero": nom,
                "duracion": int(horas),
                "categoria": categoria
            })
    return tareas
print ("ola")