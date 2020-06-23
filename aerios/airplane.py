import lxml.etree as ET
# import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from copy import deepcopy
import pkgutil
my_path = os.path.abspath(os.path.dirname(__file__))
airplanes_file_location = os.path.join(my_path, "data/airplanes.xml")
class Airplane(object):
    """
    Airplane constructor.

    :param string airplane: This can be the type of the aircraft, i.e., ``boeing 747-400``, or ``airbus a380`` or its registration i.e., ``A6-EDB``. Typically, aircraft types will have the manufacturer's name first followed by a space and then the type of aircraft. 
    
    **Sample constructor initialisations**::

        import aerios as ae

        # Create an instance of the Airplane class for a boeing-747
        myairplane = Airplane('boeing-747')

        # Create an instances of the Airpane class for an aircraft with registration A6-EDB
        myairplane = Airplane('A6-EDB')

    """
    def __init__(self, airplane, airline):
        self.airplane = airplane.lower()
        self.airline = airline.lower()
        self._get_airline_data()
    def _get_airline_data(self):
        """
        Retrieves airline data.
        """
        tree = ET.parse(airplanes_file_location)
        root = tree.getroot()
        airline = root.xpath(".//airplane[@type='" + str(self.airplane) + "' and @airline='" + str(self.airline) + "']")
        if not airline:
            airline_again = root.xpath(".//airplane[@registration='"+str(self.airplane)+"']")
            if not airline_again:
                raise(ValueError, 'Incorrect input for airplane.')
            else:
                airline = airline_again
        self.engine_id = airline[0].get('engine_id')
        self.registration = airline[0].get('registration')
        self.family_type = airline[0].get('family_type')
        self.type = airline[0].get('type')
        self.status = airline[0].get('status')
        self.number_of_engines = airline[0].get('engine_number')
        self.first_flight = airline[0].get('first_flight')
        self.airline = airline[0].get('airline')