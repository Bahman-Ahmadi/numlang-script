from re import findall
from rich import print

EN = {
	"0": " ",
	"1": "",     "2": "abc", "3": "def",
	"4": "ghi",  "5": "jkl",  "6": "mno",
	"7": "pqrs", "8": "tuv",  "9": "wxyz",
}
FA = {
	"0": " ",
	"1": "", "2": "بپتث", "3": "ا",
	"4": "سشصض", "5": "دذرزژ",  "6": "جچحخ",
	"7": "نوهی", "8": "فقکگلام", "9": "طظعغ",
}

def encrypt(value:str, lang:dict=EN) -> str:
	result = ""
	allValues = list(map(str, "".join(list(lang.values()))))
	for char in value:
		if char in allValues:
			for key, val in lang.items():
				if char in val:
					result += key + str(val.index(char)+1)
		else:
			result += char
	return result

def decrypt(value:str, lang:dict=EN) -> str:
	parts = findall(r"\d\d", value)
	result = "".join([part[0] if int(part[1]) == 0 else lang[part[0]][int(part[1])-1] for part in parts])
	return result

if __name__ == "__main__":
	print("[green]welcome to [b]NumLang[/b] project[/green]\n\n")
	lang:str = input("select a language:\n[1] EN\n[2] FA\n\n(pass = EN)>>> ")
	lang:dict = FA if lang.upper() == "FA" or "2" in lang else EN

	while True:
		try:
			text = input(">>> ").lower()
			parts, result, mode = findall(r"\d\d", text), "", "encode"
			if parts != []:
				result, mode = decrypt(text, lang), "decode"
			elif text == "!fa":
				lang = FA
				result = "SUCCESS"
			elif text == "!en":
				lang = EN
				result = "SUCCESS"
			else:
				result = encrypt(text, lang)
			print(f"    [+] [b][red]{mode}[/red][/b] : {result}\n    [-] [b][blue]{'decode' if mode == 'encode' else 'encode'}[/blue][/b] : {text}")
		except IndexError: print("    [!] [i][red]ERROR: [/red][/i] Entered Input Is Invaild")
		except KeyboardInterrupt: exit()
