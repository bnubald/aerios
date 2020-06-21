"""Utilities for reading in an XML file."""
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from copy import deepcopy
import pkgutil
import io
my_path = os.path.abspath(os.path.dirname(__file__))
airlines = os.path.join(my_path, "data/airlines.xml")
engines = os.path.join(my_path, "data/engines.xml")
airports = os.path.join(my_path, "data/airports.xml")
fuels = os.path.join(my_path, "data/fuels.xml")

NUMBER_OF_AIRPORTS = 9300
NUMBER_OF_AIRPORT_LABELS = 19
LABELS = ['icao', 'iata', 'airport-name', 'city', 'country', 'lat_deg', 'lat_min', 'lat_sec', \
         'lat_dir', 'lon_deg', 'lon_min', 'lon_sec', 'lon_dir', 'alt', 'lat_dec', \
         'lon_dec']
NAUTICAL_MILES_INTERVALS = [125, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500,\
            5000, 5500, 6000, 7000, 8000, 85000]
class Xml:
    def __init__(self, mode, asset_id):
        self.airlines_file_location = airlines
        self.engines_file_location = engines
        self.airports_file_location = airports
        self.fuels_file_location = fuels
        self.asset_id = asset_id
        self.mode = mode
        if self.mode.lower() == 'airline':
            data = self.get_airline_data()
        elif self.mode.lower() == 'engine':
            data = self.get_engine_data()
        elif self.mode.lower() == 'airport':
            data = self.get_airport_data()
        elif self.mode.lower() == 'fuel':
            data = self.get_fuel_data()
    def get_fuel_data(self):
        """
        Retrieves the fuel vs. range graph for a particular aircraft.
        """
        tree = ET.parse(self.fuels_file_location)
        tree = ET.parse('../aerios/data/fuels.xml')
        root = tree.getroot()
        data = ET.Element('data')
        port = root.findall(".//aircraft[@aircraft_id='"+str(self.asset_id)+"']")
        nautical_miles = []
        fuel_consumption = []
        for miles in NAUTICAL_MILES_INTERVALS:
            fuel_consumption.append(float( port[0].get('miles_'+str(miles))) )
            nautical_miles.append(miles)
        self.miles_vs_fuel =  [nautical_miles, fuel_consumption]
    def get_airport_data(self):
        """
        Retrieves the entire airport data set.
        """
        tree = ET.parse(self.airports_file_location)
        root = tree.getroot()
        data = ET.Element('data')
        port = root.findall(".//airport[@iata='"+str(self.asset_id)+"']")
        self.lattitude = float(port[0].get('lat_dec'))
        self.longitude = float(port[0].get('lon_dec'))
        self.altitude = float(port[0].get('alt'))
        self.city = str(port[0].get('city'))
        self.country = str(port[0].get('country'))
        self.airport_name = str(port[0].get('name'))
    def get_airline_data(self):
        """
        Retrieves airline data.
        """
        tree = ET.parse(self.airlines_file_location)
        root = tree.getroot()
        airline = root.findall(".//airplane[@registration='"+str(self.asset_id)+"']")
        self.engine_id = airline[0].get('engine_id')
        self.aircraft_type = airline[0].get('type')
        self.status = airline[0].get('status')
        self.number_of_engines = airline[0].get('engine_number')
        self.first_flight = airline[0].get('first_flight')
        self.airline = airline[0].get('airline')