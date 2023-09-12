# Exercise 04: applications of analog input

[Exercise Python script](./exercise04.py)

[Exercise 04 Questions](#questions)

Taking what we learned in the prior exercises, let's prepare the exercise04.py script for a quality program.
Connect the photocell using the 10k ohm resistor as a voltage divider [circuit](../doc/circuit.md).


## Questions

Let's calibrate the light sensor to be meaningful.
If you don't want to put a light calibration app on your phone that's fine.
Instead we could experiment to find the max_bright and min_bright values that:

* max_bright: make the LED duty cycle about 100% when in bright light (sunlight, room light) MEASURED VALUE: 45195
* min_bright: make the LED duty cycle about 0% when in very dim light (dark room, covered with hand) MEASURED VALUE: 256

Please put these values in the exercise04.json file and read them with your own version of exercise04.py.
This exercise04.json and exercise04.py should be in your own Git repo, and are the "answers" for Exercise 04.
