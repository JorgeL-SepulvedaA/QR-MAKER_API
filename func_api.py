import os
import stat
import qrcode
from PIL import Image
from time import sleep


os.system('cls')

def main(a, b):
    link = a 
    archivo = b
    extension = ".png"
    directory = "QRcodes"
    ruta = str()

    if not os.path.isdir(directory):
        os.makedirs(directory)
        ruta = os.getcwd()
    elif os.path.isdir(directory):
        ruta = os.getcwd()

    direccion = f"{ruta}\\{directory}\\{archivo}{extension}"


    num = 0
    exist = os.path.isfile(direccion)

    while exist:
        direccion = f"{ruta}\\{directory}\\{archivo}({num+1}){extension}"
        num +=1
        exist = os.path.isfile(direccion)


    os.chmod(ruta, stat.S_IWRITE)


    abrir = open(direccion, "wb")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(abrir)

    abrir.close()

    return direccion