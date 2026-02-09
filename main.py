from logic import Newsletter, EmailAbonnent, SMSAbonnent, CPUTempAbonnent
import wmi
import time


def get_windows_cpu_temp():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        # Wir greifen direkt auf das erste Element der Liste zu
        temp_data = w.MSAcpi_ThermalZoneTemperature()[0]

        # Umrechnung und direktes Return
        return (temp_data.CurrentTemperature / 10.0) - 273.15

    except Exception:
        # Falls kein Sensor gefunden wird oder Admin-Rechte fehlen
        return None


if __name__ == "__main__":
    get_windows_cpu_temp()

# 1. Das Subject erstellen
mein_newsletter = Newsletter()

# 2. Observer erstellen
kunde_a = EmailAbonnent("Kunde A")
kunde_b = SMSAbonnent("Kunde B")

# 3. Observer beim Subject anmelden (attach)
mein_newsletter.attach(kunde_a)
mein_newsletter.attach(kunde_b)

# 4. Eine Änderung auslösen (notify)
print("\n--- Erste Benachrichtigung ---")
mein_newsletter.notify("Der neue LS25 ist da!")

# 5. Einen Observer entfernen
print("\n--- Update der Liste ---")
mein_newsletter.detach(kunde_a)

# 6. Erneute Benachrichtigung
print("\n--- Zweite Benachrichtigung ---")
mein_newsletter.notify("Rabattaktion im Shop!")


print('\n--- CPU Temp Benachrichtigung --- mit neuen Subject und observer ')

print(f'erstelle Subject für die CPU Temp.')
CPU_subject = Newsletter()

print(f'\nErstelle Handy, PC und Tablet Observer')
HandyObserver = CPUTempAbonnent("Handy")
PCObserver = CPUTempAbonnent("PC")
TabletObserver = CPUTempAbonnent("Tablet")

print(f'\nFüge die Observer den Subject (CPU_subject) hinzu')
CPU_subject.attach(HandyObserver)
CPU_subject.attach(PCObserver)
CPU_subject.attach(TabletObserver)

lastCPUTemp = 0.0
currentCPUTemp = 0.0
while True:
   # time.sleep(1)
    currentCPUTemp = get_windows_cpu_temp()
    if currentCPUTemp != lastCPUTemp:
        lastCPUTemp = currentCPUTemp
        if currentCPUTemp != None:
            print(f'\nSende Nachrichten an die Observer falls sich die Temp. geändet hat')
            CPU_subject.notify(currentCPUTemp)
        else:
            print(f'Die aktuelle Temp. ist None')