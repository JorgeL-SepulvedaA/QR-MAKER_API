import fastapi
import os
import func_api

app = fastapi.FastAPI(title="QR API SOLUTION",
                            description="This is a solution for a QR code maker being used on a web",
                            version="1.0.0")

os.system('cls')

@app.get('/')
async def home():
    return 'Para acceder al modulo inicial use /QR_DATA.' + '\n \n \n' + 'Pasar por el parametro "name=[contenido_QR]?[nombre_archivo]"'

@app.get("/QR_DATA")
async def index(name = None):
    _split = []
    resul = str()

    if name is None:
        text = "default".upper()
        file = "default"
        resul = "[Sin parametros - HECHO]"
    else:
        _split = name.split("?")
        text = _split[0]
        file = _split[1]
        resul = "[Con parametros - HECHO]"
    
    return func_api.main(text, file) + " " + resul.upper()