#!/bin/bash
echo "[JAMMING] Attempting to jam drone..."
pkill -STOP -f arducopter
sleep 5
pkill -CONT -f arducopter
echo "[JAMMING] Attack finished"

