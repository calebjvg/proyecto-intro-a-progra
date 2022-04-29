balas={"1":25,"2":75,"3":500}
armas={1:"asalto",2:"bazooka",3:"sniper"}

def equipo(personas):
    reservaequipo=[]
    input_balas=""
   
    for i, cantidad in balas.items():
        input_balas+=f"{i}.{cantidad}\n"
    for i,persona in enumerate(personas):
        print(f"Cuantas balas desea comprar la persona {i+1}")
        seleccion=input(input_balas)
        personas[i]["cantidad de balas"]=balas[seleccion]


