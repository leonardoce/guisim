"""
Strings tension calculator.

Given a set of existing commercial classical guitar strings, this code will
create the actual tension for a given tuning using the given strings.

The basic formula comes from the Mersenne's laws.

f0 = (1/2L) * sqrt(F/u)

- f0 is the fundamental frequency
- L is the string length
- F is the force applied to the string
- u is the mass per unit length

Reference:
https://en.wikipedia.org/wiki/Mersenne%27s_laws
"""

import configparser
from . import notes

string_catalog = dict()
"""
This contains a mapping between each
string code and the GuitarString object
"""


class GuitarString(object):
    """
    Emulate the behavior of a classical guitar string
    """

    def __init__(self, tension, frequency, diameter, scale_length):
        self.tension = tension
        self.frequency = frequency
        self.diameter = diameter
        self.scale_length = scale_length

        # Given:
        # f0 = (1/2L) * sqrt(F/u)
        # 2L * f0 = sqrt(F/u)
        # (2L * f0)^2 = F/u
        # 1/((2L * f0)^2) = u/F
        # F/((2L * f0)^2) = u

        self.mass_per_unit_length = self.tension / pow(
            2 * self.scale_length * self.frequency, 2)

    def tension_at_frequency(self, hz):
        """
        Estimate the tension of the string maintaining the same
        mass per unit length and the same length but changing
        the emission frequency
        """

        # f0 = (1/2L) * sqrt(F/u)
        # 2L * f0 = sqrt(F/u)
        # (2L * f0)^2 = F/u
        # u * (2L * f0)^2 = F

        return self.mass_per_unit_length * pow(2 * self.scale_length * hz, 2)


class StringSet(object):
    """
    Represent a set of strings
    """

    def __init__(self, name, string_names, frequencies):
        if len(string_names) != len(frequencies):
            print(string_names)
            print(frequencies)
            raise ValueError(f'string set {name} has incoherent strings and frequencies')

        self.name = name
        self.string_names = string_names
        self.frequencies = frequencies

    def extract_report(self, file):
        """
        Create a report of the set of strings inside the given
        stream object
        """
        print(f"Set name: {self.name}", file=file)
        total_tension = 0
        for idx, name in enumerate(self.string_names):
            current_string = string_catalog[name]
            note_name = notes.find_note(self.frequencies[idx])
            tension = current_string.tension_at_frequency(self.frequencies[idx])
            total_tension += tension

            nominal_tension = current_string.tension
            stretch_factor = ((tension - nominal_tension)*100)/nominal_tension

            print(f"String {idx+1} {name} {tension:.2f} {stretch_factor:.2f}% [{note_name}]", file=file)

        print(f"Total tension: {total_tension}", file=file)
        print("---", file=file)


def main():
    # Parse the strings catalog
    parser = configparser.ConfigParser()
    parser.read('data/strings.ini')
    for section in parser.sections():
        s = GuitarString(
            float(parser.get(section, 'tension')),
            float(parser.get(section, 'frequency')),
            float(parser.get(section, 'diameter')),
            float(parser.get(section, 'scale_length')))
        string_catalog[section] = s

    # Calculate the tension of each set
    sets = configparser.ConfigParser()
    sets.read('data/string_sets.ini')
    with open('results/string_sets.txt', 'w') as f:
        for section in sets.sections():
            string_names = sets.get(section, 'strings').split(',')
            frequencies = [float(x) for x in sets.get(section, 'frequencies').split(',')]
            string_set = StringSet(section, string_names, frequencies)
            string_set.extract_report(f)
