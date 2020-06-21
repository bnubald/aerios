import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from copy import deepcopy
import pkgutil
my_path = os.path.abspath(os.path.dirname(__file__))
airports_file_location = os.path.join(my_path, "data/airports.xml")
class Airport(object):
    """
    Airport constructor.

    :param string iata_airport_code: The three character Internatioanl Air Transport Association (IATA) code assigned to a given airport.
    
    **Sample constructor initialisations**::

        import aerios as ae

        # Create an instance of the Airport class for Doha airport.
        myairport = Airport('DOH')

    """
    def __init__(self, iata_airport_code):
        self.iata_airport_code = iata_airport_code
        self._get_airport_data()
    def _get_airport_data(self):
        """
        Retrieves the entire airport data set.
        """
        tree = ET.parse(airports_file_location)
        root = tree.getroot()
        data = ET.Element('data')
        port = root.findall(".//airport[@iata='"+str(self.iata_airport_code)+"']")
        self.lattitude = float(port[0].get('lat_dec'))
        self.longitude = float(port[0].get('lon_dec'))
        self.altitude = float(port[0].get('alt'))
        self.city = str(port[0].get('city'))
        self.country = str(port[0].get('country'))
        self.airport_name = str(port[0].get('name'))