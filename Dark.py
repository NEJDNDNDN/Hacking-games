import webbrowser
import uuid
import os
import time

# ألوان
RED = '\033[1;91m'
GREEN = '\033[1;92m'
YELLOW = '\033[1;93m'
BLUE = '\033[1;94m'
PINK = '\033[1;95m'
CYAN = '\033[1;96m'
WHITE = '\033[1;97m'
RESET = '\033[0m'

# عرض اللوجو
def logo():
    os.system("clear")
    print(f"""{CYAN}
██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝ ╚███╔╝     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔═══╝  ██╔██╗     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║██║     ██╔╝ ██╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                    {RED}𝑫𝑨𝑹𝑲 𝑯𝑨𝑪𝑲𝑬𝑹
    {RESET}""")

# تحويل تلقائي للقناة
def redirect():
    print(f"{YELLOW}يتم الآن توجيهك إلى قناة المطور...{RESET}")
    time.sleep(2)
    webbrowser.open("https://t.me/+PFbp1Ayc_1I3ZTFk")
    time.sleep(1)

# التطبيقات وروابطها (استبدل الروابط بـ GitHub Pages)
apps = {
    "1": ("فري فاير", "https://yourusername.github.io/freefire.html"),
    "2": ("ببجي", "https://yourusername.github.io/pubg.html"),
    "3": ("بيس 2024", "https://yourusername.github.io/pes.html"),
    "4": ("فيسبوك", "https://yourusername.github.io/facebook.html"),
    "5": ("تويتر", "https://yourusername.github.io/twitter.html"),
    "6": ("One State", "https://yourusername.github.io/onestate.html"),
    "7": ("إنستجرام", "https://yourusername.github.io/instagram.html"),
    "8": ("روبلوكس", "https://yourusername.github.io/roblox.html"),
    "9": ("فورت نايت", "https://yourusername.github.io/fortnite.html"),
    "10": ("سناب شات", "https://yourusername.github.io/snapchat.html"),
}

# تشغيل الأداة
logo()
redirect()

print(f"{GREEN}اختر التطبيق أو اللعبة:{RESET}")
for key, (name, _) in apps.items():
    print(f"{BLUE}{key} - {WHITE}{name}{RESET}")

choice = input(f"\n{CYAN}ادخل رقم اختيارك: {RESET}").strip()

if choice in apps:
    name, base_url = apps[choice]
    user_id = str(uuid.uuid4())[:8]
    final_url = f"{base_url}?id={user_id}"
    print(f"{GREEN}جاري فتح {name}...{RESET}")
    time.sleep(1)
    webbrowser.open(final_url)
else:
    print(f"{RED}اختيار غير صحيح، حاول مرة أخرى.{RESET}")
