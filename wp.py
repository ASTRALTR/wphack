import os
import time

os.system("clear")

banner="""
'##:::::'##::'#######::'########::'########::'########::'########::'########::'######:::'######::
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##.... ##: ##.... ##: ##.....::'##... ##:'##... ##:
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::..:: ##:::..::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ########:: ########:: ######:::. ######::. ######::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##.....::: ##.. ##::: ##...:::::..... ##::..... ##:
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##:::::::: ##::. ##:: ##:::::::'##::: ##:'##::: ##:
. ###. ###::. #######:: ##:::. ##: ########:: ##:::::::: ##:::. ##: ########:. ######::. ######::
:...::...::::.......:::..:::::..::........:::..:::::::::..:::::..::........:::......::::......:::

"""


print(banner)

print("""

1-Wordpress Site Tarama Yap Bilgi topla.
2-Wordpress Kullanıcılarını bul.
3-Wordress Brute Force.


""")

işlem=input("HEDEF İŞLEM NUMARASI ==> ")
	

if (işlem=="1"):
	os.system("clear")
	url=input("Hedef Domain Veya ip Adres ==> ")
	print("Hedef sistemden bilgi toplanıyor")
	time.sleep(2)
	os.system("clear && wpscan --url "+url)
	input("Tarama sonlandırıldı , Herhangi bir tuşa basın.")
	

if (işlem=="2"):
	os.system("clear")
	url_one=input("Hedef Domain veya ip adres ==> ")
	print("Hedef Sistemdeki Kullanıcılar bulunuyor")
	time.sleep(2)
	os.system("wpscan --url "+url_one+" --enumerate u")
	input("Tarama sonlandırıldı , Herhangi bir tuşa basın.")

if (işlem=="3"):
	os.system("clear")
	url_two=input("Hedef Domain veya ip adres ==> ")
	username=input("Hedef user wordlist yolu ==> ")
	password=input("Hedef password wordlist yolu ==> ")
	time.sleep(2)
	os.system("clear && wpscan --url "+url_two+" --passwords "+password+" --usernames "+username+" ")
	input("Brute force Tamamlandı, Herhangi bir tuşa basın.")




else : 
	print("Çıkış Yapılıyor..")
	time.sleep(2)
	os.system("clear && python3 wp.py")

