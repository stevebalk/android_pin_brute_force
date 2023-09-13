<h1>Android pin brutforce</h1>

Python3 program that creates a duckyscript payload to brutforce a 4-digit pin on android. It uses an improved pin list to use most used pins first.  
  
I tested the script with my Flipper Zero on a Xiaomi Redmi Note 10 Pro and a Samsung Samsung Galaxy Tab A T580 (2016).  
The Redmi Note 10 used Android 11 and the Galaxy Tab Android 7.0  
  
Because of the security rules it is really time demanding and kind of impossible to get the pin with this approach if it’s not in the range of x (time you could afford).  
The pin security rules on those devices work like this:  
  
| Try  | tries without lock | Waittime (locked) in seconds |
| :--- | :---: | :--- |
| 1-5 | 5 | 30 |
| 6-10 | 5 | 30 |
| 11-20 | 1 | 30 |
| 21-30 | 1 | 60 |
| 31-40 | 1 | 120 |
| 41-50 | 1 | 240 |
| 51-60 | 1 | 480 |

I just tested it until i hit 480 (8 minutes).
It seems like it is increasing by the factor of 2 every 10 tries. So it is absolutly not worth after x tries to move on.
Sadly i don’t have an older device with a lower Android version or from another brand to test with.
If it would just stay within 30 seconds lock time, it would only take 16.6 hours to brutforce a 4 digit pin in the worst case scenario.
