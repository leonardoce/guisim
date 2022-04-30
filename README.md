# Guitar package

This package implements an emulator that should be useful to evaluate
some guitar design parameter such as:

- number of strings
- tuning used
- body air resonance
- boxen body resonance

## Requirements

- Python 3.9 or newer to calculate the indexes
- [Gnuplot](http://www.gnuplot.info/) to plot the results

## How to use it

The result data files can be created with:

```commandline
python harmonics.py
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

## Results discussion (a.k.a. Which guitar wins?)

This the wrong question, and you'll not be able to come up with an answer.

It's way better to just look at raw data and make your idea, based on your
instrument, your repertoire and your playing style, and basically what you
like and what you don't.

## References

I used several references as source for the formulas and the behavior
of the model. The following is an incomplete list:

- http://classicalguitar101.org/tune-your-classical-guitar.html#.YmkMePNBxz8
- https://pages.mtu.edu/~suits/NoteFreqCalcs.html
- https://www.classicalguitardelcamp.com/viewtopic.php?t=36049