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
    def __init__(self, airplane, airline=None):
        self.airplane = airplane.lower()
        self.airline = airline.lower() if airline is not None else None
        self._get_airline_data()
    def _get_airline_data(self):
        """
        Retrieves airline data.
        """
        tree = ET.parse(airplanes_file_location)
        root = tree.getroot()

        queryType = "@type='" + str(self.airplane) + "'"
        queryAirline = "@airline='" + str(self.airline) + "'"
        #If airline is not given:
        if self.airline is None:
            airline = root.xpath(".//airplane[" + queryType + "]")
        #Else: if airline is given, check for both matching type & airline
        else:
            airline = root.xpath(".//airplane[" + queryType + " and " + queryAirline + "]")

        if not airline:
            airline_again = root.xpath(".//airplane[@registration='"+str(self.airplane)+"']")
            if not airline_again:
                raise(ValueError, 'Incorrect input for airplane.')
            else:
                airline = airline_again
        self.registration = airline[0].get('registration')
        self.family_type = airline[0].get('family_type')
        self.type = airline[0].get('type')
        self.airline = airline[0].get('airline')
        self.status = airline[0].get('status')
        self.engine_id = airline[0].get('engine_id')
        self.number_of_engines = airline[0].get('engine_number')
        self.first_flight = airline[0].get('first_flight')
        self.delivery_date = airline[0].get('delivery_date')
        self.plane_age = airline[0].get('plane_age')
    def __print_info(self, text, value):
        if value is not "":
            print( '{0: <23}'.format( text + ":"), value )
    def info(self):
        """
            Print out all stored info regarding aircraft
        """
        self.__print_info( "Registration", self.registration )
        self.__print_info( "Aircraft Family Type", self.family_type )
        self.__print_info( "Aircraft Type", self.type.title() )
        self.__print_info( "Airline", self.airline.title() )
        self.__print_info( "Status", self.status )
        self.__print_info( "Engine ID", self.engine_id )
        self.__print_info( "Number of Engines", self.number_of_engines )
        self.__print_info( "First Flight", self.first_flight )
        self.__print_info( "Delivery Date", self.delivery_date )
        self.__print_info( "Aircraft Age (years)", self.plane_age )