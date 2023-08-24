import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

qr.add_data("https://www.linkedin.com/in/prashant-kumar-parth-246245253")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("LinkedIn_Prashant.png")
