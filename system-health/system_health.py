import psutil

cpu_threshold = int(input("Enter CPU threshold: "))
ram_threshold = int(input("Enter RAM threshold: "))

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory()
total_gb = ram_usage.total / (1024 ** 3)
used_gb = ram_usage.used / (1024 ** 3)
available_gb = ram_usage.available / (1024 ** 3)

def check_cpu():
  if cpu_usage > cpu_threshold:
    print(f"Email Alert sent due to high CPU usage {cpu_usage}")
  else:
    print(f"CPU is in safe mode. Current CPU usage {cpu_usage}")
def check_ram():
  if used_gb > ram_threshold:
    print(f"Email Alert sent due to high RAM usage {used_gb}, available RAM {available_gb}")
  else:
    print(f"RAM is in safe mode. Current RAM usage {used_gb}, available RAM {available_gb}")

for i in range(3):
  check_cpu()
  check_ram()