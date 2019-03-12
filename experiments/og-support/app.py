import sys
import json

RULES = [
  ('tipc_bcast_lock', ['tipc_bcast_unlock']),
  ('clk_prepare_lock', ['clk_prepare_unlock']),
  ('pci_lock_rescan_remove', ['pci_unlock_rescan_remove']),
  ('mutex_lock_nested', ['mutex_unlock']),
  ('kmap', ['kunmap']),
  ('kobject_create_and_add', ['kobject_create_and_add_$EQ_0', 'kobject_create_and_add_$NEQ_0']),
  ('kmalloc', ['kmalloc_$EQ_0', 'kmalloc_$NEQ_0']),
  ('kzalloc', ['kzalloc_$EQ_0', 'kzalloc_$NEQ_0']),
  ('drm_property_create_range', ['drm_property_create_range_$EQ_0', 'drm_property_create_range_$NEQ_0']),
  ('kthread_create_on_node', ['kthread_create_on_node_$EQ_0', 'kthread_create_on_node_$NEQ_0']),
  ('skb_clone', ['skb_clone_$EQ_0', 'skb_clone_$NEQ_0']),
  ('qlcnic_alloc_mbx_args', ['qlcnic_alloc_mbx_args_$EQ_0', 'qlcnic_alloc_mbx_args_$NEQ_0']),
  ('vzalloc', ['vzalloc_$EQ_0', 'vzalloc_$NEQ_0']),
  ('kmemdup', ['kmemdup_$EQ_0', 'kmemdup_$NEQ_0']),
  ('rc_allocate_device', ['rc_allocate_device_$EQ_0', 'rc_allocate_device_$NEQ_0']),
  ('create_singlethread_workqueue', ['create_singlethread_workqueue_$EQ_0', 'create_singlethread_workqueue_$NEQ_0']),
  ('mxl111sf_enable_usb_output', ['mxl111sf_enable_usb_output_$EQ_0', 'mxl111sf_enable_usb_output_$NEQ_0']),
  ('xenbus_printf', ['xenbus_printf_$EQ_0', 'xenbus_printf_$EQ_0']),
  ('crypto_alloc_ahash', ['IS_ERR IS_ERR_$EQ_0', 'IS_ERR IS_ERR_$NEQ_0']),
  ('mlx4_alloc_cmd_mailbox', ['IS_ERR IS_ERR_$EQ_0', 'IS_ERR IS_ERR_$NEQ_0']),
  ('i2c_new_dummy', ['i2c_new_dummy_$EQ_0', 'i2c_new_dummy_$NEQ_0']),
  ('ib_alloc_device', ['ib_alloc_device_$EQ_0', 'ib_alloc_device_$NEQ_0']),
  ('usnic_fwd_dev_alloc', ['usnic_fwd_dev_alloc_$EQ_0', 'usnic_fwd_dev_alloc_$NEQ_0']),
]

counts = {}
asamap = {}
revmap = {}
for this,thats in RULES:
  asamap[this] = thats
  counts[this] = { 'pass': 0, 'fail': 0 }

  for that in thats:
    revmap[that] = this

for line in sys.stdin:
  # Quickly skip lines with none of the
  # qualifying words
  anymatch = False
  for this,_ in RULES:
    if this in line:
      anymatch = True
      break
  if not anymatch:
    continue
  
  # Set up stacks
  rule_stacks = {}
  for this,_ in RULES:
    rule_stacks[this] = []
  
  # Parse line
  parts = [ x.strip() for x in line.split(' ') ]
  function_name = parts[0]
  trace = parts[1:]  

  # Go through and check rules
  popmap = {}
  addtonext = None
  for temp in trace:
    # Patch work to combine things like 'IS_ERR IS_ERR_$EQ_0' 
    # into a single 'word' for the purpose of checking
    if temp == 'IS_ERR':
      addtonext = temp
      continue
    word = temp
    if addtonext is not None:
      word = addtonext + ' ' + word
      addtonext = None
    
    if word in rule_stacks:
      rule_stacks[word].append(True)
      for that in asamap[word]:
        popmap[that] = word
    elif word in popmap:
      key = popmap[word]

      # See if we can pop---if we can 
      # that was a successful rule usage
      if len(rule_stacks[key]) <= 0:
        print('Failed on {}: {}'.format(key, ' '.join(trace)))
        counts[key]['fail'] += 1
      else:
        counts[key]['pass'] += 1
        rule_stacks[key].pop()
      
      # If we don't have any waiting to be
      # popped remove this
      if len(rule_stacks[key]) <= 0:
        for that in asamap[revmap[word]]:
          del popmap[that]
  
  # Anything left is a result of a rule being failed
  anyfails = None
  for this,_ in RULES:
    if len(rule_stacks[this]) > 0:
      anyfails = this
    counts[this]['fail'] += len(rule_stacks[this])

  if anyfails is not None:
    print('Failed on {}: {}'.format(anyfails, ' '.join(trace)))

print(json.dumps(counts, indent=2, sort_keys=True))
