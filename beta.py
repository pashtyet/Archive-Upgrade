from colorama import init, Fore, Back, Style
import webbrowser
import time
import os
from itertools import cycle
import sys
import math
import threading
import json
import subprocess

try:
    from pypresence import Presence
    discord_rpc_available = True
except ImportError:
    discord_rpc_available = False

init(autoreset=True)
client_id = '1368298880474812519'  
discord_rpc = None
rpc_thread = None

ARCHIVE_CHEATS_FILE = os.path.join(os.path.expanduser("~"), ".mine4rchive", "ArchiveCheats.json")

def init_discord_rpc():
    global discord_rpc
    if discord_rpc_available:
        try:
            discord_rpc = Presence(client_id)
            discord_rpc.connect()
            update_discord_rpc("В главном меню")
            return True
        except Exception as e:
            print(f"{Style.DIM}Не удалось подключиться к Discord RPC:\nERROR: {e}{Style.RESET_ALL}")
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
    settings = load_client_settings()
    if not settings["discord_rpc"]:
        return
        
    if discord_rpc_available:
        global rpc_thread
        rpc_thread = threading.Thread(target=init_discord_rpc)
        rpc_thread.daemon = True
        rpc_thread.start()

clients = {
    'Sites with cheats': [
        {"name": "CHP-cheatspacks", "link": "https://cheats-pack.su/", "clean": False},
        {"name": "RockPacks", "link": "https://rockpacks.ru/", "clean": False},
        {"name": "CheatsHub", "link": "https://cheathub.tech/", "clean": True},
    ],
    "Launchers": [
        {"name": "Collapse loader", "link": "https://collapseloader.org/", "clean": True},
        {"name": "Newlauncher", "link": "https://newlauncher.ru/", "clean": False},
        {"name": "Aorus Launcher", "link": "https://t.me/CastleOfCatlavan/8", "clean": False},
    ],
    "Rp": [
        {"name": "Дубинка", "link": "https://t.me/CastleOfCatlavan/16", "clean": False}
    ],
    "Anti shipuchki": [
        {"name": "Xameleon client", "link": "https://t.me/CastleOfCatlavan/6", "clean": False}
    ],
    "Visuals": [
        {"name": "Zeta Visuals New", "link": "https://t.me/CastleOfCatlavan/3", "clean": True},
        {"name": "Zeta Visuals Old", "link": "https://t.me/CastleOfCatlavan/11", "clean": True},
        {"name": "Darkness Visuals 1.3(free)", "link": "https://t.me/CastleOfCatlavan/12", "clean": True}
    ],
    "Clients": [
        {"name": "Minced client 1.16.5", "link": "https://workupload.com/file/2ZbVaJ8ppVp", "clean": False},
        {"name": "Minced client 1.20.1", "link": "https://drive.google.com/file/d/1HojtLWHMnDglFNFzTahBRQYlL1p2QdJc/view", "clean": False},
        {"name": "Celestial client", "link": "https://yougame.biz/threads/292486/", "clean": True},
        {"name": "Wexside client", "link": "https://www.mediafire.com/file/2pz6jwsz3xa7xts/wexside.zip", "clean": True},
        {"name": "Expensive 3.1 client", "link": "https://www.blast.hk/threads/208672/", "clean": False},
        {"name": "Expensive upgrade client", "link": "https://workupload.com/file/tyVPnkFRgyd", "clean": True},
        {"name": "RusherHack client 1.12.2", "link": "https://crystalpvp.ru/rusherhack/rushercrack.jar", "clean": True},
        {"name": "Future client 1.21.1", "link": "https://t.me/CastleOfCatlavan/5", "clean": True},
        {"name": "ThunderHack 1.21.1", "link": "https://t.me/CastleOfCatlavan/7", "clean": True},
        {"name": "Delta beta", "link": "https://t.me/CastleOfCatlavan/15", "clean": False},
        {"name": "Arbuz client", "link": "https://t.me/CastleOfCatlavan/14", "clean": False},
        {"name": "DimasikDLC", "link": "https://t.me/CastleOfCatlavan/20", "clean": True},
        {"name": "Wild client", "link": "https://t.me/CastleOfCatlavan/21", "clean": True},
    ]
}

def load_archive_cheats():
    if os.path.exists(ARCHIVE_CHEATS_FILE):
        try:
            with open(ARCHIVE_CHEATS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"{Style.BRIGHT}Ошибка загрузки истории: {e}{Style.RESET_ALL}")
            return []
    return []

def save_archive_cheats(data):
    try:
        with open(ARCHIVE_CHEATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка сохранения истории: {e}{Style.RESET_ALL}")
        return False

def exe_launch_menu():
    print(f"{Style.BRIGHT}Запуск exe/bat файлов:{Style.RESET_ALL}\n")
    options = ["Запуск из истории", "Запуск по новому пути", "Назад"]
    
    for i, option in enumerate(options, 1):
        time.sleep(0.1)
        color = get_wave_color(i, len(options))
        print(f" {color}› {Style.NORMAL}{i}. {option}{Style.RESET_ALL}")
    
    print("\n" + "="*50)
    choice = get_user_input("Выберите опцию: ", len(options))
    
    if choice == 1:
        history = load_archive_cheats()
        if not history:
            print(f"{Style.BRIGHT}История пуста.{Style.RESET_ALL}")
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата...{Style.RESET_ALL}")
            return
        
        print(f"{Style.BRIGHT}История запусков:{Style.RESET_ALL}\n")
        for idx, entry in enumerate(history, 1):
            print(f"{idx}. {entry['name']} - {entry['path']}")
        
        selected = get_user_input("Выберите номер для запуска: ", len(history))
        entry = history[selected - 1]
        path = entry['path']
        
        if os.path.exists(path):
            try:
                if os.name == 'nt': os.startfile(path)
                else: subprocess.Popen([path], shell=True)
                print(f"{Style.BRIGHT}Файл запущен: {path}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Style.BRIGHT}Ошибка запуска: {e}{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT}Файл не найден: {path}{Style.RESET_ALL}")
        
        input(f"\n{Style.BRIGHT}Нажмите Enter для возврата...{Style.RESET_ALL}")
    
    elif choice == 2:
        name = get_string_input("Введите название пути: ")
        path = get_string_input("Введите полный путь к exe/bat файлу: ").strip('"')
        
        if not os.path.exists(path):
            print(f"{Style.BRIGHT}Файл не найден!{Style.RESET_ALL}")
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата...{Style.RESET_ALL}")
            return
        
        ext = os.path.splitext(path)[1].lower()
        if ext not in ('.exe', '.bat'):
            print(f"{Style.BRIGHT}Поддерживаются только exe и bat файлы!{Style.RESET_ALL}")
            input(f"\n{Style.BRIGHT}Нажмите Enter для возврата...{Style.RESET_ALL}")
            return
        
        history = load_archive_cheats()
        history.append({
            "name": name,
            "path": os.path.abspath(path),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        save_archive_cheats(history)
        
        try:
            if os.name == 'nt': os.startfile(path)
            else: subprocess.Popen([path], shell=True)
            print(f"{Style.BRIGHT}Файл запущен и сохранен в историю.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Style.BRIGHT}Ошибка запуска: {e}{Style.RESET_ALL}")
        
        input(f"\n{Style.BRIGHT}Нажмите Enter для возврата...{Style.RESET_ALL}")

def load_client_settings():
    settings_file = os.path.join(os.path.expanduser("~"), ".mine4rchive", "settings.json")
    default_settings = {
        "animations": True,
        "loading_animation": True,
        "discord_rpc": True,
    }
    
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                return {**default_settings, **json.load(f)}
        except Exception as e:
            print(f"{Style.BRIGHT}Ошибка загрузки настроек: {e}{Style.RESET_ALL}")
    return default_settings

def save_client_settings(settings):
    try:
        with open(os.path.join(os.path.expanduser("~"), ".mine4rchive", "settings.json"), 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4)
        return True
    except Exception as e:
        print(f"{Style.BRIGHT}Ошибка сохранения настроек: {e}{Style.RESET_ALL}")
        return False

def settings_client_menu():
    settings = load_client_settings()
    options = [
        ("Анимации", "animations"),
        ("Анимация загрузки", "loading_animation"),
        ("Discord RPC", "discord_rpc"),
    ]
    
    while True:
        print(f"{Style.BRIGHT}Текущие настройки:{Style.RESET_ALL}\n")
        for i, (name, key) in enumerate(options, 1):
            status = "✓ Включено" if settings[key] else "✗ Выключено"
            color = Fore.GREEN if settings[key] else Fore.RED
            print(f"  {color}[{i}]{Style.RESET_ALL} {Style.NORMAL}{name}: {status}{Style.RESET_ALL}")
        
        print(f"\n{Style.BRIGHT}Выберите настройку для изменения (0 для выхода):{Style.RESET_ALL}")
        try:
            choice = int(input(f"\n{Style.BRIGHT}› Выберите опцию: {Style.RESET_ALL}"))
            if choice == 0: break
            if 1 <= choice <= len(options):
                key = options[choice - 1][1]
                settings[key] = not settings[key]
                save_client_settings(settings)
                print(f"\n{Style.BRIGHT}Настройка {options[choice - 1][0]} {'включена' if settings[key] else 'выключена'}{Style.RESET_ALL}")
                if key == "discord_rpc":
                    if settings[key]: run_discord_rpc()
                    else:
                        global discord_rpc
                        if discord_rpc:
                            discord_rpc.close()
                            discord_rpc = None
                input(f"\n{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
        except ValueError:
            print(f"{Style.BRIGHT}Ошибка: введите корректное число{Style.RESET_ALL}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_wave_color(position, total_length, offset=0):
    wave = math.sin((position + offset) * (2 * math.pi / total_length))
    intensity = (wave + 1) / 2 
    return (
        Style.BRIGHT if intensity > 0.9 else
        Style.BRIGHT + Style.DIM if intensity > 0.7 else
        Style.NORMAL if intensity > 0.5 else
        Style.DIM + Style.NORMAL if intensity > 0.3 else
        Style.DIM
    )

def print_rainbow_logo():
    settings = load_client_settings()
    logo = """
    ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄ 
    ▐  ▄▀   ▐ █    █   █ █   █  █  █    █  ▐ █      █ █    █   █ █    █   █ █    █   █ 
      █▄▄▄▄▄  ▐     ▀▄▀  ▐   █  ▐  ▐   █     █      █ ▐     ▀▄▀  ▐     ▀▄▀  ▐     ▀▄▀  
      █    ▌       ▄▀ █      █        █      ▀▄    ▄▀      ▄▀ █       ▄▀ █       ▄▀ █  
     ▄▀▄▄▄▄       █  ▄▀   ▄▀▀▀▀▀▄   ▄▀         ▀▀▀▀       █  ▄▀      █  ▄▀      █  ▄▀  
     █    ▐     ▄▀  ▄▀   █       █ █                    ▄▀  ▄▀     ▄▀  ▄▀     ▄▀  ▄▀   
     ▐         █    ▐    ▐       ▐ ▐                   █    ▐     █    ▐     █    ▐    
    <3333 by 3x1t3r3z Archive(orig-https://github.com/undetectedcoder/mine4rchive) upgrade
    """
    if settings["animations"]:
        for line in logo.split('\n'):
            if line.strip(): 
                animate_wave_text(line, 0.005)  
            else: print()
    else: print(logo)
    print(Style.RESET_ALL)

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

def print_header():
    clear_screen()
    settings = load_client_settings()
    if settings["animations"]:
        print_rainbow_logo()
        animate_wave_text("Custom Build", 0.01)
    else:
        print("""
        ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄ 
        ▐  ▄▀   ▐ █    █   █ █   █  █  █    █  ▐ █      █ █    █   █ █    █   █ █    █   █ 
          █▄▄▄▄▄  ▐     ▀▄▀  ▐   █  ▐  ▐   █     █      █ ▐     ▀▄▀  ▐     ▀▄▀  ▐     ▀▄▀  
          █    ▌       ▄▀ █      █        █      ▀▄    ▄▀      ▄▀ █       ▄▀ █       ▄▀ █  
         ▄▀▄▄▄▄       █  ▄▀   ▄▀▀▀▀▀▄   ▄▀         ▀▀▀▀       █  ▄▀      █  ▄▀      █  ▄▀  
         █    ▐     ▄▀  ▄▀   █       █ █                    ▄▀  ▄▀     ▄▀  ▄▀     ▄▀  ▄▀   
         ▐         █    ▐    ▐       ▐ ▐                   █    ▐     █    ▐     █    ▐    
        <3333 by 3x1t3r3z Archive(orig-https://github.com/undetectedcoder/mine4rchive) upgrade
        """)
    print("\n" + "="*50 + "\n")

def show_loading(message, duration=2):
    settings = load_client_settings()
    if not settings["loading_animation"]:
        print(f"{Style.BRIGHT}{message}...{Style.RESET_ALL}")
        time.sleep(duration)
        return
        
    chars = cycle(['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'])
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
        "Запуск exe файлов",
        "Настройки",
        "Выход"
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
            if 1 <= value <= max_value: return value
            print(f"{Style.BRIGHT}Ошибка: введите число от 1 до {max_value}{Style.RESET_ALL}")
        except ValueError:
            print(f"{Style.BRIGHT}Ошибка: введите корректное число{Style.RESET_ALL}")

def get_string_input(prompt):
    return input(f"\n{Style.BRIGHT}› {prompt}{Style.RESET_ALL} ")

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

def main():
    settings = load_client_settings()
    if settings["discord_rpc"]: run_discord_rpc()
    
    while True:
        print_header()
        show_loading("Загрузка меню", 1)
        
        if discord_rpc and settings["discord_rpc"]:
            update_discord_rpc("В главном меню")
        
        option = show_main_menu()
        
        if option == 1:
            clients_menu()
        elif option == 2:
            print_header()
            show_loading("Загрузка меню запуска", 1)
            exe_launch_menu()
        elif option == 3:
            print_header()
            show_loading("Загрузка настроек", 1)
            settings_client_menu()
        elif option == 4:
            break

if __name__ == "__main__":
    main()