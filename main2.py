from barcode.writer import ImageWriter
import barcode

ean = barcode.get('ean13', '123456789101', writer=ImageWriter())
options = dict(compress=True)
filename = ean.save('ean13')