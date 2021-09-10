# SprayBottleViz

### What Is It?

I briefly worked a summer job in a restaurant, and as part of it I had to clean a lot of stuff with a spray bottle. Understandably, this was quite boring, so I got
to thinking about what the spray pattern of the bottle actually was. This is a VERY simplified visualization of that.

### How To Use It?

There are two files included, `cmd.py` and `run.py`. The file `cmd.py` was my initial jumping off point where I first made the visualization with matplotlib and
made sure my math made sense. The other file `run.py` is an extension on this with an interactive graph (still using matplotlib) as well as a GUI powered by QT5. I
used QT5 as it is a very flexible and powerful GUI Library that works fantastically cross-platform (I originally coded this program on Windows and I tested it to
make sure it works on Linux as well!). As long as you have all the python modules, you can run either file with `python3 [file]`

### How Does It Work?

I do a very simplified model of this visualization. I start by creating a circle of uniformly spaced points and I run a basic physics simulation using simple
kinematic equations. The angle of spray is effectively just changing the velocity direction, while the height and radius of the spray affect each points starting
height. 
