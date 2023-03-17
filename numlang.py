from re import findall
from rich import print

EN = {
	"1": "",     "2": "abc", "3": "def",
	"4": "ghi",  "5": "jkl",  "6": "mno",
	"7": "pqrs", "8": "tuv",  "9": "wxyz",
}
FA = {
	"1": "", "2": "بپتث", "3": "ا",
	"4": "سشصض", "5": "دذرزژ",  "6": "جچحخ",
	"7": "نوهی", "8": "فقکگلام", "9": "طظعغ",
}

print("[green]welcome to [b]NumLang[/b] project[/green]\n\n")
lang:str = input("select a language:\n[1] EN\n[2] FA\n\n(pass = EN)>>> ")
lang:dict = FA if lang.upper() == "FA" or "2" in lang else EN

while True:
	try:
		text = input(">>> ").lower()
		parts, result, mode = findall("\d\d", text), "", "encode"
		if parts != []:
			result, mode = "".join([part[0] if int(part[1]) == 0 else lang[part[0]][int(part[1])-1] for part in parts]), "decode"
		else:
			allValues = list(map(lambda i: str(i), "".join(list(lang.values()))))
			for char in text:
				for key,val in lang.items():
					if char in val: result += key+str(val.index(char)+1)
					elif not char in allValues: result += char
	
		print(f"    [+] [b][red]{mode}[/red][/b] : {result}\n    [-] [b][blue]{'decode' if mode == 'encode' else 'encode'}[/blue][/b] : {text}")
	except IndexError: print("    [!] [i][red]ERROR: [/red][/i] Entered Input Is Invaild")
	except KeyboardInterrupt: exit()