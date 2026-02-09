# TODO for Observer Name Implementation

- [x] Update interfaces.py: Change Observer.update to take observer_name: str
- [x] Update logic.py: Add __init__ to EmailAbonnent, SMSAbonnent, CPUTempAbonnent to set self.name
- [x] Update logic.py: Update update methods in all Observer classes to print with observer_name
- [x] Update logic.py: In Newsletter.notify, pass observer.name to update
- [x] Update main.py: Create Observer instances with names
- [ ] Test the implementation by running main.py
