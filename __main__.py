from db import get, set as store, bcolors as C
from numlang import decrypt, encrypt, EN, FA
from hashlib import md5
from random import sample
from rich import print
from re import findall

print("[green]welcome to [b]Numlang[/b] project[/green]")
lang: str = input("select a lang:\n[1] EN\n[2] FA\n\n(pass = EN)>>> ")
lang: dict = FA if lang.upper() == "FA" or "2" in lang else EN


def generateKey(length=5) -> str:
    def rnd():
        return "".join(sample([*"0123456789abcdefghijklmnopqrstuvwxyz"], length))
    res = rnd()
    while get(res) is not None:
        res = rnd()
    return res


while True:
    try:
        # Help: for edit you'll have to seperate the parts with '~' and also don't encrypt new data manually; i.e. "1xy84~new value"
        text = input(f"{C.BOLD+C.OKCYAN}>>>{C.ENDC} ").lower()

        if text != "":
            save = input(
                f"{C.BOLD+C.OKBLUE}> save? ([R]ead/[W]rite/[E]dit/[N]one):{C.ENDC} ").lower()
            parts, result, mode, saveRes = findall(
                r"\d\d", text), "", "encode", "NOT SAVED"

            # encryption
            if parts != []:
                try:
                    result, mode = decrypt(text, lang), "decode"
                except:
                    result = "UNDECRYPTABLE"
            elif text == "!fa":
                lang, result = FA, "SUCCESS"
            elif text == "!en":
                lang, result = EN, "SUCCESS"
            else:
                result = encrypt(text, lang)

             # saving in the db
            if save == "r":
                saveRes = get(text)
            elif save == "w":
                saveRes = store(generateKey(), result)
            elif save == "e":
                sections = text.split("~")
                saveRes = store(sections[0], encrypt('~'.join(sections[1:])))
            else:
                ...

            print(
                f"    [+] [b][red]{mode}[/red][/b] : {result}\n    [-] [b][blue]{'decode' if mode == 'encode' else 'encode'}[/blue][/b] : {text}\n    [†] [b][green]Save Result[/green][/b] : [u]{saveRes}[/u]")

    except EOFError:
        exit()
    except IndexError:
        print("    [!] [i][red]ERROR: [/red][/i] Entered Input Is Invaild")
    except KeyboardInterrupt:
        exit()
