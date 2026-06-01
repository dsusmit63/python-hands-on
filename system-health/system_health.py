import psutil
cpu_threshold = int(input("Enter CPU threshold: "))
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > cpu_threshold:
  print(f"Email Alert sent due to high cpu usage {cpu_usage}")
else:
  print(f"CPU is in safe mode. Current cpu usage {cpu_usage}")