import qrcode
x=qrcode.QRCode()
msg="good going"
x.add_data(msg)
x.make(fit=True)
res=x.make_image(fill_color="black",back_color="white")
res.save("gud.png")
print("created successfully")