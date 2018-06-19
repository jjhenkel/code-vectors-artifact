#!/bin/bash

echo "[code-vectors-dataset] Extacting artifacts..."
echo "[code-vectors-dataset] Extracting traces..."
tar -xf /dataset/kernel-traces.tar.gz -C /output
mv /output/traces/ablation-0/*.traces.gz /output/traces
rm -rf /output/traces/ablation-0
echo "[code-vectors-dataset] Extracting vectors (vmin: 0)..."
tar -xf /dataset/best-vectors-vmin-0.txt.tar.lz -C /output
mv /output/best-vectors-vmin-0.txt /output/vectors-vmin-0.txt
echo "[code-vectors-dataset] Extracting vectors (vmin: 1000)..."
tar -xf /dataset/best-vectors-vmin-1000.txt.tar.lz -C /output
mv /output/best-vectors-vmin-1000.txt /output/vectors-vmin-1000.txt
echo "[code-vectors-dataset] Copying misc files..."
cp /dataset/README.md /output/README.md
cp /dataset/peek-traces.sh /output/peek-traces.sh
chmod +x /output/peek-traces.sh
cp /dataset/analogies.py /output/analogies.py
echo "[code-vectors-dataset] Complete!"
