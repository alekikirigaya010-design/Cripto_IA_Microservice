from fastapi import FastAPI
import requests
import ia_advisor 

app=FastAPI()

@app.get("/")
def inicio():
    return {"status": "sistemas en linea", "objetivo": "Manhattan"}

@app.get("/precio")
def precio():
    try:
        url= "https://api.coindesk.com/v1/bpi/currentprice.json"
        respuesta = requests.get(url,timeout=5)
        respuesta.raise_for_status()
        datos = respuesta.json ()
        precio_actual = datos ['bpi'] ['USD'] ['rate']
        return { "mensaje": "Precio de bitcoin obtenido satisfactoriamente","USD": precio_actual}
    except Exception as e:
        return {"error": "No se pudo conectar con el mercado", "detalle": str(e), "estado": "modo de emergencia Manhattan"}
        @app.get ("/convertir/{cantidad}")
        def convertir_moneda(cantidad:float):
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            r = requests.get(url)
            precio_usd = r.json()['bpi'] ['USD'] ['rate_float']
            total_btc = cantidad / precio_usd
            return {
            "cantidad_usd": cantidad,
            "precio_btc_actual": precio_usd,"puedes_comprar": f}
@app.get("/ia-consejo")
def dar_consejo(precio:float, tendencia: str):
    resultado = ia_advisor.get_ai_device(precio,tendencia)
    return {"mensaje": resultado}