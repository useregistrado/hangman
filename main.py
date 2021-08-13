import model as m
import os


def get_frame(attempts):
    frame = ""
    with open(f"./frames/{attempts}.txt", encoding="utf-8") as f:
        for line in f:
            frame += line
    f.close()
    print(frame)


if __name__ == "__main__":
    m.__main__()
    hangman = """
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █  ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █  ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░    ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░          ░ 
                                                                                
"""
    os.system("cls")
    print(hangman)
    while True:

        c = input("\nEnter a letter or # to exit: ")
        os.system("cls")
        print()
        print(hangman)
        # os.system("clear")
        if c == "#":
            break
        last_word, result, failed_attempts = m.view(c)
        print("")
        get_frame(failed_attempts)
        if failed_attempts == 10:
            input("\npress any key to continue...")
            break

        list(map(lambda x: print(x, end=" "), last_word))
        msg = ("\nGOOD", "\nYOU FAILED")[result]
        print(msg)
        print("FAILED ATTEMPTS: ", failed_attempts)

    os.system("cls")
    #os.system("clear")

    msg_ended = ""
    with open("./msg.txt", encoding="utf-8") as f:
        for line in f:
            msg_ended += line
    f.close()

    print(msg_ended)
