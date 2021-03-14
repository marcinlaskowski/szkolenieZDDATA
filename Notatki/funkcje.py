# Wartość domyślną - name="Marek"
def get_name(surname, name="Marek"):
    return f"{name} {surname}"


print(get_name("Kowalski", "Jan"))  # Jan Kowalski
print(get_name("Kowalski"))  # Marek Kowalski


print(get_name(surname="Kowalski", name="Jan"))  # Jan Kowalski
print(get_name(name="Jan", surname="Kowalski"))  # Jan Kowalski
