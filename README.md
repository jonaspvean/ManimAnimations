## Manim animations 

This repository houses all the Python scripts for my animated scenes written in the [Manim](https://www.manim.community/) library. Manim is perhaps most known as the animation tool of choice by Grant Sanderson, aka. [3Blue1Brown](https://www.youtube.com/@3blue1brown), who is also the creator of Manim. 

In order to download the scripts here and generate the actual .mp4 files that result from these scripts:
1. run `git clone https://github.com/jonaspvean/ManimAnimations/ ManimScripts`
2. make sure to have the `Manim` Python library installed – instructions can be found [here](https://docs.manim.community/en/stable/faq/installation.html)
3. to generate the .mp4 file for a particular scene, say `AnimationScene` as defined by a function found within its corresponding scipt file, say `script.py`, one needs to run the following command:
`/path/to/manim script.py AnimationScene`
where `/path/to/manim` specifies where the executable or binary files for Manim are found on your system.
