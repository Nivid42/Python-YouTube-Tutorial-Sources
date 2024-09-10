from ftplib import FTP

host = "ftp.beispiel.de"
user = "test"
passwort = "test"

ftp = FTP(host, user=user, passwd=passwort)

#ftp_verbindung_mit_login_methode = FTP('ftp.beispiel.de')
#ftp_verbindung_mit_login_methode.login(user=user, passwd=passwort)

ftp.mkd("neuer_ordner")

files = []
ftp.dir(files.append)
for file in files:
    print(file)

file_liste = ftp.nlst()
for file in file_liste:
    print(file)

with open('bild.jpg', 'rb') as f:
    ftp.storbinary('STOR bild.jpg', f)

with open('alte_datei.txt', 'r') as f:
        ftp.storlines('STOR alte_datei.txt', f)

with open('heruntergeladene_datei.jpg', 'wb') as f:
    ftp.retrbinary('RETR bild.jpg', f.write)

with open('heruntergeladene_datei.txt', 'w') as f:
    ftp.retrlines('RETR alte_datei.txt', lambda line: f.write(line + '\n'))

ftp.rename('alte_datei.txt', 'neue_datei.txt')

ftp.delete('neue_datei.txt')

ftp.quit()


