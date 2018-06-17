#!/bin/bash

echo "[reproduce-rq2] Reproducing ablation study..."
echo "[reproduce-rq2] Running (1)..."
tar -xf /vectors/AB1_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB1_d-300-i-1000-w-50-vm-0.txt
rm -f AB1_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (2)..."
tar -xf /vectors/AB2_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB2_d-300-i-1000-w-50-vm-0.txt
rm -f AB2_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (3)..."
tar -xf /vectors/AB3_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB3_d-300-i-1000-w-50-vm-0.txt
rm -f AB3_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (4)..."
tar -xf /vectors/AB4_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB4_d-300-i-1000-w-50-vm-0.txt
rm -f AB4_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (5)..."
tar -xf /vectors/AB5_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB5_d-300-i-1000-w-50-vm-0.txt
rm -f AB5_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (6)..."
tar -xf /vectors/AB6_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB6_d-300-i-1000-w-50-vm-0.txt
rm -f AB6_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (7)..."
tar -xf /vectors/AB7_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB7_d-300-i-1000-w-50-vm-0.txt
rm -f AB7_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Running (8)..."
tar -xf /vectors/AB8_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/ablation.py AB8_d-300-i-1000-w-50-vm-0.txt
rm -f AB8_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq2] Complete!"
