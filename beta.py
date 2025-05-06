from colorama import init, Fore, Back, Style
import webbrowser
import time
import os
from itertools import cycle
import sys
import math
import threading
import json
import shutil
try:
    from pypresence import Presence
    discord_rpc_available = True
except ImportError:
    discord_rpc_available = False

try:
    import minecraft_launcher_lib as mclib
    minecraft_launcher_available = True
except ImportError:
    minecraft_launcher_available = False
    print(f"{Style.DIM}minecraft-launcher-lib почему то не обнаружен :\ попробуйте -> pip install minecraft-launcher-lib{Style.RESET_ALL}")

init(autoreset=True)
client_id = '1368298880474812519'  
discord_rpc = None
rpc_thread = None

MINECRAFT_DIR = os.path.join(os.path.expanduser("~"), ".mine4rchive")
PROFILES_FILE = os.path.join(MINECRAFT_DIR, "profiles.json")

def init_discord_rpc():
    global discord_rpc
    if discord_rpc_available:
        try:
            discord_rpc = Presence(client_id)
            discord_rpc.connect()
            update_discord_rpc("В главном меню")
            return True
        except Exception as e:
            print(f"{Style.DIM}Не удалось подключиться к Discord RPC :\ ERROR: {e}{Style.RESET_ALL}")
    return False

def update_discord_rpc(details, state="Выбирает клиент", large_image="logo", large_text="Mine4rchive"):
    if discord_rpc:
        try:
            discord_rpc.update(
                details=details,
                state=state,
                large_image=large_image,
                large_text=large_text,
                start=int(time.time())
            )
        except Exception:
            pass

def run_discord_rpc():
    if discord_rpc_available:
        global rpc_thread
        rpc_thread = threading.Thread(target=init_discord_rpc)
        rpc_thread.daemon = True
        rpc_thread.start()
'''#читы #кряк #чит #кфг
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴋᴩяᴋ нуᴩᴄуᴧᴛᴀн 1.16.5 - https://liget.ru/bSzj
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴇxᴘᴇɴsɪᴠᴇ ꜰɪxᴇᴅ ᴨод 3.1 (ᴨодходяᴛ ᴋɸᴦ оᴛ ϶ᴋᴄы 3.1) - https://moneyz.fun/BSQs3h
ⶆ 🖤ᴄᴋᴀчᴀᴛь чиᴛы дᴧя ᴋᴀᴩɯᴇй ᴄᴇᴩʙᴇᴩоʙ - https://moneyz.fun/nytzyh
ⶆ 🖤ᴄᴋᴀчᴀᴛь цᴇᴧᴋу ᴋᴩяᴋ ʙʏ ʙᴀʟᴛʏɴ- https://moneyz.fun/PymQ9T
ⶆ 🖤ᴄᴋᴀчᴀᴛь цᴇᴧᴇᴄᴛиᴀᴧ 1.16.5 - https://moneyz.fun/C4m7qU
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴍᴏᴏɴʜᴀᴄᴋ 1.16.5 - https://workupload.com/file/gQ7WmyjMmn6
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴋᴩяᴋ нуᴩᴄуᴧᴛᴀн  нᴇᴋᴄᴛᴦᴇн 1.12.2 - https://moneyz.fun/4NKAYD
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴛᴏxɪᴄᴄʟɪᴇɴᴛ 1.16.5 - https://workupload.com/file/Gdg475RZztp
ⶆ 🖤ᴄᴋᴀчᴀᴛь ɴᴇᴡᴄᴏᴅᴇ 1.0 - https://workupload.com/file/BESb3nuTEAu
ⶆ 🖤ᴄᴋᴀчᴀᴛь ɴᴇᴡᴄᴏᴅᴇ 1.4 (1.16.5) - https://workupload.com/file/Pj4dz364WWB
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴋᴩяᴋ ʙиᴧдᴀ 1.16.5 - https://moneyz.fun/WajcFC
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴀᴜʀᴏʀᴀ ᴄʟɪᴇɴᴛ ʙᴀsᴇ ᴇxᴘᴇɴsɪᴠᴇ - https://workupload.com/file/7nKTwWTh3jM
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴇxᴄᴇʟʟᴇɴᴛ ʙᴇᴛᴀ ᴄʀᴀᴄᴋ (1.16.5) - https://moneyz.fun/y1wrSc
ⶆ 🖤ᴄᴋᴀчᴀᴛь ᴠᴏᴅᴋᴀ ᴄʟɪᴇɴᴛ 1.1 нᴀ 1.16.5 - https://workupload.com/file/dunwGQ4jECg
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Verist Client - https://workupload.com/start/6SpPT5xCfjx
ⶆ 🖤 ᴄᴋᴀчᴀᴛь VenusFree Client - https://t.me/+Oih0OfHwVr85NDky (Скачать из тг)
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Celestial Recode (Старый билд) - https://drive.google.com/file/d/18xydgjbc1FAXkhhjlC-YgICtI09KhWo6/view?usp=drive_link
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Сrack Britva Myst Beta - https://drive.google.com/file/d/1sffGMEJW4pSRb29sntzWnUddLQTWhNwn/view?usp=drive_link
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Troxil Client (Legit) - https://drive.google.com/file/d/1Q95cXghcq0ein2IYYsO-r0RlcsRewOwj/view?usp=sharing
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Blessed Client (Legit) - https://drive.google.com/file/d/1wnwD4sfPmud_2mbjWHbYvD9wV745sgzY/view?usp=sharing
ⶆ 🖤 ᴄᴋᴀчᴀᴛь NeoWare - https://workupload.com/file/DGJQdRCRHd2
ⶆ 🖤ᴄᴋᴀчᴀᴛь Night Project - https://workupload.com/file/JU88vUBMLNb
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Xameleon 3.0.0 - https://workupload.com/start/eCpqAeN8yDE
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Vape V4 4.17 (Бед Варс т.д) - https://workupload.com/file/HmEVdZHr5Fq
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Flap (Бед Варс т.д) - https://workupload.com/file/ecR4MaJFWMH
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Wissend Premium 1.2 - https://workupload.com/file/M34agFNprDE
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Vredux Beta (Старый билд) - https://drive.google.com/file/d/1eyJyTrDdSqXeawLP23HRNKTTeeWaurn0/view
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Aurora DLC (Legit) - https://workupload.com/file/jVnrQA4QvYq
ⶆ 🖤 ᴄᴋᴀчᴀᴛь ThunderHack Recode - https://github.com/Pan4ur/ThunderHack-Recode/releases
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Fluger Client - https://workupload.com/file/HyLykevQbV2
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Takker - https://workupload.com/file/kZC3LyaP4Hj
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Abstract 4 (1.20.4) - https://workupload.com/file/gzSTDGqPamL
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Cleaner Chets - https://mega.nz/file/ukUy0ACR#9p0C_urJR8N88zusG8Etz3bCgQvoAiHATmQzudpJCnM
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Energy Client (Билд 2024.08) - https://workupload.com/file/vrJCMP5HQvD
ⶆ 🖤 ᴄᴋᴀчᴀᴛь ArixRecode - https://workupload.com/file/Vys4tCNQCMe
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Hush Plus - https://workupload.com/file/4PqHvu8jmPL
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Crack Veline Plus - https://workupload.com/file/ShvakzGDvUZ
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Legit HitBox - https://yougame.biz/threads/330046/
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Enigma Reloaded - https://workupload.com/file/keRyXyg2CmX
ⶆ 🖤 ᴄᴋᴀчᴀᴛь Очистка Journal Trace - https://workupload.com/file/GXJuxt3ndtQ
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

ⶆ ᴄᴋᴀчᴀᴛь ᴄбоᴩниᴋ ᴩᴨ ʙᴀʟʏʏɴᴀ дᴧя ᴨʙᴨ 1.16.5 - https://drive.google.com/file/d/1wHvCdkTntb1h1TBgZbk3FG8BK7HDb2O1/view?usp=sharing
ⶆ ᴄᴋᴀчᴀᴛь ᴄбоᴩниᴋ ʙизуᴀᴧоʙ 1.16.5 (ꜰᴏʀɢᴇ) - https://moneyz.fun/BFx6dB
ⶆ ᴄᴋᴀчᴀᴛь ноʙоᴇ ᴋɸᴦ ʙᴀʟʏʏɴᴀ ARBUZ CLIENT - https://moneyz.fun/rhyLgt
ⶆ ᴄᴋᴀчᴀᴛь ʙᴄᴇ ᴩᴨɯниᴋи ɸᴧюᴦᴇᴩᴀ - https://moneyz.fun/VpzFEd
ⶆ ᴄᴋᴀчᴀᴛь ᴋɸᴦ нᴀ ᴇxᴘᴇɴsɪᴠᴇ ᴜᴘɢʀᴇᴀᴅᴇ ᴨод ʀᴇᴀʟʟʏ ᴡᴏʀʟᴅ - https://moneyz.fun/cMonjN
ⶆ ᴄᴋᴀчᴀᴛь ᴋɸᴦ оᴛ ᴦодзиᴧᴋи нᴀ ᴡɪʟᴅ ᴄʟɪᴇɴᴛ - https://moneyz.fun/ytX8g4
ⶆ ᴄᴋᴀчᴀᴛь ᴋɸᴦ оᴛ ФЛЮГЕРА нᴀ ᴡɪʟᴅ ᴄʟɪᴇɴᴛ - https://moneyz.fun/fDzbEC'''
clients = {
        'Sites with cheats':[
            {
            "name": "CHP-cheatspacks",
            "link": "https://cheats-pack.su/",
            "clean": False
            },
            {
            "name": "RockPacks",
            "link": "https://rockpacks.ru/",
            "clean": False
            },
            {
            "name": "CheatsHub",
            "link": "https://cheathub.tech/",
            "clean": True
            },
        ],
        "CheatsPacks": [
            {
            "name": "Pack-legit for funtime-2b2t clients-hvh",
            "link": "https://t.me/CastleOfCatlavan/9",
            "clean": True
            },
        ],
        "Launchers": [
        {
            "name": "Collapse loader",
            "link": "https://collapseloader.org/",
            "clean": True
        },
        {
            "name": "Newlauncher",
            "link": "https://newlauncher.ru/",
            "clean": False
        },
        {
            "name": "Aorus Launcher",
            "link": "https://t.me/CastleOfCatlavan/8",
            "clean": False
        },
    ],
    "Anti shipuchki": [
        {
            "name": "Xameleon client",
            "link": "https://t.me/CastleOfCatlavan/6",
            "clean": False
        }
    ],
    "Visuals": [
        {
            "name": "Zeta Visuals New",
            "link": "https://t.me/CastleOfCatlavan/3",
            "clean": True
        },
        {
            "name": "Zeta Visuals Old",
            "link": "https://t.me/CastleOfCatlavan/11",
            "clean": True
        },
        {
            "name": "Darkness Visuals 1.3(free)",
            "link": "https://t.me/CastleOfCatlavan/12",
            "clean": True
        }
    ],
    "Legit clients (1.8.9, 1.16.5 and ...)": [
        {
            "name": "Crypton client",
            "link": 'https://t.me/CastleOfCatlavan/4',
            "clean": True
        }
    ],
    "Rage clients (1.12.2, 1.16.5 and ...)": [
        {
            "name": "Minced client 1.16.5",
            "link": "https://workupload.com/file/2ZbVaJ8ppVp",
            "clean": False
        },
        {
            "name": "Minced client 1.20.1",
            "link": "https://drive.google.com/file/d/1HojtLWHMnDglFNFzTahBRQYlL1p2QdJc/view",
            "clean": False
        },
        {
            "name": "Celestial client",
            "link": "https://yougame.biz/threads/292486/",
            "clean": True
        },
        {
            "name": "Wexside client",
            "link": "https://www.mediafire.com/file/2pz6jwsz3xa7xts/wexside.zip",
            "clean": True
        },
        {
            "name": "Expensive 3.1 client",
            "link": "https://www.blast.hk/threads/208672/",
            "clean": False
        },
        {
            "name": "Expensive upgrade client",
            "link": "https://workupload.com/file/tyVPnkFRgyd",
            "clean": True
        },
        {
            "name": "RusherHack client 1.12.2",
            "link": "https://crystalpvp.ru/rusherhack/rushercrack.jar",
            "clean": True
        },
        {
            "name": "Future client 1.21.1",
            "link": "https://t.me/CastleOfCatlavan/5",
            "clean": True
        },
        {
            "name": "ThunderHack 1.21.1",
            "link": "https://t.me/CastleOfCatlavan/7",
            "clean": True
        },
    ]
}

def init_minecraft_launcher():
    if not os.path.exists(MINECRAFT_DIR):
        os.makedirs(MINECRAFT_DIR)
    
    if not os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                "profiles": {},
                "selectedProfile": None,
                "username": "Player",
                "memory": {
                    "min": 1,
                    "max": 2
                }
            }, f, indent=4)

    launcher_profiles_path = os.path.join(MINECRAFT_DIR, "launcher_profiles.json")
    if not os.path.exists(launcher_profiles_path):
        with open(launcher_profiles_path, 'w', encoding='utf-8') as f:
            json.dump({
                "profiles": {
                    "mine4rchive": {
                        "name": "mine4rchive",
                        "type": "custom"
                    }
                },
                "selectedProfile": "mine4rchive",
                "version": 3
            }, f, indent=4)

def load_profiles():
    if not os.path.exists(PROFILES_FILE):
        init_minecraft_launcher()
        return {"profiles": {}, "selectedProfile": None, "username": "Player"}
    
    with open(PROFILES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_profiles(profiles_data):
    with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
        json.dump(profiles_data, f, indent=4)

def get_minecraft_versions():
    """Получение списка доступных версий Minecraft"""
    return mclib.utils.get_version_list()

#Реккомендед фордж для каждой версии
def get_forge_versions(minecraft_version):
    recommended_forge = {
        "1.20.1": "47.2.0",  
        "1.16.5": "36.2.39", 
        "1.12.2": "14.23.5.2860", 
        "1.8.9": "11.15.1.2318" 
    }
    
    if minecraft_version in recommended_forge:
        forge_version = f"{minecraft_version}-{recommended_forge[minecraft_version]}"
        return [forge_version]
    
    try:
        all_versions = mclib.forge.find_forge_version(minecraft_version)
        # валидаем что версия строка а не отдельные символы
        valid_versions = []
        for version in all_versions:
            if "-" in version and len(version) > 5: 
                valid_versions.append(version)
        
        if valid_versions:
            return [valid_versions[0]]
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка при получении списка версий Forge: {e}{Style.RESET_ALL}")
    
    return []

def install_minecraft_version(version, callback=None):
    def progress_callback(x, y=None):
        if y is None:
            print(f"{Style.BRIGHT}Прогресс установки: {x}{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT}Прогресс установки: {x}/{y}{Style.RESET_ALL}")
            
    callback_dict = {
        "setStatus": lambda text: print(f"{Style.BRIGHT}{text}{Style.RESET_ALL}"),
        "setProgress": progress_callback,
        "setMax": lambda x: None
    }
    
    mclib.install.install_minecraft_version(version, MINECRAFT_DIR, callback=callback_dict)

def install_forge_version(minecraft_version, forge_version, callback=None):
    def progress_callback(x, y=None):
        if y is None:
            print(f"{Style.BRIGHT}Прогресс установки Forge: {x}{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT}Прогресс установки Forge: {x}/{y}{Style.RESET_ALL}")
            
    callback_dict = {
        "setStatus": lambda text: print(f"{Style.BRIGHT}{text}{Style.RESET_ALL}"),
        "setProgress": progress_callback,
        "setMax": lambda x: None
    }
    
    mclib.forge.install_forge_version(forge_version, MINECRAFT_DIR, callback=callback_dict)

def create_profile(name, version, game_directory=None, forge_version=None):
    profiles_data = load_profiles()
    
    if game_directory is None:
        game_directory = os.path.join(MINECRAFT_DIR, "profiles", name)
    
    if not os.path.exists(game_directory):
        os.makedirs(game_directory)
    
    profile_data = {
        "name": name,
        "version": version,
        "gameDirectory": game_directory,
        "forgeVersion": forge_version
    }
    
    profiles_data["profiles"][name] = profile_data
    profiles_data["selectedProfile"] = name
    
    save_profiles(profiles_data)
    return profile_data

def delete_profile(name):
    """Удаление профиля"""
    profiles_data = load_profiles()
    
    if name in profiles_data["profiles"]:
        profile = profiles_data["profiles"][name]
        
        response = input(f"{Style.BRIGHT}Удалить файлы профиля {name}? (y/n): {Style.RESET_ALL}")
        if response.lower() == 'y':
            game_dir = profile.get("gameDirectory")
            if game_dir and os.path.exists(game_dir):
                shutil.rmtree(game_dir)
        
        del profiles_data["profiles"][name]
        
        if profiles_data["selectedProfile"] == name:
            profiles_data["selectedProfile"] = next(iter(profiles_data["profiles"].keys())) if profiles_data["profiles"] else None
        
        save_profiles(profiles_data)
        return True
    
    return False

def extract_natives_from_jars(natives_dir):
    print(f"{Style.BRIGHT}Поиск и извлечение нативных библиотек из JAR'ок...{Style.RESET_ALL}")

    import zipfile

    libraries_dir = os.path.join(MINECRAFT_DIR, "libraries")
    lwjgl_jars = []
    
    for root, _, files in os.walk(libraries_dir):
        for file in files:
            if file.endswith(".jar") and ("lwjgl" in file.lower() or "platform" in file.lower()):
                lwjgl_jars.append(os.path.join(root, file))
    
    if not lwjgl_jars:
        print(f"{Style.DIM}Не найдены JAR с LWJGL в библиотеках :({Style.RESET_ALL}")
        return False
    
    print(f"{Style.DIM}Найдено: {len(lwjgl_jars)} JAR с LWJGL{Style.RESET_ALL}")

    os.makedirs(natives_dir, exist_ok=True)

    extracted_count = 0
    for jar_path in lwjgl_jars:
        try:
            with zipfile.ZipFile(jar_path, 'r') as jar:
                for file_info in jar.infolist():
                    file_name = file_info.filename.lower()
                    is_windows_dll = file_name.endswith('.dll') and ("windows" in file_name.lower() or "/native/" in file_name.lower())
                    is_linux_so = file_name.endswith('.so') and "linux" in file_name.lower() and os.name != 'nt'
                    is_mac_dylib = file_name.endswith('.dylib') and "macos" in file_name.lower() and os.name == 'posix' and sys.platform == 'darwin'
                    
                    if is_windows_dll or is_linux_so or is_mac_dylib or (file_name.endswith('.dll') and not any(x in file_name for x in ['windows', 'linux', 'macos'])):
                        base_name = os.path.basename(file_info.filename)
                        source = jar.read(file_info.filename)
                        target_path = os.path.join(natives_dir, base_name)

                        with open(target_path, 'wb') as f:
                            f.write(source)
                        
                        print(f"{Style.DIM}Извлечена библиотека: {base_name} из {os.path.basename(jar_path)}{Style.RESET_ALL}")
                        extracted_count += 1
        except Exception as e:
            print(f"{Style.DIM}Ошибка при извлечении библеотеки из {os.path.basename(jar_path)}: {e}{Style.RESET_ALL}")
    
    if extracted_count > 0:
        print(f"{Style.BRIGHT}Успешно извлечено: {extracted_count} нативных библиотек{Style.RESET_ALL}")
        return True
    else:
        print(f"{Style.BRIGHT}Не удалось извлечь нативные библиотеки :({Style.RESET_ALL}")
        return False

def download_lwjgl294_natives():
    print(f"{Style.BRIGHT}Загрузка специальных LWJGL библиотек 2.9.4 для 1.8.9...{Style.RESET_ALL}")
    
    try:
        import requests
        import tempfile
        import zipfile
        
        lwjgl_natives_dir = os.path.join(MINECRAFT_DIR, "natives", "lwjgl294")
        os.makedirs(lwjgl_natives_dir, exist_ok=True)

        lwjgl_url = "https://repo1.maven.org/maven2/org/lwjgl/lwjgl/lwjgl-platform/2.9.4-nightly-20150209/lwjgl-platform-2.9.4-nightly-20150209-natives-windows.jar"

        response = requests.get(lwjgl_url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jar") as tmp:
            tmp.write(response.content)
            tmp_path = tmp.name

        with zipfile.ZipFile(tmp_path, 'r') as jar:
            for file_info in jar.infolist():
                if file_info.filename.endswith('/'):
                    continue

                file_name = os.path.basename(file_info.filename)
                if file_name.endswith('.dll'):
                    content = jar.read(file_info.filename)

                    file_path = os.path.join(lwjgl_natives_dir, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(content)
                    
                    print(f"{Style.DIM}Извлечена библиотека: {file_name}{Style.RESET_ALL}")
        
        os.unlink(tmp_path)
        
        jinput_url = "https://repo1.maven.org/maven2/net/java/jinput/jinput-platform/2.0.5/jinput-platform-2.0.5-natives-windows.jar"
        
        response = requests.get(jinput_url)
        response.raise_for_status()
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jar") as tmp:
            tmp.write(response.content)
            tmp_path = tmp.name
        
        with zipfile.ZipFile(tmp_path, 'r') as jar:
            for file_info in jar.infolist():
                if file_info.filename.endswith('/'):
                    continue
                
                file_name = os.path.basename(file_info.filename)
                if file_name.endswith('.dll'):
                    content = jar.read(file_info.filename)
                    file_path = os.path.join(lwjgl_natives_dir, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(content)
                    
                    print(f"{Style.DIM}Извлечена библиотека jinput: {file_name}{Style.RESET_ALL}")

        os.unlink(tmp_path)
        
        required_libraries = ["lwjgl.dll", "lwjgl64.dll", "OpenAL32.dll", "OpenAL64.dll", 
                             "jinput-dx8.dll", "jinput-dx8_64.dll", "jinput-raw.dll", "jinput-raw_64.dll"]
        
        missing_libraries = []
        for lib in required_libraries:
            if not os.path.exists(os.path.join(lwjgl_natives_dir, lib)):
                missing_libraries.append(lib)
        
        if missing_libraries:
            print(f"{Style.BRIGHT}Не удалось скачать следующие библиотеки: {', '.join(missing_libraries)}{Style.RESET_ALL}")
            return False
        
        print(f"{Style.BRIGHT}Успешно скачаны и извлечены нативные библиотеки LWJGL 2.9.4{Style.RESET_ALL}")
        return lwjgl_natives_dir
    
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка при скачивании LWJGL 2.9.4: {e}{Style.RESET_ALL}")
        return False

def prepare_lwjgl_natives():
    print(f"{Style.BRIGHT}Подготовка нативных библиотек LWJGL для всех версий...{Style.RESET_ALL}")

    common_natives_dir = os.path.join(MINECRAFT_DIR, "natives")
    os.makedirs(common_natives_dir, exist_ok=True)

    natives_count = len([f for f in os.listdir(common_natives_dir) if f.endswith('.dll') or f.endswith('.so') or f.endswith('.dylib')])
    if natives_count > 0:
        print(f"{Style.BRIGHT}В общей директории уже есть {natives_count} нативных библиотек{Style.RESET_ALL}")
        return True
    
    lwjgl294_dir = download_lwjgl294_natives()
    if lwjgl294_dir and os.path.exists(lwjgl294_dir):
        for file in os.listdir(lwjgl294_dir):
            src_path = os.path.join(lwjgl294_dir, file)
            dst_path = os.path.join(common_natives_dir, file)
            shutil.copy2(src_path, dst_path)
            print(f"{Style.DIM}Скопирована библиотека: {file} в общую директорию{Style.RESET_ALL}")
    
    extracted = extract_natives_from_jars(common_natives_dir)

    if not extracted and (not lwjgl294_dir or not os.path.exists(lwjgl294_dir)):
        print(f"{Style.BRIGHT}Попытка скачать нативные библиотеки LWJGL...{Style.RESET_ALL}")
        
        try:
            import requests
            import tempfile
            import zipfile
            
            lwjgl_urls = {
                "2.9.4": "https://repo1.maven.org/maven2/org/lwjgl/lwjgl/lwjgl-platform/2.9.4-nightly-20150209/lwjgl-platform-2.9.4-nightly-20150209-natives-windows.jar",
                "3.2.2": "https://repo1.maven.org/maven2/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar",
                "3.3.1": "https://repo1.maven.org/maven2/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1.jar"
            }
            
            for version, url in lwjgl_urls.items():
                try:
                    response = requests.get(url)
                    response.raise_for_status()

                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jar") as tmp:
                        tmp.write(response.content)
                        tmp_path = tmp.name

                    with zipfile.ZipFile(tmp_path, 'r') as jar:
                        for file_info in jar.infolist():
                            file_name = file_info.filename.lower()
                            if file_name.endswith('.dll') or file_name.endswith('.so') or file_name.endswith('.dylib'):
                                base_name = os.path.basename(file_info.filename)
                                source = jar.read(file_info.filename)
                                target_path = os.path.join(common_natives_dir, base_name)
                                
                                with open(target_path, 'wb') as f:
                                    f.write(source)
                                
                                print(f"{Style.DIM}Скачана библиотека: {base_name} (LWJGL {version}){Style.RESET_ALL}")
                    
                    os.unlink(tmp_path)
                    
                except Exception as e:
                    print(f"{Style.DIM}Ошибка при скачивании LWJGL {version}: {e}{Style.RESET_ALL}")
            
            natives_count = len([f for f in os.listdir(common_natives_dir) if f.endswith('.dll') or f.endswith('.so') or f.endswith('.dylib')])
            if natives_count > 0:
                print(f"{Style.BRIGHT}Успешно скачано: {natives_count} нативных библиотек{Style.RESET_ALL}")
                return True
            else:
                print(f"{Style.BRIGHT}Не удалось скачать нативные библиотеки :( {Style.RESET_ALL}")
                return False
                
        except Exception as e:
            print(f"{Style.BRIGHT}Ошибка при скачивании нативных библиотек: {e}{Style.RESET_ALL}")
            return False
    
    return True

def launch_minecraft(profile_name=None, username=None):
    profiles_data = load_profiles()
    
    if profile_name is None:
        profile_name = profiles_data["selectedProfile"]
    
    if profile_name not in profiles_data["profiles"]:
        print(f"{Style.BRIGHT}Профиль {profile_name} не найден!{Style.RESET_ALL}")
        return False
    
    profile = profiles_data["profiles"][profile_name]
    
    if username is None:
        username = profiles_data["username"]
    
    options = mclib.utils.generate_test_options()
    
    options["username"] = username
    options["launcherVersion"] = "Mine4rchive v1.0"
    options["gameDirectory"] = profile["gameDirectory"]
    
    memory_settings = profiles_data.get("memory", {"min": 1, "max": 2})
    min_memory = memory_settings.get("min", 1)
    max_memory = memory_settings.get("max", 2)
    
    is_minecraft_189 = profile["version"] == "1.8.9"
    
    natives_dir = os.path.join(MINECRAFT_DIR, "versions", profile["version"], f"{profile['version']}-natives")
    #Проверка на майнкрафт 1.8.9 ну типа minecraft_189 это minecraft_1.8.9
    if is_minecraft_189:
        lwjgl294_dir = os.path.join(MINECRAFT_DIR, "natives", "lwjgl294")
        if os.path.exists(lwjgl294_dir) and os.listdir(lwjgl294_dir):
            natives_dir = lwjgl294_dir
            print(f"{Style.BRIGHT}Используются специальные нативные библиотеки LWJGL 2.9.4 для Minecraft 1.8.9{Style.RESET_ALL}")
    
    if not os.path.exists(natives_dir):
        natives_dir = os.path.join(MINECRAFT_DIR, "natives")

        if not os.path.exists(natives_dir) or not os.listdir(natives_dir):
            prepare_lwjgl_natives()

    if not os.path.exists(natives_dir) or not os.listdir(natives_dir):
        print(f"{Style.BRIGHT}Нативные библиотеки не найдены. Пытаемся найти и извлечь...{Style.RESET_ALL}")

        os.makedirs(natives_dir, exist_ok=True)

        extract_natives_from_jars(natives_dir)

    lwjgl64_path = os.path.join(natives_dir, "lwjgl64.dll")
    lwjgl_path = os.path.join(natives_dir, "lwjgl.dll")
    
    if not os.path.exists(lwjgl64_path) and not os.path.exists(lwjgl_path):
        print(f"{Style.BRIGHT}Критические библиотеки LWJGL не найдены! Пытаемся скачать...{Style.RESET_ALL}")

        if is_minecraft_189:
            lwjgl294_dir = download_lwjgl294_natives()
            if lwjgl294_dir and os.path.exists(lwjgl294_dir):
                natives_dir = lwjgl294_dir
                print(f"{Style.BRIGHT}Используются специальные нативные библиотеки LWJGL 2.9.4{Style.RESET_ALL}")

    options["jvmArguments"] = [
        f"-Xmx{max_memory}G",  
        f"-Xms{min_memory}G",  
        f"-Djava.library.path={natives_dir}",  
        "-XX:+UnlockExperimentalVMOptions",
        "-XX:+UseG1GC",
        "-XX:G1NewSizePercent=20",
        "-XX:G1ReservePercent=20",
        "-XX:MaxGCPauseMillis=50",
        "-XX:G1HeapRegionSize=32M"
    ]
    
    if is_minecraft_189:
        options["jvmArguments"].append("-Dorg.lwjgl.librarypath=" + natives_dir)
        options["jvmArguments"].append("-Dnet.java.games.input.librarypath=" + natives_dir)

    print(f"{Style.BRIGHT}Выделенная память: {min_memory}ГБ - {max_memory}ГБ{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Путь к нативным библиотекам: {natives_dir}{Style.RESET_ALL}")

    if os.path.exists(natives_dir):
        dll_files = [f for f in os.listdir(natives_dir) if f.endswith('.dll')]
        print(f"{Style.DIM}Найдены библиотеки: {', '.join(dll_files)}{Style.RESET_ALL}")
    
    version = profile["version"]

    forge_version_id = None
    if profile.get("forgeVersion"):
        if profile["forgeVersion"] == "direct_install":
            print(f"{Style.BRIGHT}Проверка установленных версий Minecraft и Forge...{Style.RESET_ALL}")
            
            try:
                forge_versions = mclib.utils.get_installed_versions(MINECRAFT_DIR)
                print(f"{Style.DIM}Найдено {len(forge_versions)} установленных версий:{Style.RESET_ALL}")

                for i, v in enumerate(forge_versions, 1):
                    v_id = v.get("id", "Неизвестно")
                    v_type = v.get("type", "Неизвестно")
                    print(f"{Style.DIM}{i}. {v_id} (тип: {v_type}){Style.RESET_ALL}")

                forge_mappings = {
                    "1.20.1": f"1.20.1-forge-47.2.0",
                    "1.16.5": f"1.16.5-forge-36.2.39",
                    "1.12.2": f"1.12.2-forge-14.23.5.2860",
                    "1.8.9": f"1.8.9-forge1.8.9-11.15.1.2318"
                }

                forge_installed = False
                forge_version_id = forge_mappings.get(version)
                
                for v in forge_versions:
                    v_id = v.get("id", "").lower()
                    if forge_version_id and forge_version_id.lower() in v_id:
                        print(f"{Style.BRIGHT}Найдена установленная версия Forge: {v.get('id')}{Style.RESET_ALL}")
                        version = v.get("id")
                        forge_installed = True

                        forge_natives_dir = os.path.join(MINECRAFT_DIR, "versions", version, f"{version}-natives")
                        if os.path.exists(forge_natives_dir):
                            natives_dir = forge_natives_dir
                            print(f"{Style.BRIGHT}Используются нативные библиотеки Forge: {natives_dir}{Style.RESET_ALL}")

                            for i, arg in enumerate(options["jvmArguments"]):
                                if arg.startswith("-Djava.library.path="):
                                    options["jvmArguments"][i] = f"-Djava.library.path={natives_dir}"
                                    break
                        break

                if not forge_installed and forge_version_id:
                    print(f"{Style.BRIGHT}Forge для версии {version} не найден. Попробуем установить...{Style.RESET_ALL}")
                    if install_forge_direct(version):
                        forge_versions = mclib.utils.get_installed_versions(MINECRAFT_DIR)
                        for v in forge_versions:
                            v_id = v.get("id", "").lower()
                            if forge_version_id and forge_version_id.lower() in v_id:
                                print(f"{Style.BRIGHT}Успешно установлена версия Forge: {v.get('id')}{Style.RESET_ALL}")
                                version = v.get("id")
                                forge_installed = True
                                break
                
                if not forge_installed:
                    print(f"{Style.BRIGHT}Forge не найден даже после попытки установки :({Style.RESET_ALL}")
                    print(f"{Style.BRIGHT}Может запустим Minecraft всё таки без Forge?{Style.RESET_ALL}")
                    print(f"  {Style.NORMAL}[1] Да{Style.RESET_ALL}")
                    print(f"  {Style.NORMAL}[2] Нет{Style.RESET_ALL}")
                    choice = get_user_input("Выберите опцию: ", 2)
                    
                    if choice == 2:
                        return False
            except Exception as e:
                print(f"{Style.BRIGHT}Ошибка при проверке версий: {e}{Style.RESET_ALL}")
    
    try:

        if forge_version_id:
            options["gameDirectory"] = profile["gameDirectory"]
            print(f"{Style.BRIGHT}Директория игры установлена: {options['gameDirectory']}{Style.RESET_ALL}")
            mods_dir = os.path.join(profile["gameDirectory"], "mods")
            if os.path.exists(mods_dir):
                mods_count = len([f for f in os.listdir(mods_dir) if f.endswith('.jar')])
                print(f"{Style.BRIGHT}Найдено {mods_count} модов в {mods_dir}{Style.RESET_ALL}")

                lwjgl_mods = [f for f in os.listdir(mods_dir) if "lwjgl" in f.lower()]
                if lwjgl_mods:
                    print(f"{Style.BRIGHT}Внимание! Найдены моды с LWJGL: {', '.join(lwjgl_mods)}{Style.RESET_ALL}")
                    print(f"{Style.BRIGHT}Они могут конфликтовать с системными библиотеками LWJGL{Style.RESET_ALL}")
            else:
                print(f"{Style.BRIGHT}Папка модов не найдена: {mods_dir}{Style.RESET_ALL}")

        print(f"{Style.BRIGHT}Запуск Minecraft версии {version}...{Style.RESET_ALL}")
        minecraft_command = mclib.command.get_minecraft_command(version, MINECRAFT_DIR, options)

        print(f"{Style.DIM}Команда запуска: {' '.join(minecraft_command)}{Style.RESET_ALL}")

        import subprocess
        process = subprocess.Popen(minecraft_command)
        
        print(f"{Style.BRIGHT}Minecraft запущен! (PID: {process.pid}){Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка при запуске Minecraft: {e}{Style.RESET_ALL}")
        
        if "forge" in version.lower():
            print(f"{Style.BRIGHT}Попытка запуска стандартной версии Minecraft...{Style.RESET_ALL}")
            try:
                vanilla_version = profile['version']
                minecraft_command = mclib.command.get_minecraft_command(vanilla_version, MINECRAFT_DIR, options)
                process = subprocess.Popen(minecraft_command)
                print(f"{Style.BRIGHT}Minecraft (стандартная версия) запущен! (PID: {process.pid}){Style.RESET_ALL}")
                return True
            except Exception as e2:
                print(f"{Style.BRIGHT}Ошибка при запуске стандартной версии: {e2}{Style.RESET_ALL}")
        
        return False

def install_mods(profile_name, mod_paths):
    profiles_data = load_profiles()
    
    if profile_name not in profiles_data["profiles"]:
        print(f"{Style.BRIGHT}Профиль {profile_name} не найден!{Style.RESET_ALL}")
        return False
    
    profile = profiles_data["profiles"][profile_name]
    mods_dir = os.path.join(profile["gameDirectory"], "mods")
    
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
        print(f"{Style.BRIGHT}Создана директория для модов: {mods_dir}{Style.RESET_ALL}")
    
    installed_count = 0
    for mod_path in mod_paths:
        if os.path.exists(mod_path):
            mod_name = os.path.basename(mod_path)
            try:
                if mod_path.lower().endswith('.jar'):
                    dest_path = os.path.join(mods_dir, mod_name)
                    shutil.copy(mod_path, dest_path)
                    print(f"{Style.BRIGHT}Мод {mod_name} установлен в {dest_path}{Style.RESET_ALL}")
                    installed_count += 1
                else:
                    print(f"{Style.BRIGHT}Файл {mod_name} не является JAR-файлом и был пропущен{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Style.BRIGHT}Ошибка при установке мода {mod_name}: {e}{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT}Файл не найден: {mod_path}{Style.RESET_ALL}")
    
    if installed_count > 0:
        print(f"{Style.BRIGHT}Установлено {installed_count} модов для профиля {profile_name}{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}Не удалось установить ни одного мода{Style.RESET_ALL}")
    
    return installed_count > 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_wave_color(position, total_length, offset=0):
    wave = math.sin((position + offset) * (2 * math.pi / total_length))
    intensity = (wave + 1) / 2 
    
    if intensity > 0.9:
        return Style.BRIGHT
    elif intensity > 0.7:
        return Style.BRIGHT + Style.DIM
    elif intensity > 0.5:
        return Style.NORMAL
    elif intensity > 0.3:
        return Style.DIM + Style.NORMAL
    else:
        return Style.DIM

def animate_wave_text(text, delay=0.02):
    total_length = len(text)
    frames = 50
    for frame in range(frames):
        colored_text = ''
        offset = frame * (total_length / frames)
        for j, char in enumerate(text):
            position = total_length - j
            color = get_wave_color(position, total_length, offset)
            colored_text += color + char
        print(colored_text)
        time.sleep(delay)
        sys.stdout.write("\033[F\033[K")
    print(Style.RESET_ALL + text)

def print_rainbow_logo():
    logo = """
           ,ggg,                                                                 ,ggg,         gg                                                                           &&&&&       
          dP""8I                        ,dPYb,                                  dP""Y8a        88                                                         8I              &&&&&&          
         dP   88                        IP'`Yb                                  Yb, ;88        88                                                         8I             &&&&&         
        dP    88                        I8  8I      gg                           `"''88        88                                                         8I             &&&&         
       ,8'    88                        I8 .8'      ""                               88        88                                                         8I              &&         
       d88888888    ,gggggg,    ,gggg,  I8 dPgg,    gg      ggg    gg   ,ggg,        88        88  gg,gggg,      ,gggg,gg   ,gggggg,    ,gggg,gg    ,gggg,8I   ,ggg,       &
 __   ,8"     88    dP""""8I   dP"  "Yb I8dP" "8I   88     d8tt\   88bgi8" "8i       88        88  I8P"  "Yb    dP"  "Y8I   dP""""8I   dP"  "Y8I   dP"  "Y8I  i8" "8i    ____
dP"  ,8P      Y8   ,8'    8I  i8'       I8P    I8   88    dP  I8   8I \I8, 8;/       88        88  I8'    ,8i  i8'    ,8I  ,8'    8I  i8'    ,8I  i8'    ,8I  I8, ,8I   1    1
Yb,_,dP       `8b,,dP     Y8,,d8,_    _,d8     I8,_,88,_,dP   I8, ,8I  \`Yb:/       Y8b,____,d88,,I8 _  ,d8' ,d8,   ,d8I ,dP     Y8,,d8,   ,d8b,,d8,   ,d8b, `YbadP'    1    1
 "Y8P"         `Y88P      `Y8P""Y8888PP88P     `Y88P""Y88"     "Y8P"    '8P"Y888    "Y888888P"Y8PI8 YY88888PP"Y8888P"8888P      `Y8P"Y8888P"`Y8P"Y8888P"`Y8888P"Y8889989 ''''
By 3x1t3r3z143kk(Astolfo & Femboys fan)                                                            I8                ,d8I'                                             
Original by https://github.com/undetectedcoder                                                     I8              ,dP'8I                                              
                                                                                                   I8             ,8"  8I                                              
                                                                                                   I8             I8   8I                                              
                                                                                                   I8             `8, ,8I                                              
                                                                                                   I8              `Y8P"                                               
    """
    for line in logo.split('\n'):
        if line.strip(): 
            animate_wave_text(line, 0.005)  
        else:
            print()
    print(Style.RESET_ALL)

def print_header():
    clear_screen()
    print_rainbow_logo()
    animate_wave_text("Upgraded(alpha 1.2) Build", 0.01)
    print("\n" + "="*50 + "\n")

def show_loading(message, duration=2):
    chars = cycle(['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷','⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'])
    end_time = time.time() + duration
    while time.time() < end_time:
        color = get_wave_color(int(time.time() * 20), 10) 
        sys.stdout.write(f'\r{color}{next(chars)} {message}')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\r' + ' '*50 + '\r', end='')

def show_main_menu():
    print(f"{Style.BRIGHT}Главное меню:{Style.RESET_ALL}\n")
    options = [
        "Архив клиентов",
        "Лаунчер Minecraft",
        "Выход"
    ]
    for i, option in enumerate(options, 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(options))
        print(f" {color}› {Style.NORMAL}{i}. {option}{Style.RESET_ALL}")
    print("\n" + "="*50)
    return get_user_input("Выберите опцию: ", len(options))

def show_launcher_menu():
    print(f"{Style.BRIGHT}Лаунчер Minecraft:{Style.RESET_ALL}\n")
    options = [
        "Играть",
        "Управление профилями",
        "Настройки пользователя",
        "Настройки системы",
        "Назад"
    ]
    for i, option in enumerate(options, 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(options))
        print(f" {color}› {Style.NORMAL}{i}. {option}{Style.RESET_ALL}")
    print("\n" + "="*50)
    return get_user_input("Выберите опцию: ", len(options))

def show_profile_menu():
    print(f"{Style.BRIGHT}Управление профилями:{Style.RESET_ALL}\n")
    options = [
        "Создать профиль",
        "Выбрать профиль",
        "Удалить профиль",
        "Установить моды",
        "Назад"
    ]
    for i, option in enumerate(options, 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(options))
        print(f" {color}› {Style.NORMAL}{i}. {option}{Style.RESET_ALL}")
    print("\n" + "="*50)
    return get_user_input("Выберите опцию: ", len(options))

def show_category_menu():
    print(f"{Style.BRIGHT}Доступные категории:{Style.RESET_ALL}\n")
    for i, category in enumerate(clients.keys(), 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(clients))
        print(f" {color}› {Style.NORMAL}{i}. {category}{Style.RESET_ALL}")
    print("\n" + "="*50)

def show_clients_menu(category):
    print(f"\n{Style.BRIGHT}Категория:{Style.NORMAL} {category}{Style.RESET_ALL}\n")
    for i, client in enumerate(clients[category], 1):
        time.sleep(0.1)
        clean_tag = f"{Fore.GREEN}✓ ЧИСТ" if client["clean"] else f"{Fore.RED}⚠ ВОЗМОЖНО ЗАРАЖЕНО"
        color = get_wave_color(i, len(clients[category]))
        print(f"  {color}[{i}]{Style.RESET_ALL} {clean_tag}{Style.RESET_ALL} - {Style.NORMAL}{client['name']}{Style.RESET_ALL}")
    print("\n" + "="*50)

def get_user_input(prompt, max_value):
    while True:
        try:
            value = int(input(f"\n{Style.BRIGHT}› {prompt}{Style.RESET_ALL} "))
            if 1 <= value <= max_value:
                return value
            print(f"{Style.BRIGHT}Ошибка: введите число от 1 до {max_value}{Style.RESET_ALL}")
        except ValueError:
            print(f"{Style.BRIGHT}Ошибка: введите корректное число{Style.RESET_ALL}")

def get_string_input(prompt):
    return input(f"\n{Style.BRIGHT}› {prompt}{Style.RESET_ALL} ")

def show_profiles():
    profiles_data = load_profiles()
    profiles = profiles_data["profiles"]
    
    if not profiles:
        print(f"{Style.BRIGHT}Нет созданных профилей{Style.RESET_ALL}")
        return None
    
    print(f"{Style.BRIGHT}Доступные профили:{Style.RESET_ALL}\n")
    profile_list = list(profiles.keys())
    for i, profile_name in enumerate(profile_list, 1):
        profile = profiles[profile_name]
        time.sleep(0.1)
        color = get_wave_color(i, len(profile_list))
        selected = f"{Fore.GREEN}✓" if profile_name == profiles_data["selectedProfile"] else " "
        forge = f"{Fore.YELLOW}[Forge]" if profile.get("forgeVersion") else ""
        print(f"  {color}[{i}]{Style.RESET_ALL} {selected} {Style.NORMAL}{profile_name}{Style.RESET_ALL} - {profile['version']} {forge}")
    print("\n" + "="*50)
    
    if profile_list:
        index = get_user_input("Выберите профиль: ", len(profile_list))
        return profile_list[index - 1]
    
    return None

def create_profile_menu():
    print(f"{Style.BRIGHT}Создание нового профиля{Style.RESET_ALL}\n")
    
    name = get_string_input("Введите название профиля: ")
    
    if minecraft_launcher_available: #версии майна
        main_versions = ["1.20.1", "1.16.5", "1.12.2", "1.8.9"]
        
        print(f"{Style.BRIGHT}Доступные версии Minecraft:{Style.RESET_ALL}\n")
        for i, version in enumerate(main_versions, 1):
            time.sleep(0.05)
            color = get_wave_color(i, len(main_versions))
            print(f"  {color}[{i}]{Style.RESET_ALL} {Style.NORMAL}{version}{Style.RESET_ALL}")
        print("\n" + "="*50)
        
        version_index = get_user_input("Выберите версию: ", len(main_versions))
        minecraft_version = main_versions[version_index - 1]

        print(f"{Style.BRIGHT}Использовать Forge?(для модов){Style.RESET_ALL}")
        print(f"  {Style.NORMAL}[1] Да{Style.RESET_ALL}")
        print(f"  {Style.NORMAL}[2] Нет{Style.RESET_ALL}")
        forge_choice = get_user_input("Выберите опцию: ", 2)
        
        # Создаем профиль
        profile = create_profile(name, minecraft_version, forge_version="direct_install" if forge_choice == 1 else None)
        
        print(f"{Style.BRIGHT}Профиль {name} успешно создан!{Style.RESET_ALL}")

        print(f"{Style.BRIGHT}Установка Minecraft {minecraft_version}...{Style.RESET_ALL}")
        install_minecraft_version(minecraft_version)

        if forge_choice == 1:
            print(f"{Style.BRIGHT}Начало установки Forge для {minecraft_version}...{Style.RESET_ALL}")
            install_forge_direct(minecraft_version)
        
        print(f"{Style.BRIGHT}Установка завершена!{Style.RESET_ALL}")

        game_directory = os.path.join(MINECRAFT_DIR, "profiles", name)
        mods_directory = os.path.join(game_directory, "mods")
        if not os.path.exists(mods_directory):
            os.makedirs(mods_directory)
            print(f"{Style.BRIGHT}Создана папка для модов: {mods_directory}{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}Библиотека minecraft-launcher-lib не установлена.{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}Установите её с помощью: pip install minecraft-launcher-lib{Style.RESET_ALL}")

def install_forge_direct(minecraft_version):
    forge_versions = {
        "1.20.1": "47.2.0",
        "1.16.5": "36.2.39",
        "1.12.2": "14.23.5.2860",
        "1.8.9": "11.15.1.2318"
    }
    
    if minecraft_version not in forge_versions:
        print(f"{Style.BRIGHT}Для версии {minecraft_version} нет предустановленной версии Forge{Style.RESET_ALL}")
        return False
    
    forge_version = forge_versions[minecraft_version]
    print(f"{Style.BRIGHT}Выбрана версия Forge {forge_version} для Minecraft {minecraft_version}{Style.RESET_ALL}")

    forge_mappings = {
        "1.20.1": {
            "url": f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar",
            "version_id": f"{minecraft_version}-forge-{forge_version}"
        },
        "1.16.5": {
            "url": f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar",
            "version_id": f"{minecraft_version}-forge-{forge_version}"
        },
        "1.12.2": {
            "url": f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar",
            "version_id": f"{minecraft_version}-forge-{forge_version}"
        },
        "1.8.9": {
            "url": f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}-{minecraft_version}/forge-{minecraft_version}-{forge_version}-{minecraft_version}-installer.jar",
            "version_id": f"{minecraft_version}-forge{minecraft_version}-{forge_version}-{minecraft_version}"
        }
    }
    
    if minecraft_version not in forge_mappings:
        print(f"{Style.BRIGHT}Нет данных для скачивания Forge для версии {minecraft_version}{Style.RESET_ALL}")
        return False
    
    forge_data = forge_mappings[minecraft_version]
    forge_url = forge_data["url"]
    forge_version_id = forge_data["version_id"]

    import tempfile
    import requests
    import zipfile
    import subprocess

    temp_dir = tempfile.mkdtemp()
    installer_jar = os.path.join(temp_dir, "forge-installer.jar")
    
    try:
        print(f"{Style.BRIGHT}Скачивание установщика Forge...{Style.RESET_ALL}")
        response = requests.get(forge_url, stream=True)
        response.raise_for_status()

        with open(installer_jar, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        versions_dir = os.path.join(MINECRAFT_DIR, "versions", forge_version_id)
        libraries_dir = os.path.join(MINECRAFT_DIR, "libraries")
        
        if not os.path.exists(versions_dir):
            os.makedirs(versions_dir)
        
        if not os.path.exists(libraries_dir):
            os.makedirs(libraries_dir)

        vanilla_dir = os.path.join(MINECRAFT_DIR, "versions", minecraft_version)
        if not os.path.exists(os.path.join(vanilla_dir, f"{minecraft_version}.jar")):
            print(f"{Style.BRIGHT}Установка базовой версии Minecraft...{Style.RESET_ALL}")
            mclib.install.install_minecraft_version(minecraft_version, MINECRAFT_DIR)

        print(f"{Style.BRIGHT}Извлечение файлов Forge...{Style.RESET_ALL}")
        extract_command = ["java", "-jar", installer_jar, "--extract", temp_dir]
        subprocess.run(extract_command, check=True)

        install_profile = os.path.join(temp_dir, "install_profile.json")
        version_json = os.path.join(temp_dir, "version.json")
        
        if os.path.exists(install_profile):
            print(f"{Style.BRIGHT}Найден профиль установки Forge{Style.RESET_ALL}")
            version_json_dest = os.path.join(versions_dir, f"{forge_version_id}.json")
            shutil.copy(version_json if os.path.exists(version_json) else install_profile, version_json_dest)
            universal_jar = None
            with open(install_profile, "r") as f:
                import json
                profile_data = json.load(f)
                if "libraries" in profile_data:
                    for lib in profile_data["libraries"]:
                        if "name" in lib and "forge" in lib["name"].lower():
                            parts = lib["name"].split(":")
                            if len(parts) >= 3:
                                artifact_path = "/".join(parts[0].split(".")) + "/" + parts[1] + "/" + parts[2] + "/" + parts[1] + "-" + parts[2] + ".jar"
                                universal_jar = os.path.join(libraries_dir, artifact_path)
                                break
            
            if "path" in profile_data and not universal_jar:
                universal_jar = os.path.join(libraries_dir, profile_data["path"])

            if universal_jar:
                os.makedirs(os.path.dirname(universal_jar), exist_ok=True)
                forge_jar_source = os.path.join(temp_dir, "maven", "net", "minecraftforge", "forge", f"{minecraft_version}-{forge_version}", f"forge-{minecraft_version}-{forge_version}.jar")
                
                if os.path.exists(forge_jar_source):
                    shutil.copy(forge_jar_source, universal_jar)
                else:
                    for root, _, files in os.walk(os.path.join(temp_dir, "maven")):
                        for file in files:
                            if file.endswith(".jar") and "forge" in file.lower():
                                shutil.copy(os.path.join(root, file), universal_jar)
                                break
            
            client_jar_dest = os.path.join(versions_dir, f"{forge_version_id}.jar")
            vanilla_jar = os.path.join(vanilla_dir, f"{minecraft_version}.jar")
            
            if os.path.exists(vanilla_jar):
                shutil.copy(vanilla_jar, client_jar_dest)

            print(f"{Style.BRIGHT}Установка библиотек Forge...{Style.RESET_ALL}")
            with open(install_profile, "r") as f:
                profile_data = json.load(f)
                if "libraries" in profile_data:
                    maven_dir = os.path.join(temp_dir, "maven")
                    if os.path.exists(maven_dir):
                        for root, dirs, files in os.walk(maven_dir):
                            for file in files:
                                src_path = os.path.join(root, file)
                                rel_path = os.path.relpath(src_path, maven_dir)
                                dest_path = os.path.join(libraries_dir, rel_path)
                                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                                shutil.copy(src_path, dest_path)

            launchwrapper_dir = os.path.join(libraries_dir, "net", "minecraft", "launchwrapper", "1.12")
            if not os.path.exists(launchwrapper_dir):
                os.makedirs(launchwrapper_dir, exist_ok=True)
                launchwrapper_url = "https://libraries.minecraft.net/net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar"
                launchwrapper_jar = os.path.join(launchwrapper_dir, "launchwrapper-1.12.jar")
                try:
                    response = requests.get(launchwrapper_url)
                    response.raise_for_status()
                    with open(launchwrapper_jar, "wb") as f:
                        f.write(response.content)
                    print(f"{Style.BRIGHT}Установлена библиотека LaunchWrapper{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Style.BRIGHT}Ошибка при скачивании LaunchWrapper: {e}{Style.RESET_ALL}")
            
            asm_versions = ["5.0.3", "5.2", "6.2", "7.1", "9.2"]
            for asm_version in asm_versions:
                asm_dir = os.path.join(libraries_dir, "org", "ow2", "asm", "asm", asm_version)
                if not os.path.exists(asm_dir):
                    os.makedirs(asm_dir, exist_ok=True)
                    asm_url = f"https://repo1.maven.org/maven2/org/ow2/asm/asm/{asm_version}/asm-{asm_version}.jar"
                    asm_jar = os.path.join(asm_dir, f"asm-{asm_version}.jar")
                    try:
                        response = requests.get(asm_url)
                        response.raise_for_status()
                        with open(asm_jar, "wb") as f:
                            f.write(response.content)
                        print(f"{Style.BRIGHT}Установлена библиотека ASM {asm_version}{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Style.BRIGHT}Ошибка при скачивании ASM {asm_version}: {e}{Style.RESET_ALL}")
            
            print(f"{Style.BRIGHT}Forge успешно установлен!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Style.BRIGHT}Не найден профиль установки Forge{Style.RESET_ALL}")
            return False
    
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка при установке Forge: {e}{Style.RESET_ALL}")
        return False
    finally:
        try:
            shutil.rmtree(temp_dir)
        except Exception:
            pass

def select_profile_menu():
    profile_name = show_profiles()
    if profile_name:
        profiles_data = load_profiles()
        profiles_data["selectedProfile"] = profile_name
        save_profiles(profiles_data)
        print(f"{Style.BRIGHT}Профиль {profile_name} выбран!{Style.RESET_ALL}")

def delete_profile_menu():
    profile_name = show_profiles()
    if profile_name:
        delete_profile(profile_name)
        print(f"{Style.BRIGHT}Профиль {profile_name} удален!{Style.RESET_ALL}")

def install_mods_menu():
    profile_name = show_profiles()
    if profile_name:
        print(f"{Style.BRIGHT}Установка модов для профиля {profile_name}{Style.RESET_ALL}\n")
        print(f"{Style.NORMAL}Введите полные пути к .jar файлам модов через пробел.{Style.RESET_ALL}")
        print(f"{Style.NORMAL}Пример: C:\\mods\\mod1.jar D:\\games\\mod2.jar{Style.RESET_ALL}")
        print(f"{Style.DIM}Можно перенести файл в консоль напрямую{Style.RESET_ALL}")
        
        mod_paths_input = get_string_input("Пути к модам: ")
        mod_paths = mod_paths_input.split()
        
        if mod_paths:
            install_mods(profile_name, mod_paths)
            
            profiles_data = load_profiles()
            profile = profiles_data["profiles"][profile_name]
            mods_dir = os.path.join(profile["gameDirectory"], "mods")
            if os.path.exists(mods_dir):
                mods_count = len([f for f in os.listdir(mods_dir) if f.endswith('.jar')])
                print(f"{Style.BRIGHT}Всего модов в папке: {mods_count}{Style.RESET_ALL}")
                
                if mods_count > 0:
                    print(f"{Style.BRIGHT}Хотите запустить Minecraft модами?{Style.RESET_ALL}")
                    print(f"  {Style.NORMAL}[1] Да{Style.RESET_ALL}")
                    print(f"  {Style.NORMAL}[2] Нет{Style.RESET_ALL}")
                    choice = get_user_input("Выберите опцию: ", 2)
                    
                    if choice == 1:
                        launch_minecraft(profile_name)
        else:
            print(f"{Style.BRIGHT}Не указаны пути к модам{Style.RESET_ALL}")

def settings_user_menu():
    profiles_data = load_profiles()
    current_username = profiles_data["username"]
    
    print(f"{Style.BRIGHT}Настройки пользователя{Style.RESET_ALL}\n")
    print(f"{Style.NORMAL}Текущий ник: {current_username}{Style.RESET_ALL}")
    
    new_username = get_string_input("Введите новый ник (оставьте пустым, чтобы не менять): ")
    
    if new_username:
        profiles_data["username"] = new_username
        save_profiles(profiles_data)
        print(f"{Style.BRIGHT}Ник изменен на {new_username}{Style.RESET_ALL}")

#Настраиваем память
def settings_memory_menu():
    profiles_data = load_profiles()

    if "memory" not in profiles_data:
        profiles_data["memory"] = {"min": 1, "max": 2}
    
    min_mem = profiles_data["memory"]["min"]
    max_mem = profiles_data["memory"]["max"]
    
    print(f"{Style.BRIGHT}Настройки памяти для Minecraft{Style.RESET_ALL}\n")
    print(f"{Style.NORMAL}Текущие настройки:{Style.RESET_ALL}")
    print(f"{Style.NORMAL}• Минимальная память: {min_mem} ГБ{Style.RESET_ALL}")
    print(f"{Style.NORMAL}• Максимальная память: {max_mem} ГБ{Style.RESET_ALL}")

    import psutil
    system_memory = round(psutil.virtual_memory().total / (1024**3), 1)  
    print(f"{Style.NORMAL}Доступная системная память: {system_memory} ГБ{Style.RESET_ALL}")
    print(f"{Style.DIM}Рекомендуется выделять не более 70% доступной памяти{Style.RESET_ALL}")

    memory_options = [0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16]
    valid_options = [opt for opt in memory_options if opt <= system_memory]
    
    print(f"\n{Style.BRIGHT}Выберите минимальный размер памяти (ГБ):{Style.RESET_ALL}")
    for i, mem in enumerate(valid_options, 1):
        color = get_wave_color(i, len(valid_options))
        print(f"  {color}[{i}]{Style.RESET_ALL} {Style.NORMAL}{mem} ГБ{Style.RESET_ALL}")
    
    min_choice = get_user_input("Выберите опцию: ", len(valid_options))
    new_min_mem = valid_options[min_choice - 1]
    
    print(f"\n{Style.BRIGHT}Выберите максимальный размер памяти (ГБ):{Style.RESET_ALL}")
    max_valid_options = [opt for opt in valid_options if opt >= new_min_mem]
    for i, mem in enumerate(max_valid_options, 1):
        color = get_wave_color(i, len(max_valid_options))
        print(f"  {color}[{i}]{Style.RESET_ALL} {Style.NORMAL}{mem} ГБ{Style.RESET_ALL}")
    
    max_choice = get_user_input("Выберите опцию: ", len(max_valid_options))
    new_max_mem = max_valid_options[max_choice - 1]

    profiles_data["memory"]["min"] = new_min_mem
    profiles_data["memory"]["max"] = new_max_mem
    save_profiles(profiles_data)
    
    print(f"{Style.BRIGHT}Настройки памяти сохранены:{Style.RESET_ALL}")
    print(f"{Style.NORMAL}• Минимальная память: {new_min_mem} ГБ{Style.RESET_ALL}")
    print(f"{Style.NORMAL}• Максимальная память: {new_max_mem} ГБ{Style.RESET_ALL}")

def settings_system_menu():
    print(f"{Style.BRIGHT}Системные настройки{Style.RESET_ALL}\n")
    options = [
        "Настройки памяти",
        "Назад"
    ]
    for i, option in enumerate(options, 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(options))
        print(f" {color}› {Style.NORMAL}{i}. {option}{Style.RESET_ALL}")
    print("\n" + "="*50)
    
    option = get_user_input("Выберите опцию: ", len(options))
    
    if option == 1: 
        settings_memory_menu()

def clients_menu():
    print_header()
    show_loading("Загрузка данных", 1.5)
    
    show_category_menu()
    category_index = get_user_input("Выберите номер категории: ", len(clients))
    selected_category = list(clients.keys())[category_index - 1]

    if discord_rpc:
        update_discord_rpc("Просматривает категорию", state=selected_category)
    
    show_clients_menu(selected_category)
    client_index = get_user_input("Выберите номер клиента: ", len(clients[selected_category]))
    selected_client = clients[selected_category][client_index - 1]

    if discord_rpc:
        update_discord_rpc("Скачивает клиент", state=selected_client["name"])
    
    show_loading("Открытие ссылки", 1)
    webbrowser.open_new_tab(selected_client["link"])
    
    print(f"\n{Style.BRIGHT}✓ Ссылка успешно открыта!{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}Если ссылка не открылась: \033[4m{selected_client['link']}\033[24m{Style.RESET_ALL}")
    input(f"\n{Style.BRIGHT}Нажмите Enter для возврата в главное меню...{Style.RESET_ALL}")

def launcher_menu():
    if not minecraft_launcher_available:
        print(f"{Style.BRIGHT}Библиотека minecraft-launcher-lib не установлена.{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}Установите её с помощью: pip install minecraft-launcher-lib{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}Если всё равно не работает, багрепорт сюда: {Style.RESET_ALL}")
        input(f"\n{Style.BRIGHT}Нажмите Enter для возврата в главное меню...{Style.RESET_ALL}")
        return
    
    init_minecraft_launcher()
    
    while True:
        print_header()
        show_loading("Загрузка лаунчера", 1)
        
        if discord_rpc:
            update_discord_rpc("В лаунчере", state="Выбирает действие")
        
        option = show_launcher_menu()
        
        if option == 1:  # Играть
            profiles_data = load_profiles()
            if not profiles_data["profiles"]:
                print(f"{Style.BRIGHT}Нет созданных профилей. Создайте профиль сначала.{Style.RESET_ALL}")
                input(f"\n{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
                continue
            
            profile_name = profiles_data["selectedProfile"]
            if not profile_name:
                print(f"{Style.BRIGHT}Не выбран профиль. Выберите профиль сначала.{Style.RESET_ALL}")
                input(f"\n{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
                continue
            
            print(f"{Style.BRIGHT}Запуск Minecraft с профилем {profile_name}...{Style.RESET_ALL}")
            
            if discord_rpc:
                update_discord_rpc("Играет", state=f"Профиль: {profile_name}")
            
            launch_minecraft()
            
            print(f"{Style.BRIGHT}Minecraft запущен!{Style.RESET_ALL}")
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата в меню лаунчера...{Style.RESET_ALL}")
        
        elif option == 2:  
            while True:
                print_header()
                show_loading("Загрузка профилей", 1)
                
                if discord_rpc:
                    update_discord_rpc("Управляет профилями", state="Настраивает")
                
                profile_option = show_profile_menu()
                
                if profile_option == 1:  
                    create_profile_menu()
                elif profile_option == 2:  
                    select_profile_menu()
                elif profile_option == 3:  
                    delete_profile_menu()
                elif profile_option == 4:  
                    install_mods_menu()
                elif profile_option == 5:  
                    break
                
                input(f"\n{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
        
        elif option == 3: 
            print_header()
            show_loading("Загрузка настроек", 1)
            
            if discord_rpc:
                update_discord_rpc("В настройках", state="Меняет профиль")
            
            settings_user_menu()
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата в меню лаунчера...{Style.RESET_ALL}")
        
        elif option == 4:  
            print_header()
            show_loading("Загрузка системных настроек", 1)
            
            if discord_rpc:
                update_discord_rpc("В настройках", state="Системные настройки")
            
            settings_system_menu()
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата в меню лаунчера...{Style.RESET_ALL}")
        
        elif option == 5: 
            break

def main():
    run_discord_rpc()
    
    while True:
        print_header()
        show_loading("Загрузка меню", 1)
        
        if discord_rpc:
            update_discord_rpc("В главном меню")
        
        option = show_main_menu()
        
        if option == 1:  
            clients_menu()
        elif option == 2:  
            launcher_menu()
        elif option == 3:  
            break

if __name__ == "__main__":
    main()