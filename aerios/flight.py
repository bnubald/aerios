import numpy as np 
import pandas as pd
from aerios.readxml import Xml

class Flight(object):
    """
    Flight constructor.

    :param list airports: A list of two airports, defined as strings by their IATA codes. 
    :param string aircraft_type: The type of the aircraft, i.e., ``boeing-747-400``, or ``airbus a380``.
    :param string aircraft_registration: The aircraft registration, i.e., ``A6-EDB``. Note that this is not the manufacturer's ID.
    
    """
    def __init__(self, airports, aircraft_type=None, aircraft_registration=None): 
        if len(airports) > 2:
            raise(ValueError, 'The list airports should only have two IATA codes.')
        # Aircraft inputs!
        if aircraft_type is None:
            mode='aircraft-type'
            xmldata_airline = Xml(mode, asset_id=aircraft_type)
        elif aircraft_registration is None:
            mode = 'aircraft-registration'
            xmldata_airline = Xml(mode, asset_id=aircraft_id)
        else:
            raise(ValueError, 'You must either provide an aircraft registration or an aircraft ID, but not both.')
        self.aircraft_type = xmldata_airline.aircraft_type
        self.airline = xmldata_airline.airline
        self.status = xmldata_airline.status 
        self.engine_id = xmldata_airline.engine_id
        self.number_of_engines = xmldata_airline.number_of_engines
        self.first_flight = xmldata_airline.first_flight
        # Airport inputs!
        xmldata_airports = []
        for airport in airports:
            xmldata_airports.append( Xml(mode='airport', asset_id=airport) )
    def get_fuel_estimate(self):
        """
        Returns the fuel estimate for the flight.
        """
        return 0
    def get_trajectory(self, param1, param2):
        """
        Computes the great circle trajectory of the flight.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        return 0
    def get_pollution_levels(self):
        """Create toctree_data, used to build sidebar navigation

        :param pagename: The name of the page
        :type pagename: str
        :param templatename: The name of the templatename
        :type templatename: str
        :param context: The context
        :type context: dict
        :param doctree: A doctree
        :type doctree: docutils.nodes.document

        Add to `toctree_data` to `context` that will be available on templates.
        Although data is "global", it is called once per page because current
        page is "highlighted", and some part of TOC might be collapsed.

        :return: None
        """
        return 0
    def get_noise_levels(self):
        """
        Computes the noise levels.
        """
        return 0
        