import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(path: Path, prefix=""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            print_tree(item, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    init(autoreset=True)
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Вкажіть шлях до директорії як аргумент командного рядка!{Style.RESET_ALL}")
        sys.exit(1)

    dir_path = Path(sys.argv[1])
    if not dir_path.exists():
        print(f"{Fore.RED}Вказаний шлях не існує!{Style.RESET_ALL}")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"{Fore.RED}Вказаний шлях не є директорією!{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.BLUE}{dir_path.name}{Style.RESET_ALL}/")
    print_tree(dir_path)

if __name__ == "__main__":
    main()