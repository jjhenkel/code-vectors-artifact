# Output from test run 

Generated using an 8-core Debian 9 desktop with 10GB of RAM.

### Command

`jjhenkel@twiltie:~/workspace/code-vectors-artifact$ docker run -it --rm jjhenkel/code-vectors-artifact:rq3`

### Results

```
[reproduce-rq3] Reproducing syntactic VS semantic experiment...
[reproduce-rq3] Running (SEMANTIC)...
[reproduce-rq3] Loading model from: SEMANTIC_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq3] K is set to: 1
[reproduce-rq3] Results 0/16344/19042 (85.83%)


real	23m47.331s
user	97m41.288s
sys	34m45.492s
[reproduce-rq3] Running (SYNTACTIC)...
[reproduce-rq3] Loading model from: SYNTACTIC_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq3] K is set to: 1
[reproduce-rq3] Results 5502/5970/13540 (31.35%)


real	9m22.498s
user	45m30.836s
sys	11m57.288s
[reproduce-rq3] Complete!
```

---

Generated using an 64-core CentOS 7 workstation with 256GB of RAM.

### Command

`jjhenkel@twiltie:~/workspace/code-vectors-artifact$ docker run -it --rm jjhenkel/code-vectors-artifact:rq3`

### Results

```
[reproduce-rq3] Reproducing syntactic VS semantic experiment...
[reproduce-rq3] Running (SEMANTIC)...
[reproduce-rq3] Loading model from: SEMANTIC_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq3] K is set to: 1
[reproduce-rq3] Results 0/16344/19042 (85.83%)


real	14m20.438s
user	259m34.113s
sys	368m57.174s
[reproduce-rq3] Running (SYNTACTIC)...
[reproduce-rq3] Loading model from: SYNTACTIC_d-300-i-1000-w-50-vm-0.txt
[reproduce-rq3] K is set to: 1
[reproduce-rq3] Results 5502/5970/13540 (31.35%)


real	4m59.003s
user	72m30.655s
sys	95m8.942s
[reproduce-rq3] Complete!
```
