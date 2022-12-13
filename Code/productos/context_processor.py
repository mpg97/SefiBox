from .carrito import Carrito



def total_carrito(request):
    total = 0
    
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += int(value["precio_unitario"])*int(value["cantidad"])
    return {"total_carrito": total}


def carrito(request): 
    return {'carrito': Carrito(request)}