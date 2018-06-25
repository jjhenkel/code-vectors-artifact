



### Get function AFTER CHANGE from linux
```bash
git show 937c397eb633b804d9a806d08c395ecfc42b1fec:drivers/net/wireless/iwlwifi/iwl3945-base.c | ./extract.sh iwl3945_dump_nic_event_log &> /nobackup/jjhenkel/workspace/code-vectors-artifact/reproduce/rq4/3-bad.c
```

### Get function BEFORE CHANGE from linux
```bash
git show 937c397eb633b804d9a806d08c395ecfc42b1fec^1:drivers/net/wireless/iwlwifi/iwl3945-base.c | ./extract.sh iwl3945_dump_nic_event_log &> /nobackup/jjhenkel/workspace/code-vectors-artifact/reproduce/rq4/3-bad.c
```

### Extract Function Script
```bash
#!/bin/sh
# $1 = function name
less <&0 | indent -st -orig | awk '
BEGIN { state = 0; last = ""; }
$0 ~ /^'$1'\(/ { print last; state = 1; }
        { if (state == 1) print; }
$0 ~ /^}/ { if (state) state = 2; }
        { last = $0; }
'
```