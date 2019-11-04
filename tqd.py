#-*-coding: utf-8-*-
# from argparse import argument parser
from json import dumps,loads
from getpass import getpass
from tqdm import tqdm
import os
class main:
    def __init__(self):
        self.recursses = loads(open("recurse.json","r").read())
        self.base_path = self.recursses["termux_base_path"]
        self.scannable_dir = self.recursses["only_not_scannable_dir"]
        self.start_scann_path = os.path.join(base_path,"storage")
        self.start_scann = [x for x in os.listdir(self.start_scann_path)]
        self.crypto_dirs = self.recursses["crypto_dirs_order"]
        self.scann = self.scann_dir()
        self.counter = 3
    def banner(self):
        s = getpass("escribe tu contraseña:")
        if s == self.recursses["passwors"]:
            pass
        else:
            print("te quedan: {self.counter - 1} intentos")
            self.counter = self.counter -1
            if self.counter == 0:
                print("maximo limite alcanzado, intenta de nuevo en 10 minutos ...")
                exit(sleep(10))
            return self.banner()
    def comprobate(self):
        if os.path.isdir(self.base_path) == False:
            raise NameError(f"no se localizo el directorio {self.base_path}")
        for x in self.scannable_dir:
            if os.path.isdir(x):
                pass
            elif os.path.exists(x):
                pass
            else:
                raise NameError(f"dir: {x} not_found ... ")
    def scann_dir(self):
        with open(os.path.join(self.base_path,"scan_archs.json"),"w") as file_scan:
            for x in self.startscan:
                pwd = os.path.join(self.start_scann_path,x)
                for rutabs,direct,archive in os.walk(pwd):
                    file_scan.write({"pattherns":[str(rutabs),str(direct),str(archive)]})
        return os.path.join(self.base_path,"scan_archs.json")
    def printdir(self):
        with open(self.scann,"r") as file:
            resp = loads(file)
            code = [ compile(resp[x]) for x in resp["pattherns"]]
            for x in code:
                for z in x:
                    if self.crypto_dirs:
                        print(z)
                    else:
                        if z.startswith(".") or z.endswith("."):
                            pass
if __name__ == "__main__":
    mk = main()
    mk.banner()
    mk.printdir()
