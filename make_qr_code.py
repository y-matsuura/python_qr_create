import os
import qrcode

save_qr = "qr_code.png"
print("Please input string you want to convert to qrcode")
input_string = input()
qr_img = qrcode.make(input_string)
qr_img.save(save_qr)
current_dir = os.getcwd()
print("「{0}\\{1}」にQRコードを保存しました".format(current_dir, save_qr))
