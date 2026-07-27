import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4)
qr.add_data("https://i.pinimg.com/236x/25/aa/1a/25aa1a16b78d63f639b04b8427d4f2d6.jpg")
qr.make(fit=True)

img = qr.make_image(back_color="pink",fill_color="blue")
img.save("simple.png")