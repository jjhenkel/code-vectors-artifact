# Output from test run 

Generated using an 8-core Debian 9 desktop with 10GB of RAM.

### Command

`jjhenkel@twiltie:~/workspace/code-vectors-artifact$ docker run -it --rm jjhenkel/code-vectors-artifact:rq1`

### Results

```
Loading model from: /vectors/vectors-gensim.txt
K is set to: 1
# RQ1 - Experiments

## 5.1 - Code Analogies
Running 20 tests:
  Running 16 / 32 (18):
    Passed 246/306 (80.39%)
  Running Add / Remove (9):
    Passed 72/72 (100.00%)
  Running Create / Destroy (19):
    Passed 302/342 (88.30%)
  Running Enable / Disable (62):
    Passed 3577/3782 (94.58%)
  Running Enter / Exit (12):
    Passed 122/132 (92.42%)
  Running In / Out (5):
    Passed 20/20 (100.00%)
  Running Inc / Dec (10):
    Passed 88/90 (97.78%)
  Running Input / Output (5):
    Passed 20/20 (100.00%)
  Running Join / Leave (4):
    Passed 8/12 (66.67%)
  Running Lock / Unlock (53):
    Passed 2504/2756 (90.86%)
  Running On / Off (19):
    Passed 303/342 (88.60%)
  Running Read / Write (64):
    Passed 3950/4032 (97.97%)
  Running Set / Get (22):
    Passed 404/462 (87.45%)
  Running Start / Stop (31):
    Passed 838/930 (90.11%)
  Running Up / Down (24):
    Passed 495/552 (89.67%)
  Running Ret Check / Call (21):
    Passed 252/420 (60.00%)
  Running Ret Error / Prop (25):
    Passed 600/600 (100.00%)
  Running Check / Check (50):
    Passed 2424/2450 (98.94%)
  Running Next / Prev (16):
    Passed 240/240 (100.00%)
  Running Test / Set (39):
    Passed 1425/1482 (96.15%)
SUMMARY:
  Passed 17890/19042 (93.95%)
  0/19042 out of vocabulary

## 5.2 - Simple Similarity
sin_mul and cos_mul
dec_stream_header and dec_stream_footer
rx_b_frame and tx_b_frame
nouveau_bo_new_$EQ_0 and nouveau_bo_map
5 closest words to affs_bread:
  #1 - affs_bread_$NEQ_0
  #2 - affs_checksum_block
  #3 - AFFS_SB
  #4 - affs_free_block
  #5 - affs_brelse
5 closest words to kzalloc:
  #1 - kzalloc_$NEQ_0
  #2 - kfree
  #3 - _volume
  #4 - snd_emu10k1_audigy_write_op
  #5 - ?->output_amp

## 5.3 - Queries via Word-Vector Averaging
              w :   2/20  passed (10.00%)
       w + $ERR :  14/20  passed (70.00%)
       w + $END :  16/20  passed (80.00%)
w + $ERR + $END :  18/20  passed (90.00%)
```

---

Generated using an 64-core CentOS 7 workstation with 256GB of RAM.

### Command

`[jjhenkel@velveeta] (63)$ docker run -it --rm jjhenkel/code-vectors-artifact:rq2`

### Results

```
Loading model from: /vectors/vectors-gensim.txt
K is set to: 1
# RQ1 - Experiments

## 5.1 - Code Analogies
Running 20 tests:
  Running 16 / 32 (18):
    Passed 246/306 (80.39%)
  Running Add / Remove (9):
    Passed 72/72 (100.00%)
  Running Create / Destroy (19):
    Passed 302/342 (88.30%)
  Running Enable / Disable (62):
    Passed 3577/3782 (94.58%)
  Running Enter / Exit (12):
    Passed 122/132 (92.42%)
  Running In / Out (5):
    Passed 20/20 (100.00%)
  Running Inc / Dec (10):
    Passed 88/90 (97.78%)
  Running Input / Output (5):
    Passed 20/20 (100.00%)
  Running Join / Leave (4):
    Passed 8/12 (66.67%)
  Running Lock / Unlock (53):
    Passed 2504/2756 (90.86%)
  Running On / Off (19):
    Passed 303/342 (88.60%)
  Running Read / Write (64):
    Passed 3950/4032 (97.97%)
  Running Set / Get (22):
    Passed 404/462 (87.45%)
  Running Start / Stop (31):
    Passed 838/930 (90.11%)
  Running Up / Down (24):
    Passed 495/552 (89.67%)
  Running Ret Check / Call (21):
    Passed 252/420 (60.00%)
  Running Ret Error / Prop (25):
    Passed 600/600 (100.00%)
  Running Check / Check (50):
    Passed 2424/2450 (98.94%)
  Running Next / Prev (16):
    Passed 240/240 (100.00%)
  Running Test / Set (39):
    Passed 1425/1482 (96.15%)
SUMMARY:
  Passed 17890/19042 (93.95%)
  0/19042 out of vocabulary

## 5.2 - Simple Similarity
sin_mul and cos_mul
dec_stream_header and dec_stream_footer
rx_b_frame and tx_b_frame
nouveau_bo_new_$EQ_0 and nouveau_bo_map
5 closest words to affs_bread:
  #1 - affs_bread_$NEQ_0
  #2 - affs_checksum_block
  #3 - AFFS_SB
  #4 - affs_free_block
  #5 - affs_brelse
5 closest words to kzalloc:
  #1 - kzalloc_$NEQ_0
  #2 - kfree
  #3 - _volume
  #4 - snd_emu10k1_audigy_write_op
  #5 - ?->output_amp

## 5.3 - Queries via Word-Vector Averaging
              w :   2/20  passed (10.00%)
       w + $ERR :  14/20  passed (70.00%)
       w + $END :  16/20  passed (80.00%)
w + $ERR + $END :  18/20  passed (90.00%)
```
