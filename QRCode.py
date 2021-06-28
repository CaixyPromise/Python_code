# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""


import qrcode
import os

qr = qrcode.QRCode(version=10,box_size = 10, border = 4,
                   error_correction = qrcode.constants.ERROR_CORRECT_L)
qr.add_data("https://www.baidu.com")
qr.make(fit=True)
img = qr.make_image()
img.save("QrCode.png")
os.startfile("QrCode.png")
