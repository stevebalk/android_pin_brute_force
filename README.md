<h1>android_pin_brutforce</h1>
<br>
Python3 program that creates a duckyscript payload to brutforce a 4-digit pin on android. It uses an improved pin list to use most used pins first.<br>
<br>
I tested the script with my Flipper Zero on a Xiaomi Redmi Note 10 Pro and a Samsung Samsung Galaxy Tab A T580 (2016).<br>
The Redmi Note 10 used Android 11 and the Galaxy Tab Android 7.0<br>
<br>
Because of the security rules it is really time demanding and kind of impossible to get the pin with this approach if it’s not in the range of x (time you could afford<br>
The pin security rules on this devices work like this:<br>
<br>
Try | Waittime (locked) in seconds<br>
1-5 (5 trys)  | 30<br>
6-10 (5 trys) | 30<br>
11-20 (1 try) | 30<br>
21-30 (1 try) | 60<br>
31-40 (1 try) | 120<br>
41-50 (1 try) | 240<br>
51-60 (1 try) | 480<br>
<br>
I just tested it until i hit 480 (8 minutes).<br>
It seems like it is increasing by the factor of 2 every 10 tries. So it is absolutly not worth after x tries to move on.<br>
Sadly i don’t have an older device with a lower Android version or from another brand to test with.<br>
If it would just stay within 30 seconds lock time, it would only take 16.6 hours to brutforce a 4 digit pin in the worst case scenario.<br>
