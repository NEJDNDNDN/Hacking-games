def get_file_name(choice):
    files = {
        "1": "freefire.html",
        "2": "pubg.html",
        "3": "pes2024.html",
        "4": "facebook.html",
        "5": "twitter.html",
        "6": "onestate.html",
        "7": "instagram.html",
        "8": "roblox.html",
        "9": "fortnite.html",
        "10": "snapchat.html"
    }
    return files.get(choice)

def show_menu():
    print("Redirecting you to the developer's channel...\n")
    print("Choose the app or game:")
    print("1 - Free Fire")
    print("2 - PUBG")
    print("3 - PES 2024")
    print("4 - Facebook")
    print("5 - Twitter")
    print("6 - One State")
    print("7 - Instagram")
    print("8 - Roblox")
    print("9 - Fortnite")
    print("10 - Snapchat")

def main():
    show_menu()
    choice = input("\nEnter your choice number: ").strip()

    file_name = get_file_name(choice)
    if file_name:
        print(f"Opening: {file_name}")
        # If you want to open it in browser, uncomment the next line
        # import webbrowser; webbrowser.open(file_name)
    else:
        print("Invalid choice. Please select a number from 1 to 10.")

if __name__ == "__main__":
    main()
