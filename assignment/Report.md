# Exercise 1
## Question 01
Before running the exercise01.py program, about how long do you think the program above will take to run? Did you have the right answer -- what does the program print out?
## Answer: 
I predicted that the program would take 3.0 seconds to run considering that I chose to run the loop 3 times with a 1-second sleep interval for each loop iteration. My answer was close but not correct. My measured time was 3.016 seconds.
## Question 02
What do the "int" and "float" notation mean?
Will the program run if these notations are removed or incorrect?
##  Answer: 
The "int" and "float" notation declares the variable of either type "int" or "float". Depending on where this notation is used, it can be used to cast one variable into a different type as well as make the output of the function of that type. Ex: def total_time(N: int, sleep_time: float) -> float We expect to return a float at the end of the function. The program will not run if the type is not correct.
## Question 03
Why is "time.ticks_diff(toc, tic)" used to determine elapsed time instead of "toc - tic"?
## Answer: 
"time.ticks_diff(toc, tic)" is used to determine elapsed time instead of "toc - tic" because this is a built-in function and already performs the "toc - tic" operation inside it.

# Exercise 2
## Question 01
Why do you think we would use a file (e.g. JSON file) for parameter storage instead of accepting the parameters as user input(), especially on an embedded system?
## Answer: 
We use a file for parameter storage instead of accepting the parameters as user 'input(); especially in embedded systems because files allow for consistency and reusability, security such as storing API keys, flexibility, ease of maintenance if certain parameters need to be updated, performance since embedded systems often have startup configurations that are read from a file during boot time, testing, and user experience.
## Question 02
Why might we prefer to use a JSON file to store parameters instead of hard-coding values in the Python script?
## Answer: 
We prefer to use a JSON file to store parameters instead of hard-coding values in the Python script for code organization, cleaner code, and security issues when dealing with sensitive data.
## Question 03
Why didn't the exercise02.py code use os.path.isfile, that is, why did I write the "is_regular_file()" function?
## Answer:
The is_regular_file() function was created to provide a way to check if a file is a regular file that works in both MicroPython and standard Python environments, allowing for code that is portable between these two environments since the "os.path.isfile()" method does not exist in the MicroPython environment. This function leverages the available functionalities in each environment to perform the file check, ensuring the script can run correctly regardless of the Python environment it is executed in.

# Exercise 3
## Question 1
Suppose I want to add additional code that requires me to increase sample time, to allow more time for the additional code to execute. What is the tradeoff when I increase sample time relative to the "dot_dash_threshold" value? Try this by increasing "sample_ms" in exercise3.json on the Pico. The effect should be quite noticeable.
## Answer: 
Increasing the time between samples simply means there are fewer samples taken. If increased too high, this means that gaps between presses, or even entire dots, can slip through completely undetected. If the dot/dash threshold remains fixed, it also means that fewer samples are required to register a dash. Fewer samples mean dots can be mistaken for dashes and vice versa, as there is simply less data to interpolate. Thus, increasing the sample time without increasing the threshold results in more errors.

# Exercise 4
## Questions
Let's calibrate the light sensor to be meaningful. If you don't want to put a light calibration app on your phone that's fine. Instead we could experiment to find the max_bright and min_bright values that:
max_bright: make the LED duty cycle about 100% when in bright light (sunlight, room light) 
min_bright: make the LED duty cycle about 0% when in very dim light (dark room, covered with hand) 

## Answer:
Measured Value (Max): 45195

Measured Value (Min): 256

These values are stored in the exercise04.json file.
