#!/usr/bin/env python


# Obfuscation Marshal
def Obfuscation_Marshal(created_by="Ruben Leonardo Sigalingging."):
	from marshal import dumps
	from os import system
	system("clear")
	from pyfiglet import figlet_format
	tema=figlet_format("Obfuscation",font="slant")
	print(tema)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Rabu, 29 Juni 2022, Pukul 1:47 AM.")
	print("[!] Fungsi: Untuk Obfuscation Kode atau File Python.\n")


	file=input("[!] Enter File Name: ")
	buka_dan_baca_isi_file=open(file,"r").read()
	compile_file=compile(buka_dan_baca_isi_file,"","exec")
	# Obfuscation File Yang Sudah Dicompile.
	obfuscation=dumps(compile_file)


	# Membuat File Baru Hasil Obfuscation.
	file_baru=open("Obfuscation"+str(file),"w")
	file_baru.write("import marshal\n")
	file_baru.write("exec(marshal.loads("+repr(obfuscation)+"))")
	file_baru.write("\n")

	print(f"[!] Sukses Obfuscation File: "+str(file_baru))
Obfuscation_Marshal()