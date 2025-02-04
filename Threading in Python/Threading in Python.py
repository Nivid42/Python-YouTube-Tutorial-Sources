import time
import threading

def datei_download(name, dauer):
    """Simuliert das Herunterladen einer Datei"""
    print(f"Starte Download: {name}...")
    time.sleep(dauer)  # Simuliert die Download-Zeit
    print(f"{name} fertig!")

#SEQUENTIELLE VERSION (nacheinander)
start_time = time.time()

datei_download("Datei 1", 3)
datei_download("Datei 2", 3)

print(f"Sequentielle Laufzeit: {time.time() - start_time:.2f} Sekunden\n")

#PARALLELE VERSION (gleichzeitig mit Threads)
start_time = time.time()

thread1 = threading.Thread(target=datei_download, args=("Datei 1", 3))
thread2 = threading.Thread(target=datei_download, args=("Datei 2", 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Parallele Laufzeit: {time.time() - start_time:.2f} Sekunden")
