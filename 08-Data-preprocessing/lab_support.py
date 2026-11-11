"""Small notebook support; contains no preprocessing or modelling solution."""


def ready(*values, language="cs"):  # Kontrola doplnění / Check completion.
    complete = all(value is not None for value in values)  # None značí TODO / None marks a TODO.
    if not complete:  # Zatím chybí řešení / A solution is still missing.
        message = {  # Jazyk hlášky / Message language.
            "cs": "Zatím nedoplněno: nejprve vyřešte příslušnou buňku TODO.",
            "en": "Not completed yet: finish the corresponding TODO cell first.",
        }
        print(message.get(language, message["en"]))  # Srozumitelná výzva / Short prompt.
    return complete  # Kontrola se spustí až po doplnění / Run checks only after completion.
