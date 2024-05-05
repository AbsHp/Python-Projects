import pyqrcode

data = input("Enter the text or link to generate QR Code: ")

qr = pyqrcode.create(data)

qr.svg('qr_code.svg', scale = 8)