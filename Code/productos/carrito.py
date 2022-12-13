class Carrito(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, suscripcion, cantidad):
        id = str(suscripcion.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "suscripcion_id": suscripcion.id,
                "name": suscripcion.name,
                "precio_unitario": suscripcion.precio,
                "cantidad": int(cantidad),
            }
        else:
            self.carrito[id]["cantidad"] += 1
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, suscripcion):
        id = str(suscripcion.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, suscripcion):
        id = str(suscripcion.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            if self.carrito[id]["cantidad"] <= 0: 
                self.eliminar(suscripcion)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
