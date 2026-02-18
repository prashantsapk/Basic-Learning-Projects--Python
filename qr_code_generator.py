import qrcode as qr
a=input("Enter the content or link to create qr code")
img = qr.make(f"{a}") 
img.save(f"{img}.png")

# Dependicies to install
#pip install qrcode
#pip install "qrcode[pil]"