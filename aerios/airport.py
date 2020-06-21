import numpy as np 
import pandas as pd
from aerios.readxml import Xml
class Airport:
    def __init__(self, iata_airport_code):
        self.iata_airport_code = iata_airport_code
        xmldata = Xml('airport', iata_airport_code)
        self.lattitude = xmldata.lattitude
        self.longitude = xmldata.longitude
        self.altitude = xmldata.altitude
        self.city = xmldata.city
        self.country = xmldata.country
        self.airport_name = xmldata.airport_name