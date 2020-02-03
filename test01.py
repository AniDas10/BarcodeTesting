import barcode

#hr = barcode.get_barcode_class('ean13')
#Hr = hr('600041700111')
#
#qr = Hr.save('pass01')

from barcode.writer import ImageWriter

qr = barcode.get_barcode_class('code39')

qrcode = qr('A60004170011', writer=ImageWriter())

test = qrcode.save('pass01')