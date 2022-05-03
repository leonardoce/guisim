"""
Guitar harmonic resonance simulator.
"""

# plot "results/ten_string_yepes_guitar.csv" using 1:2:($3-1+0.1) with circles

from collections import namedtuple
import configparser
from statistics import quantiles
from . import notes


HarmonicData = namedtuple("HarmonicData", "order hz amplitude")
HarmonicContribution = namedtuple("HarmonicContribution", "order name amplitude hz")

HARMONICS_TO_CONSIDER = 9
"""
How many harmonics will be considered during the modeling
"""

RESONANCE_TOLERANCE = 2
"""
The resonance tolerance in hz. With this default setting,
this mean that an object sounding at 432hz will make an object
whose resonance is 430 start to vibrate
"""

STRING_RESONANCE_WEIGHT = 0.5
"""
Considering the acoustic pure sound of a plucked string
being "1", this is the weight of the string resonance.

"0.5" is the first resonance index, as discussed in:
https://physics.stackexchange.com/questions/563765/why-do-higher-harmonics-have-a-lower-amplitude-than-the-fundamental-frequency/563930#563930
"""

BODY_AIR_RESONANCE = 0.5
"""
Considering the acoustic pure sound of a plucked string
being "1", this is the weight of the resonance of the air
inside the instrument body.
"""

BOX_RESONANCE = 0.25
"""
Considering the acoustic pure sound of a plucked string
being "1", this is the weight of the resonance of the wooden
box of the instrument
"""


class VibratingObject(object):
    """
    This class represent a vibrating object, and can calculate
    the amplitude of acoustic resonance. This object can be anything,
    i.e. this class will be used to model a string and the body
    resonance o the guitar itself.
    """

    def __init__(self, name, base_frequency):
        """
        Creates a new object with a certain fundamental
        frequency.
        """
        self.name = name
        self.base_frequency = base_frequency
        self._calculate_harmonics()

    def _calculate_harmonics(self):
        self.harmonics = []
        # Reference:
        # https://physics.stackexchange.com/questions/563765/why-do-higher-harmonics-have-a-lower-amplitude-than-the-fundamental-frequency/563930#563930
        for x in range(1, HARMONICS_TO_CONSIDER):
            self.harmonics.append(
                HarmonicData(
                    order=x,
                    hz=self.base_frequency*x,
                    amplitude=1/(x*x)))

    def sound_amplitude(self, emitting_object):
        """
        Calculates the amplitude of the acoustic resonance for a certain
        frequency as emitted by another object.

        :param emitting_object: is the object which is the sound, and is
          used to calculate the harmonics
        """

        amplitude = 0
        contributions = []

        for base_harmonic in emitting_object.harmonics:
            for resonant_harmonic in self.harmonics:
                if _compare(base_harmonic, resonant_harmonic):
                    contribution = base_harmonic.amplitude * resonant_harmonic.amplitude
                    contributions.append(
                        HarmonicContribution(
                            order=resonant_harmonic.order,
                            name=self.name,
                            amplitude=contribution,
                            hz=resonant_harmonic.hz))
                    amplitude += contribution

        return amplitude, contributions


class StringInstrument(object):
    """
    This class models a string instrument, which is composed by a set
    of strings and a body, just like a guitar.
    """
    def __init__(self, strings_frequencies, body_resonance, box_resonance, frets):
        self.strings = [
            VibratingObject(f"String {idx+1}", hz)
            for (idx, hz) 
            in enumerate(strings_frequencies)]

        self.resonant_objects = self.strings[:]
        self.frets = frets

        body_air = VibratingObject("Body air", body_resonance)
        body_air.weight = BODY_AIR_RESONANCE
        self.resonant_objects.append(body_air)

        wooden_box = VibratingObject("Wooden box", box_resonance)
        wooden_box.weight = BOX_RESONANCE
        self.resonant_objects.append(wooden_box)

    def amplitude(self, hz, string_used):
        """
        Approximate the amplitude of a certain sound given a certain string
        instrument, used on a certain string.

        :param number hz: The frequency
        :param VibratingObject string_used: The string we use to emit the sound
        """
        contributions = []

        emitting_object = VibratingObject(string_used.name, hz)
        base = 1

        # Calculate the resonating emission of the strings and
        # of the body of the instrument
        for string in self.resonant_objects:
            if string == string_used:
                # The string we use to play will not resonate
                # by itself
                continue

            amplitude, string_contributions = string.sound_amplitude(
                emitting_object)

            # The amplitude is trimmed by half as this is a resonance
            # and not a plain sound.
            # This is a consequence of the theory of string emission
            # by resonance, considering that the VibratingObject
            # class will work by default with plucked sounds.
            # Reference:
            # https://physics.stackexchange.com/questions/563765/why-do-higher-harmonics-have-a-lower-amplitude-than-the-fundamental-frequency/563930#563930
            base += 0.5 * amplitude
            contributions += string_contributions

        return base, contributions

    def test(self, file_name, strings_count):
        """
        Approximate the amplitude of every string in this instrument,
        as fretted by passed number of bars
        :param string file_name: Where to write the test result
        :param number strings_count: The number of strings to consider
        """

        total_amplitude = 0
        contributions_counts = 0
        amplitude_collector = []

        with open(file_name, "w") as f:
            for (idx, string) in enumerate(self.strings):
                if idx >= strings_count:
                    continue
                for bar in range(self.frets+1):
                    base_hz = string.base_frequency * pow(2.0, bar/12)
                    amplitude, contributions = self.amplitude(base_hz, string)
                    total_amplitude += amplitude
                    amplitude_collector.append(amplitude)
                    contributions = sorted(contributions, key=lambda x: -x.amplitude)
                    if len(contributions) > 0:
                        contributions_counts += 1
                    print(f"{bar} {idx} {amplitude:.2f} # base:{base_hz} {contributions}", file=f)

            base_amplitude = strings_count * (self.frets+1)
            resonance_effect = total_amplitude - base_amplitude
            print(f"# total amplitude: {total_amplitude:.2f}", file=f)
            print(f"# base amplitude: {base_amplitude:.2f}", file=f)
            print(f"# resonance effect: {resonance_effect:.2f}", file=f)
            print(f"# contributions: {contributions_counts}", file=f)
            print(f"# silent notes: {base_amplitude - contributions_counts}", file=f)

            for idx, q in enumerate(quantiles(amplitude_collector, n=10, method='inclusive')):
                print(f"# amplitude deciles: {idx} {q:.2f}", file=f)


def _compare(harmonic_1, harmonic_2):
    """
    Comparison function between two harmonics
    :return: True when the two harmonic relation can oscillate
       by resonance
    """
    return notes.compare(harmonic_1.hz-harmonic_2.hz)


def main():
    config = configparser.ConfigParser()
    config.read('data/guitars.ini')
    sections = config.sections()

    for section in sections:
        string_frequencies = [float(x.strip()) for x in config[section]['strings'].split(',')]
        body_resonance = float(config[section]['body_resonance'].strip())
        box_resonance = float(config[section]['box_resonance'].strip())
        frets = int(config[section]['frets'].strip())
        played_strings = int(config[section]['played_strings'].strip())

        guitar = StringInstrument(
            string_frequencies,
            body_resonance,
            box_resonance,
            frets)
        guitar.test(f"results/{section}.csv", played_strings)
