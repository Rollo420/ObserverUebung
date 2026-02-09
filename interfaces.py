from abc import ABC, abstractmethod

#Der Observer ist der beobachter der dadrauf wartet das er informiert wird das sich die CPU Temperatur erhöht
class Observer(ABC):
    @abstractmethod
    def update(self, message: str, observer_name: str):
        """Wird aufgerufen, wenn das Subject eine Nachricht sendet."""
        pass

#Das Subject ist das zu beobachtende Object z.B. ein Newsletter oder die CPU Temperatur 
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        """Fügt einen Beobachter hinzu."""
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """Entfernt einen Beobachter."""
        pass

    @abstractmethod
    def notify(self, message: str):
        """Benachrichtigt alle angemeldeten Beobachter."""
        pass
