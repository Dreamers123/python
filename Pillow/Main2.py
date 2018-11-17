from PIL import Image
from PIL import ImageFilter
from struct import *
test=Image.open("pranti.jpg")
b_w=test.convert("L")
blur=test.filter(ImageFilter.BLUR)
edge=test.filter(ImageFilter.FIND_EDGES)
Detail=test.filter(ImageFilter.DETAIL)
"""b_w.show()"""
pack_data=pack("iif",34,43,4.343)
print(pack_data)
print(unpack("iif",b'"\x00\x00\x00+\x00\x00\x00\xdb\xf9\x8a@'))
"""edge.show()
blur.show()
Detail.show()"""