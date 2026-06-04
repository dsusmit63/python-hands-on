import psutil 

cpu_threshold = int(input("Enter CPU threshold(%): "))
ram_threshold = int(input("Enter RAM threshold(%): "))
disk_threshold = int(input("Enter Disk threshold(%): "))

def validate_user_input():
  if cpu_threshold > 100 or cpu_threshold < 0 or ram_threshold > 100 or ram_threshold < 0 or disk_threshold > 100 or disk_threshold < 0:
    print("Threshold value should between 0-100")
    return False
  else:
    return True
def check_cpu(cpu_threshold,cpu_usage):
  if cpu_usage > cpu_threshold:
    print(f"Email Alert sent due to high CPU usage {cpu_usage}%")
  else:
    print(f"CPU is in safe mode. Current CPU usage {cpu_usage}%")
def check_ram(ram_threshold, ram_usage):
  if ram_usage > ram_threshold:
    print(f"Email Alert sent due to high RAM usage {ram_usage}%")
  else:
    print(f"RAM is in safe mode. Current RAM usage {ram_usage}%")
def check_disk(disk_threshold,disk_usage):
  if disk_usage >disk_threshold:
    print(f"Email Alert sent due to high Disk usage {disk_usage}%")
  else:
    print(f"Disk is in safe mode. Current Disk usage {disk_usage}%")
def check_system_resources():
  cpu_usage = psutil.cpu_percent(interval=1)
  ram_usage = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage('/').percent
  check_cpu(cpu_threshold,cpu_usage)
  check_ram(ram_threshold,ram_usage)
  check_disk(disk_threshold,disk_usage)

validation_result = validate_user_input()

if validation_result:
  check_system_resources()
 