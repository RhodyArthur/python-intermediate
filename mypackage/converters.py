# `converters.py` should contain: `celsius_to_fahrenheit(c)`, `km_to_miles(km)`, `kg_to_pounds(kg)`

def celsius_to_fahrenheit(c):
    """
    Covert temperature from celsius to fahrenheit
    :param c: temperature in celsius
    """
    return (c * 9/5) + 32

def km_to_miles(km):
    """
    convert distance from kilometers to miles
    :param km: distance in km
    """
    return km * 0.6214

def kg_to_pounds(kg):
    """
    Convert weight from kg to pounds
    :param kg: weight in kn
    """
    return kg * 2.205