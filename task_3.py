import sys
import os
from colorama import Fore, Style

def visualize_directory_structure(directory):
    try:
        print(Fore.BLUE + "📁", os.path.abspath(directory))
        
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                print(Fore.GREEN + "┣ 📂", item)
                visualize_directory_structure(item_path)
            elif os.path.isfile(item_path):
                print(Fore.RED + "┣ 📄", item)
    
    except FileNotFoundError:
        print("Шлях не знайдено.")
    except PermissionError:
        print("У вас немає доступу до цієї директорії.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print("Введіть шлях до директорії як аргумент командного рядка.")
        return
    
    directory = sys.argv[1]
    
    visualize_directory_structure(directory)

if __name__ == "__main__":
    main()