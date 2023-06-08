from json import loads, dumps
from hashlib import md5
from rich import print

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

db = loads(open('db.json', 'rt').read())

def get(key:str, default=None) -> any:
    db = loads(open('db.json').read())
    return db.get(key) or default

def set(key:str, value:any) -> str:
    db = loads(open('db.json').read())
    db[key] = value
    open('db.json', 'w').write(dumps(db, indent=4, ensure_ascii=False))
    return key

if __name__ == "__main__":
    while 1:
        try:
            inp, mode = input(f"{bcolors.BOLD + bcolors.OKCYAN}>>>{bcolors.ENDC} "), input(f'{bcolors.BOLD + bcolors.OKBLUE}>> mode? ([R]ead/[W]rite/[E]dit):{bcolors.ENDC} ').lower()
            if mode == "r":
                print(get(inp))
            elif mode == "e":
                print(set(*inp.split()))
            else:
                print(set(md5(inp.encode()).hexdigest(), inp))
        except KeyboardInterrupt:
            exit()
