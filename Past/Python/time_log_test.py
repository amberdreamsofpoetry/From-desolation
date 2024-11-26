import time
from datetime import datetime

file_name = "time_log_test.txt"

try:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, 'a') as file:
            file.write(current_time + '\n')
            file.close()

        time.sleep(1)

except KeyboardInterrupt:
    print("\nDone.")
