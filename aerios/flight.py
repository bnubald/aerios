import numpy as np 
import pandas as pd
from aerios.airport import Airport
from aerios.airplane import Airplane
from math import radians
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pkgutil
import os
my_path = os.path.abspath(os.path.dirname(__file__))
fuels_file_location = os.path.join(my_path, "data/fuels.xml")
NAUTICAL_MILES_INTERVALS = [125, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500,\
            5000, 5500, 6000, 7000, 8000, 85000]
class Flight(object):
    """
    Flight constructor.

    :param list airports: A list of two airports, defined as strings by their IATA codes. The first airport denotes the ``origin``, whilst the second airport denotes the ``destination``. An example of this input is ``['DOH', 'DCA']``.
    :param string airplane: This can be the type of the aircraft, i.e., ``boeing 747-400``, or ``airbus a380`` or its registration i.e., ``A6-EDB``. Typically, aircraft types will have the manufacturer's name first followed by a space and then the type of aircraft. 
    
    **Sample constructor initialisations**::

        import aerios as ae

        # Create a flight between Doha and Washington-Regean for aircraft registration A6-EDB
        myflight = ae.Flight(airports=['DOH', 'DCA'], airplane='A6-EDB')

        # Create a flight between London Heathrow and Paris Orly for a boeing 737
        myflight = ae.Flight(airports=['LHR', 'ORY'], airplane='boeing 737')

    """
    def __init__(self, airports, airplane): 
        self.origin = Airport(airports[0])
        self.destination = Airport(airports[1])
        self.myplane = Airplane(airplane)
    def get_fuel_estimate(self, output='kg'):
        """
        Returns the fuel estimate for the flight.

        :param Flight self: An instance of the Flight class.
        :param string output: An input to specify whether the fuel estimate is given as ``kg`` or ``pounds``; default is the former.
        """
        # Using the standard great circle formula!
        [miles, fuel] = self.get_fuel_data()
        lon1, lat1, lon2, lat2 = map(radians, [self.origin.longitude, self.origin.lattitude, self.destination.longitude, self.destination.lattitude])
        great_circle_distance =  3958.756 * ( np.arccos( np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(lon1 - lon2)) )
    def get_fuel_data(self):
        """
        Retrieves the fuel vs. range graph for a particular aircraft.

        :param Flight self: An instance of the Flight class.
        """
        tree = ET.parse(fuels_file_location)
        root = tree.getroot()
        print(self.myplane.type)
        port = root.findall(".//aircraft[@aircraft_type'"+self.myplane.type+"']")
        print(port[0])
        nautical_miles = []
        fuel_consumption = []
        for miles in NAUTICAL_MILES_INTERVALS:
            try:
                fuel_consumption.append(float( port[0].get('miles_'+str(miles))) )
                nautical_miles.append(miles)
            except IndexError as error:
                print('Error')
        return [nautical_miles, fuel_consumption]