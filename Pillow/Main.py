from PIL import Image
peya=Image.open("paranty.jpg")
Abeer=Image.open("pranti.jpg")
Hot_lady =Image.open("Peya.jpg")
Cool_boy =Image.open("Abeer.jpg")
My_girl =Hot_lady.resize((200,200))
My_boy=Cool_boy.resize((400,400))
area=(100,100,300,300)
Flip_boy=Cool_boy.transpose(Image.FLIP_LEFT_RIGHT)
Spin_boy=Cool_boy.transpose(Image.ROTATE_90)
"""My_boy.paste(My_girl,area)"""
My_boy.show()
Flip_boy.show()
Spin_boy.show()
My_boy.show()
r1,g1,b1=peya.split()
r2,g2,b2=Abeer.split()
new_image=Image.merge("RGB",(r1,g2,b2))
new_image.show()