import time

SLEEP = 2
print("Hello, This is a python script for docker project")
print(f"Going to sleep for {SLEEP} seconds..if you want to kill the container , set SLEEP variable to 20")
print("Waiting...")
time.sleep(SLEEP)
print("Script done successfully!")
exit()
