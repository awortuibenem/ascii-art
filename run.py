import pyfiglet

def generate_ascii_art():
    print("Welcome to the ASCII Art Generator!")
    
    text = input("Enter the text you want to convert to ASCII art: ")

    ascii_art = pyfiglet.figlet_format(text)

    print("\nHere is your ASCII art:\n")
    print(ascii_art)

if __name__ == "__main__":
    generate_ascii_art()
