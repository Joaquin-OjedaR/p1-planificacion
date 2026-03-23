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


def planificar(tareas, recursos):
    makespan = []
    for tarea in tareas:
        contador = 0
        for r in recursos:
            if tarea["categoria"] in r["categorias"]:
                contador += 1
        tarea["opciones"] = contador

    tareas.sort(key=lambda t: (t["opciones"], -t["duracion"]))
    for tarea in tareas:
      
        compatibles = []
        for r in recursos:
            if tarea["categoria"] in r["categorias"]:
                compatibles.append(r)

        mejor_recurso = min(compatibles, key=lambda r: r["tiempo"])

        inicio = mejor_recurso["tiempo"]
        fin = inicio + tarea["duracion"]

        makespan.append({
            "tarea": tarea["numero"],          
            "recurso": mejor_recurso["numero"], 
            "inicio": inicio,
            "fin": fin
        })

        mejor_recurso["tiempo"] = fin

    return makespan

def generar_output(plan, nombre_archivo: str):
    with open(nombre_archivo, "w") as f:
        for p in plan:
            linea = f"{p['tarea']},{p['recurso']},{p['inicio']},{p['fin']}\n"
            f.write(linea)
        makespan = max(p["fin"] for p in plan)
        f.write(f"Makespan: {makespan}\n")