from enum import Enum

class PropertyType(str, Enum):
    SIMPLE_GARAGE = "Einfache Garage"
    UNDERGROUND_PARKING = "Tiefgaragenplatz"
    CARPORT = "Carport"

class PersonType(str, Enum):
    TENANT = "Mieter"
    LANDLORD = "Vermieter"

class ContractStatus(str, Enum):
    ACTIVE = "Aktiv"
    TERMINATED = "Beendet"
    IN_NOTICE = "In Kündigung" 