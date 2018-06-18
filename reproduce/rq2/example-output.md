# Output from test run 

Generated using an 8-core Debian 9 desktop with 10GB of RAM.

### Command

`jjhenkel@twiltie:~/workspace/code-vectors-artifact$ docker run -it --rm jjhenkel/code-vectors-artifact:rq2`

### Results

```
[reproduce-rq2] Reproducing ablation study...
[reproduce-rq2] Running (1)...
[reproduce-rq2] Loading model from: AB1_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/16344/19042 (85.83%)


real	22m19.437s
user	137m42.732s
sys	20m4.792s
[reproduce-rq2] Running (2)...
[reproduce-rq2] Loading model from: AB2_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/9847/19042 (51.71%)


real	25m29.695s
user	167m31.440s
sys	19m13.636s
[reproduce-rq2] Running (3)...
[reproduce-rq2] Loading model from: AB3_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 1020/15887/18022 (83.43%)


real	13m34.521s
user	85m31.480s
sys	12m7.540s
[reproduce-rq2] Running (4)...
[reproduce-rq2] Loading model from: AB4_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 4172/11749/14870 (61.70%)


real	8m19.943s
user	50m35.472s
sys	7m37.108s
[reproduce-rq2] Running (5)...
[reproduce-rq2] Loading model from: AB5_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 600/15812/18442 (83.04%)


real	23m36.998s
user	152m20.520s
sys	18m58.100s
[reproduce-rq2] Running (6)...
[reproduce-rq2] Loading model from: AB6_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/16278/19042 (85.48%)


real	26m48.911s
user	169m10.432s
sys	23m30.832s
[reproduce-rq2] Running (7)...
[reproduce-rq2] Loading model from: AB7_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/15954/19042 (83.78%)


real	27m26.004s
user	166m15.816s
sys	25m9.160s
[reproduce-rq2] Running (8)...
[reproduce-rq2] Loading model from: AB8_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/15698/19042 (82.44%)


real	26m56.576s
user	167m42.204s
sys	22m29.952s
[reproduce-rq2] Complete!
```

---

Generated using an 64-core CentOS 7 workstation with 256GB of RAM.

### Command

`[jjhenkel@velveeta] (63)$ docker run -it --rm jjhenkel/code-vectors-artifact:rq2`

### Results

```
[reproduce-rq2] Reproducing ablation study...
[reproduce-rq2] Running (1)...
[reproduce-rq2] Loading model from: AB1_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/16344/19042 (85.83%)


real	11m5.528s
user	186m23.418s
sys	242m20.295s
[reproduce-rq2] Running (2)...
[reproduce-rq2] Loading model from: AB2_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/9847/19042 (51.71%)


real	11m25.588s
user	189m59.392s
sys	255m56.710s
[reproduce-rq2] Running (3)...
[reproduce-rq2] Loading model from: AB3_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 1020/15887/18022 (83.43%)


real	8m49.833s
user	136m49.155s
sys	178m37.074s
[reproduce-rq2] Running (4)...
[reproduce-rq2] Loading model from: AB4_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 4172/11749/14870 (61.70%)


real	6m8.588s
user	90m40.701s
sys	116m17.038s
[reproduce-rq2] Running (5)...
[reproduce-rq2] Loading model from: AB5_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 600/15812/18442 (83.04%)


real	14m15.981s
user	250m49.488s
sys	382m0.752s
[reproduce-rq2] Running (6)...
[reproduce-rq2] Loading model from: AB6_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/16278/19042 (85.48%)


real	11m35.302s
user	190m47.615s
sys	265m58.833s
[reproduce-rq2] Running (7)...
[reproduce-rq2] Loading model from: AB7_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/15954/19042 (83.78%)


real	11m34.145s
user	191m19.814s
sys	260m19.028s
[reproduce-rq2] Running (8)...
[reproduce-rq2] Loading model from: AB8_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq2] K is set to: 1
[reproduce-rq2] Results 0/15698/19042 (82.44%)


real	11m30.228s
user	193m29.547s
sys	254m56.523s
[reproduce-rq2] Complete!
```