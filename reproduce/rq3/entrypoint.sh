#!/bin/bash

echo "[reproduce-rq3] Reproducing syntactic VS semantic experiment..."
echo "[reproduce-rq3] Running (SEMANTIC)..."
tar -xf /vectors/SEMANTIC_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/syntactic-vs-semantic.py SEMANTIC_d-300-i-1000-w-50-vm-0.txt
rm -f SEMANTIC_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq3] Running (SYNTACTIC)..."
tar -xf /vectors/SYNTACTIC_d-300-i-1000-w-50-vm-0.txt.tar.lz
time python /app/syntactic-vs-semantic.py SYNTACTIC_d-300-i-1000-w-50-vm-0.txt
rm -f SYNTACTIC_d-300-i-1000-w-50-vm-0.txt
echo "[reproduce-rq3] Complete!"
