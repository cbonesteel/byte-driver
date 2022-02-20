![Byte Driver](/imgs/ByteDriver_Title.png)

![hackathon](https://img.shields.io/badge/hackathon-UGAHacks7-lightgrey)
![lines](https://img.shields.io/tokei/lines/github/cbonesteel/byte-driver)
![size](https://img.shields.io/github/repo-size/cbonesteel/byte-driver)
![downloads](https://img.shields.io/github/downloads/cbonesteel/byte-driver/total)
![issues](https://img.shields.io/github/issues-raw/cbonesteel/byte-driver)
![python](https://img.shields.io/badge/python-v3.7%2B-brightgreen)
![pygame](https://img.shields.io/badge/pygame-v2.1.2-brightgreen)

Made at UGAHacks7.

Byte Driver is a top down 8-bit racer reminiscent of the games that people our age played. If you're in the mood for some time trials or you want to race with friends, Byte Driver is the game for you!

## Table of Contents

[Installing this Repo](https://github.com/cbonesteel/byte-driver#installing-this-repo)
* [Dependencies](https://github.com/cbonesteel/byte-driver#dependencies)
* [Installing and Running](https://github.com/cbonesteel/byte-driver#installing-and-running)

[Project Story](https://github.com/cbonesteel/byte-driver#project-story)
* [Inspiration](https://github.com/cbonesteel/byte-driver#inspiration)
* [What it does](https://github.com/cbonesteel/byte-driver#what-it-does)
* [How we built it](https://github.com/cbonesteel/byte-driver#how-we-built-it)
* [Challenges we ran into](https://github.com/cbonesteel/byte-driver#challenges-we-ran-into)
* [Accomplishments that we're proud of]()
* [What we learned](https://github.com/cbonesteel/byte-driver#accomplishments-that-were-proud-of)
* [What's next for Byte Driver](https://github.com/cbonesteel/byte-driver#whats-next-for-byte-driver)

[What is UGAHacks?](https://github.com/cbonesteel/byte-driver#what-is-ugahacks)

[Contributors](https://github.com/cbonesteel/byte-driver#contributors)

## Installing this Repo

### Dependencies
This game depends on python and pygame to run. Ensure you have the most recent python installation by following the instructions [here](https://www.python.org/downloads/). Once python is installed, use this command to ensure the installation is setup correctly.
``` console
~ user$ python3 --version
Python 3.7.4
```
To install pygame, run either of the commands below.
``` console
~ user$ pip3 install pygame
```
``` console
~ user$ pip3 install -r requirements.txt
```

Now that we have python and pygame installed, we will install the repo!

### Installing and Running
To install this repo, simply clone with the url above under the clone tab.
``` console
~ user$ git clone [url]
```
Once it is cloned, move into the directory and use the python command to run, or run from your favorite python ide and enjoy!
``` console
~ user$ python3 run.py
```

## Project Story

### Inspiration
With the theme being retro this year, making a retro style video game was on the table for our team. The old school racing games were something many of us had enjoyed, so a simple top down racer was our go to choice. Byte Driver strives to be an enjoyable, race against the clock, retro racing game for all ages!

### What it does
Byte Driver is a single player, time trial racing game meant for users of all ages! Race around the track attempting to beat your and other's best times!

### How we built it
We built Byte Driver on the pygame framework for python. Most game functions were built by us including, collisions, map generation from a csv, menu functions, etc. The website was built using HTML and CSS and was meant to give a retro yet modern feel to introduce our game to users and take them to the GitHub page so they can download and play the game.

### Challenges we ran into
Because pygame is a framework we didn't have the luxuries of the prebuilt libraries game engines have. Physics calculations, collision masking, csv track generation, and more was built by hand and often took a few hours of work to get working.

### Accomplishments that we're proud of
Despite our difficulties with working with pygame, we are rather proud of the features we got implemented. Collisions were our biggest challenge, taking a grueling 5 hours (from midnight to 5am) to get working properly. Needless to say, the completion of that feature was a sigh of relief.

### What we learned
From all of our difficulties with pygame, next time we will simply use a game engine. As much as python is a simple language to code with, the luxury of prebuilt libraries for the engine is something we won't pass up in the future when we have such a short time limit to work with.

### What's next for Byte Driver
The next step would be to rework and add onto the "game engine" we have built throughout the weekend. We can encapsulate some functions better and optimize some of the functions and algorithms we already use to make Byte Driver easier to develop with new features.

## What is UGAHacks?
UGAHacks is a 36 hour weekend hackathon hosted by the UGAHacks team at the University of Georgia! We build a fun project, fight in nerf wars, and enjoy plenty of good food throughout the weekend as well as many more workshops and events.

## Contributors
* [Wesley Baker](https://www.linkedin.com/in/wesley-baker-295518232/)
* [Cameron Bonesteel](https://www.linkedin.com/in/cbonesteel/)
* [Divya Ragunathan](https://www.linkedin.com/in/divya-ragunathan-2437ba1b6/)
* [Andres Rodriguez](https://www.linkedin.com/in/andres-rodriguez-831b55191/)
* [Evan Tichenor](https://www.linkedin.com/in/evan-tichenor/)

<hr/>
<small>
Byte Driver <a href="https://bytedriver.tech">bytedriver.tech</a>
</small>