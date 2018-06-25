# Output from test run

Generated using an 64-core CentOS 7 workstation with 256GB of RAM.

### Command

`[jjhenkel@velveeta] (29)$ docker run -it --rm jjhenkel/code-vectors-artifact:rq4`

### Results

```
Using TensorFlow backend.
Found 22076 unique tokens.
Shape of data tensor: (120, 100)
Shape of label tensor: (120, 121)
Found 136085 word vectors.
2018-06-25 21:25:45.434470: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX FMA
Accuracy @1: 62.50%
Accuracy @3: 85.83%
Accuracy @5: 90.83%
```
