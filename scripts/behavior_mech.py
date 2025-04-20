#!/usr/bin/env python3
from pymavlink import mavutil
import time

# Connect to the drone via MAVLink
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
print("[CONNECT] Waiting for initial heartbeat...")
master.wait_heartbeat()
print(f"[STATUS] Connected to system {master.target_system}.")

last_heartbeat = time.time()
failsafe_triggered = False
heartbeat_timeout = 5  # seconds

print("[MONITOR] Watching for heartbeat loss...")

while True:
    now = time.time()

    # Try to receive heartbeat messages
    msg = master.recv_match(type='HEARTBEAT', blocking=False)
    if msg:
        last_heartbeat = now
        if failsafe_triggered:
            print("[RECOVERY] Heartbeat restored.")
        failsafe_triggered = False

    if not failsafe_triggered and now - last_heartbeat > heartbeat_timeout:
        print(f"[WARNING] No heartbeat for {heartbeat_timeout}s! Triggering LAND...")

        # Switch to LAND mode using MAV_CMD_DO_SET_MODE
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_MODE,
            0,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            9, 0, 0, 0, 0, 0  # LAND mode
        )

        failsafe_triggered = True


    time.sleep(0.5)
