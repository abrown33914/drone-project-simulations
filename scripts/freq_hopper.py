#!/usr/bin/env python3
import time
import random
import subprocess

frequencies = [5180, 5190, 5200, 5210, 5220, 5230]
hop_interval = 4  # seconds

# Define multiple jam attacks: (start_time, end_time, jammed_channel)
jam_schedule = [
    (5, 10, 5190),
    (12, 18, 5210),
    (25, 30, 5220)
]

start_time = time.time()
active_attack = None
attack_process = None

print("=== Frequency Hopping Simulation with Multiple Jam Windows ===")
for idx, (s, e, ch) in enumerate(jam_schedule):
    print(f"  Jam #{idx+1} → {ch} MHz from {s}s to {e}s")

print("--------------------------------------------------------------")

while True:
    now = int(time.time() - start_time)
    current_freq = random.choice(frequencies)

    # Check for any active jam matching the current time
    jam_match = None
    for window in jam_schedule:
        start, end, channel = window
        if start <= now <= end and current_freq == channel:
            jam_match = window
            break

    # Log status
    if jam_match:
        print(f"[{now:02}s] Channel: {current_freq} MHz | JAM DETECTED → Attempting attack...")
        if not active_attack:
            attack_process = subprocess.Popen(["bash", "jam_attack.sh"])
            active_attack = jam_match
    else:
        print(f"[{now:02}s] Channel: {current_freq} MHz | No attack triggered")

        # If we're hopping away from a previously jammed channel, cancel it
        if active_attack:
            if attack_process and attack_process.poll() is None:
                print(f"[{now:02}s] Hopped away. Canceling jam for {active_attack[2]} MHz.")
                attack_process.terminate()
            active_attack = None

    time.sleep(hop_interval)
