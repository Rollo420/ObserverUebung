from interfaces import Subject, Observer


class Newsletter(Subject):
    def __init__(self):
        """
        Initialisiert eine neue Newsletter-Instanz.

        Erstellt eine leere Liste für die Beobachter.

        Returns:
            None
        """
        self._observers = []  # Das "Adressbuch"

    
    def attach(self, observer: Observer):
        """
        Fügt einen Beobachter hinzu, falls er nicht bereits vorhanden ist.

        Args:
            observer (Observer): Der hinzuzufügende Beobachter-Instanz.

        Returns:
            None
        """
        if observer not in self._observers:
            self._observers.append(observer)
            print("System: Ein neuer Abonnent wurde hinzugefügt.")

    def detach(self, observer: Observer):
        """
        Entfernt einen Beobachter aus der Liste.

        Args:
            observer (Observer): Der zu entfernende Beobachter-Instanz.

        Returns:
            None

        Raises:
            ValueError: Wenn der Beobachter nicht in der Liste ist.
        """
        self._observers.remove(observer)
        print("System: Ein Abonnent wurde entfernt.")

    def notify(self, message):
        """
        Benachrichtigt alle angemeldeten Beobachter mit einer Nachricht.

        Args:
            message (str): Die zu sendende Nachricht.

        Returns:
            None
        """
        print(f"Newsletter: Sende Nachricht: '{message}'")
        for observer in self._observers:
            observer.update(message, observer.name)

# Konkrete Observer (Die "Zuhörer")


class EmailAbonnent(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str, observer_name: str):
        """
        Wird aufgerufen, wenn eine Nachricht empfangen wird, und sendet eine E-Mail.

        Args:
            message (str): Die empfangene Nachricht.
            observer_name (str): Der Name des Observers.

        Returns:
            None
        """
        print(
            f"📧 E-Mail erhalten von {observer_name}: Ich sende eine Mail mit dem Inhalt: {message}")


class SMSAbonnent(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str, observer_name: str):
        """
        Wird aufgerufen, wenn eine Nachricht empfangen wird, und sendet eine SMS.

        Args:
            message (str): Die empfangene Nachricht.
            observer_name (str): Der Name des Observers.

        Returns:
            None
        """
        print(f"📱 SMS erhalten von {observer_name}: Kurznachricht wird verschickt: {message}")

class CPUTempAbonnent(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str, observer_name: str):
        print(f'Die CPU Temperatur liegt bei: {message} für den observer {observer_name}')
