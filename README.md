# Guitar package

This package implements an emulator that should be useful to evaluate
some guitar design parameter such as:

- number of strings
- tuning used
- body air resonance
- wooden body resonance

## Requirements

- Python 3.9 or newer to calculate the indexes
- [Gnuplot](http://www.gnuplot.info/) to plot the results

## Resonance analyser

### How to use it

The result data files can be created with:

```commandline
python3 main.py resonance
```

The results will look like:

```
0 0 1.10 # base:329.63 [HarmonicContribution(order=3, name='String 5', amplitude=0.1111111111111111, hz=330.0), HarmonicContribution(order=4, name='String 6', amplitude=0.0625, hz=329.64), HarmonicContribution(order=4, name='String 2', amplitude=0.006944444444444444, hz=987.76), HarmonicContribution(order=6, name='String 5', amplitude=0.006944444444444444, hz=660.0), HarmonicContribution(order=8, name='String 6', amplitude=0.00390625, hz=659.28)]
1 0 1.06 # base:349.2308197936545 [HarmonicContribution(order=3, name='String 8', amplitude=0.1111111111111111, hz=349.62), HarmonicContribution(order=6, name='String 8', amplitude=0.006944444444444444, hz=699.24)]
2 0 1.05 # base:369.9971649842186 [HarmonicContribution(order=4, name='String 10', amplitude=0.0625, hz=370.0), HarmonicContribution(order=3, name='String 2', amplitude=0.027777777777777776, hz=740.8199999999999), HarmonicContribution(order=8, name='String 10', amplitude=0.00390625, hz=740.0), HarmonicContribution(order=6, name='String 2', amplitude=0.001736111111111111, hz=1481.6399999999999)]
[...]
10 0 1.11 # base:587.3338889212 [HarmonicContribution(order=3, name='String 3', amplitude=0.1111111111111111, hz=588.0), HarmonicContribution(order=4, name='String 4', amplitude=0.0625, hz=587.32), HarmonicContribution(order=6, name='Body air', amplitude=0.027777777777777776, hz=588), HarmonicContribution(order=6, name='String 3', amplitude=0.006944444444444444, hz=1176.0), HarmonicContribution(order=8, name='String 4', amplitude=0.00390625, hz=1174.64)]
11 0 1.03 # base:622.2585793785332 [HarmonicContribution(order=6, name='String 9', amplitude=0.027777777777777776, hz=622.98), HarmonicContribution(order=6, name='Wooden box', amplitude=0.027777777777777776, hz=622.98)]
12 0 1.02 # base:659.26 [HarmonicContribution(order=6, name='String 5', amplitude=0.027777777777777776, hz=660.0), HarmonicContribution(order=8, name='String 6', amplitude=0.015625, hz=659.28)]
0 1 1.06 # base:246.94 [HarmonicContribution(order=3, name='String 6', amplitude=0.1111111111111111, hz=247.23), HarmonicContribution(order=3, name='String 1', amplitude=0.006944444444444444, hz=988.89), HarmonicContribution(order=6, name='String 6', amplitude=0.006944444444444444, hz=494.46), HarmonicContribution(order=8, name='String 10', amplitude=0.001736111111111111, hz=740.0)]
1 1 1.04 # base:261.6238165210844 [HarmonicContribution(order=4, name='String 7', amplitude=0.0625, hz=261.64), HarmonicContribution(order=4, name='String 3', amplitude=0.006944444444444444, hz=784.0), HarmonicContribution(order=8, name='String 7', amplitude=0.00390625, hz=523.28), HarmonicContribution(order=8, name='Body air', amplitude=0.001736111111111111, hz=784), HarmonicContribution(order=8, name='String 3', amplitude=0.00043402777777777775, hz=1568.0)]
2 1 1.06 # base:277.1807782095166 [HarmonicContribution(order=3, name='String 10', amplitude=0.1111111111111111, hz=277.5), HarmonicContribution(order=6, name='String 10', amplitude=0.006944444444444444, hz=555.0), HarmonicContribution(order=8, name='String 9', amplitude=0.001736111111111111, hz=830.64), HarmonicContribution(order=8, name='Wooden box', amplitude=0.001736111111111111, hz=830.64)]
[...]
10 1 1.10 # base:439.9970589151508 [HarmonicContribution(order=3, name='String 4', amplitude=0.1111111111111111, hz=440.49), HarmonicContribution(order=4, name='String 5', amplitude=0.0625, hz=440.0), HarmonicContribution(order=4, name='String 1', amplitude=0.006944444444444444, hz=1318.52), HarmonicContribution(order=6, name='String 4', amplitude=0.006944444444444444, hz=880.98), HarmonicContribution(order=8, name='String 5', amplitude=0.00390625, hz=880.0)]
11 1 1.03 # base:466.16064554723476 [HarmonicContribution(order=4, name='String 8', amplitude=0.0625, hz=466.16), HarmonicContribution(order=8, name='String 8', amplitude=0.00390625, hz=932.32)]
12 1 1.03 # base:493.88 [HarmonicContribution(order=3, name='String 1', amplitude=0.027777777777777776, hz=988.89), HarmonicContribution(order=6, name='String 6', amplitude=0.027777777777777776, hz=494.46)]
0 2 1.20 # base:196.0 [HarmonicContribution(order=2, name='Body air', amplitude=0.25, hz=196), HarmonicContribution(order=3, name='String 7', amplitude=0.1111111111111111, hz=196.23), HarmonicContribution(order=4, name='Body air', amplitude=0.015625, hz=392), HarmonicContribution(order=4, name='String 4', amplitude=0.006944444444444444, hz=587.32), HarmonicContribution(order=6, name='String 7', amplitude=0.006944444444444444, hz=392.46), HarmonicContribution(order=6, name='Body air', amplitude=0.0030864197530864196, hz=588), HarmonicContribution(order=8, name='Body air', amplitude=0.0009765625, hz=784), HarmonicContribution(order=8, name='String 4', amplitude=0.00043402777777777775, hz=1174.64)]
1 2 1.27 # base:207.6547664944219 [HarmonicContribution(order=2, name='String 9', amplitude=0.25, hz=207.66), HarmonicContribution(order=2, name='Wooden box', amplitude=0.25, hz=207.66), HarmonicContribution(order=4, name='String 9', amplitude=0.015625, hz=415.32), HarmonicContribution(order=4, name='Wooden box', amplitude=0.015625, hz=415.32), HarmonicContribution(order=6, name='String 9', amplitude=0.0030864197530864196, hz=622.98), HarmonicContribution(order=6, name='Wooden box', amplitude=0.0030864197530864196, hz=622.98), HarmonicContribution(order=8, name='String 9', amplitude=0.0009765625, hz=830.64), HarmonicContribution(order=8, name='Wooden box', amplitude=0.0009765625, hz=830.64)]
2 2 1.17 # base:220.0025614686371 [HarmonicContribution(order=2, name='String 5', amplitude=0.25, hz=220.0), HarmonicContribution(order=2, name='String 1', amplitude=0.027777777777777776, hz=659.26), HarmonicContribution(order=3, name='String 4', amplitude=0.027777777777777776, hz=440.49), HarmonicContribution(order=4, name='String 5', amplitude=0.015625, hz=440.0), HarmonicContribution(order=6, name='String 5', amplitude=0.0030864197530864196, hz=660.0), HarmonicContribution(order=4, name='String 1', amplitude=0.001736111111111111, hz=1318.52), HarmonicContribution(order=6, name='String 4', amplitude=0.001736111111111111, hz=880.98), HarmonicContribution(order=8, name='String 6', amplitude=0.001736111111111111, hz=659.28), HarmonicContribution(order=8, name='String 5', amplitude=0.0009765625, hz=880.0)]
3 2 1.13 # base:233.08459454053332 [HarmonicContribution(order=2, name='String 8', amplitude=0.25, hz=233.08), HarmonicContribution(order=4, name='String 8', amplitude=0.015625, hz=466.16), HarmonicContribution(order=6, name='String 8', amplitude=0.0030864197530864196, hz=699.24), HarmonicContribution(order=8, name='String 8', amplitude=0.0009765625, hz=932.32)]
[...]
# total amplitude: 93.33
# base amplitude: 78.00
# resonance effect: 15.33
# contributions: 78
# silent notes: 0
# amplitude deciles: 0 1.02
# amplitude deciles: 1 1.03
# amplitude deciles: 2 1.04
# amplitude deciles: 3 1.06
# amplitude deciles: 4 1.07
# amplitude deciles: 5 1.10
# amplitude deciles: 6 1.14
# amplitude deciles: 7 1.16
# amplitude deciles: 8 1.21
# amplitude deciles: 9 1.54
# amplitude deciles: 10 1.60
```

The initial data lines have the format:

```
<bar number> <string number> <amplitude index> # comments about the calculation method
```
- `<bar number>` is `0` for the empty string, and `1` for the first bar, etc
- `<string number>` is `0` for the first string (high e in standard tuning), 5 for the sixth 
  string (low e in the standard tuning)
- `<amplitude index>` is calculated as `1 + resonance index`: we have one point for
  sound you get when plucking the string, and a resonance index based on the whole  instrument

Following the data section, there are a few comments lines about the global behavior of the instrument:

```
# total amplitude: 93.33
# base amplitude: 78.00
# resonance effect: 15.33
# contributions: 78
# silent notes: 0
# amplitude deciles: 0 1.02
# amplitude deciles: 1 1.03
# amplitude deciles: 2 1.04
# amplitude deciles: 3 1.06
[...]
# amplitude deciles: 8 1.21
```

* `total amplitude` is the sum of the amplitudes of every note of the instrument, and
  is composed by the `resonance effect` plus the `base amplitude` (which is the one you
  obtain by just plucking the strings)
* `silent notes` is the count of notes which don't result in any resonance of the
  instrument
* `contributions` is the count of the resonance contributions by the strings or by the
  instrument itself
* `amplitude deciles` is what it tells, and is mainly a way to understand if the
  instrument is balanced or not.

### Graphics

A picture is worth a thousand words. Just use [Gnuplot](http://www.gnuplot.info/)
like in the following example:

```
$ gnuplot
gnuplot> plot "results/ten_string_yepes_guitar.csv" using 1:2:($3-1+0.1) with circles
```

### Results discussion (a.k.a. Which guitar wins?)

This the wrong question, and you'll not be able to come up with an answer.

It's way better to just look at raw data and make your idea, based on your
instrument, your repertoire and your playing style, and basically what you
like and what you don't.

And by the way, this is theory, and its main purpose is to help luthiers
devise new solution or to test an intuition.

## String set tension calculator

This tool is useful if you want to calculate the amount of force
that is applied to a guitar when you string it.

Important: tension is somewhat related but definitely 
not the same as the amount of force you need to press down the
strings. Several other factors enter the game when you need to
calculate that, such as the elasticity of the string itself.

To use this tool you need to modify the `data/string_sets.ini`
and `strings.ini` files to include your preferred set and how
you will tune the strings.

This is an excerpt of `data/strings.ini`:

```
[J4301]
tension=15.65
frequency=329.63
diameter=0.0275
scale_length=25.5906
```

These are the unit of measures:

* tension is measured in **lbs**
* the diameter and the scale length in **inches**
* the frequency is measured in **hertz**

You can specify the properties of strings using different unit
of measure, if you like. Just have a look at the examples in the
data file.

Every string set is described in `data/string_sets.ini`:

```
[daddario_ej45]
strings=J4501,J4502,J4503,J4504,J4505,J4506
frequencies=329.63,246.94,196.00,146.83,110.00,82.41

[daddario_ej46_scale_63_5]
strings=J4601,J4602,J4603,J4604,J4605,J4606
frequencies=329.63,246.94,196.00,146.83,110.00,82.41
scale_length=25
```

By defining a custom string set, you can calculate the tension resulting
from the strings under the conditions specified. You can change the
fundamental frequency of the string and the string length.

To start the string tension calculator you can use:

```
python3 main.py strings
```

The results are stored in `results/string_sets.txt` in the following
format:

```
Set name: composite_yepes_daddario
String 1 J4501 16.23 0.00%
String 2 J4502 12.04 0.00%
String 3 J4503 11.88 0.00%
String 4 J4504 15.62 0.00%
String 5 J4505 15.89 0.00%
String 6 J4506 14.19 0.00%
String 7 J4606 9.58 -37.00%
String 8 J4305 15.51 12.24%
String 9 J4605 15.11 -10.90%
String 10 J4306 16.43 25.99%
Total tension: 142.4835898521798
```

The total tension is calculated with the tension of every string, and the
stretch factor over the intended tension.

This is useful to check how your strings will react with a different tuning
and/or a different scale length, and will give an indication of the
difference between the work tension the string was designed for and the
one you'll adopt.

We don't take into account the actual **anharmonicity Constant** of the
materials used to build the string but just the variation on the string
tension, and we don't take into account the actual breaking tension of
the string.

## References

I used several references as source for the formulas and the behavior
of the model. The following is an incomplete list:

- http://classicalguitar101.org/tune-your-classical-guitar.html#.YmkMePNBxz8
- https://pages.mtu.edu/~suits/NoteFreqCalcs.html
- https://www.classicalguitardelcamp.com/viewtopic.php?t=36049
- https://www.andreasaba.com/DIdattica/acustica/dispensa%20di%20acustica.pdf
- https://en.wikipedia.org/wiki/Mersenne%27s_laws
- https://www.yamaha.com/en/musical_instrument_guide/acoustic_guitar/mechanism/mechanism004.html