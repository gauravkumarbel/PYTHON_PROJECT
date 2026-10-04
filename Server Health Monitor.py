import psutil

print("===== SERVER HEALTH =====")

print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

memory = psutil.virtual_memory()
print(f"RAM Usage: {memory.percent}%")
print(f"RAM Available: {memory.available / (1024**3):.2f} GB")

disk = psutil.disk_usage("/")
print(f"Disk Usage: {disk.percent}%")
print(f"Disk Free: {disk.free / (1024**3):.2f} GB")

uptime = psutil.boot_time()
print(f"Boot Time: {uptime}")

battery = psutil.sensors_battery()

if battery:
    print("Battery:", battery.percent, "%")
    print("Charging:", battery.power_plugged)
else:
    print("pleas check pc logs")


network = psutil.net_io_counters()

print("Data Sent:", network.bytes_sent / (1024**2), "MB")
print("Data Received:", network.bytes_recv / (1024**2), "MB")

print("YOUR PC IS OK")

