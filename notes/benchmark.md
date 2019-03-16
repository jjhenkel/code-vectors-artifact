# Specification From Previous Work

## From API-San (raw table)

Although APISan lists quite a few bugs, each bug does not correspond to a separate specification. In fact, quite the opposite holds, most bugs are related to only a handful of specifications.

| Program | Module | API Misuse | Impact | Checker | Bugs | Confirmed |
| --- | --- | --- | --- | --- | --- | --- |
| Linux | cifs/cifs_dfs_ref.c | heap overflow | code execution | args | 1 | ✓ |
| Linux | xenbus/xenbus_dev_frontend.c | missing integer overflow check | code execution | intovfl | 1 | ✓ |
| Linux | ext4/resize.c | incorrect integer overflow check | code execution | intovfl | 1 | ✓ |
| Linux | tipc/link.c | missing tipc_bcast_unlock() | deadlock | cpair | 1 | ✓ |
| Linux | clk/clk.c | missing clk_prepare_unlock() | deadlock | cpair | 1 | ✓ |
| Linux | hotplug/acpiphp_glue.c | missing pci_unlock_rescan_remove() | deadlock | cpair | 1 | ✓ |
| Linux | usbvision/usbvision-video.c | missing mutex_unlock() | deadlock | cpair | 1 | ✓ |
| Linux | drm/drm_dp_mst_topology.c | missing drm_dp_put_port() | DoS | cpair | 1 | ✓ |
| Linux | affs/file.c | missing kunmap() | DoS | cpair | 1 | ✓ |
| Linux | acpi/sysfs.c | missing kobject_create_and_add() check | system crash | rvchk | 1 | ✓ |
| Linux | cx231xx/cx231xx-417.c | missing kmalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | qxl/qxl_kms.c | missing kmalloc() check | system crash | rvchk | 1 | P |
| Linux | chips/cfi_cmdset_0001.c | missing kmalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | ata/sata_sx4.c | missing kzalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | hsi/hsi.c | missing kzalloc() check | system crash | rvchk | 2 | ✓ |
| Linux | mwifiex/sdio.c | missing kzalloc() check | system crash | rvchk | 2 | ✓ |
| Linux | usbtv/usbtv-video.c | missing kzalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | cxgb4/clip_tbl.c | missing t4_alloc_mem() check | system crash | rvchk | 1 | ✓ |
| Linux | devfreq/devfreq.c | missing devm_kzalloc() check | system crash | rvchk | 2 | ✓ |
| Linux | i915/intel_dsi_panel_vbt.c | missing devm_kzalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | gpio/gpio-mcp23s08.c | missing devm_kzalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | drm/drm_crtc.c | missing drm_property_create_range() check | system crash | rvchk | 13 | ✓ |
| Linux | gma500/framebuffer.c | missing drm_property_create_range() check | system crash | rvchk | 1 | ✓ |
| Linux | emu10k1/emu10k1_main.c | missing kthread_create() check | system crash | rvchk | 1 | ✓ |
| Linux | m5602/m5602_s5k83a.c | missing kthread_create() check | system crash | rvchk | 1 | ✓ |
| Linux | hisax/isdnl2.c | missing skb_clone() check | system crash | rvchk | 1 | ✓ |
| Linux | qlcnic/qlcnic_ctx.c | missing qlcnic_alloc_mbx_args() check | system crash | rvchk | 1 | ✓ |
| Linux | xen-netback/xenbus.c | missing vzalloc() check | system crash | rvchk | 1 | ✓ |
| Linux | i2c/ch7006_drv.c | missing drm_property_create_range() check | system crash | rvchk | 1 | ✓ |
| Linux | fmc/fmc-fakedev.c | missing kmemdup() check | system crash | rvchk | 1 | P |
| Linux | rc/igorplugusb.c | missing rc_allocate_device() check | system crash | rvchk | 1 | ✓ |
| Linux | s5p-mfc/s5p_mfc.c | missing create_singlethread_workqueue() check | system crash | rvchk | 1 | P |
| Linux | fusion/mptbase.c | missing create_singlethread_workqueue() check | system crash | rvchk | 1 | P |
| Linux | nes/nes_cm.c | missing create_singlethread_workqueue() check | system crash | rvchk | 1 | ✓ |
| Linux | dvb-usb-v2/mxl111sf.c | missing mxl111sf_enable_usb_output() check | malfunction | rvchk | 2 | ✓ |
| Linux | misc/xen-kbdfront.c | missing xenbus_printf() check | malfunction | rvchk | 1 | ✓ |
| Linux | pvrusb2/pvrusb2-context.c | incorrect kthread_run() check | malfunction | rvchk | 1 | P |
| Linux | agere/et131x.c | incorrect drm_alloc_coherent() check | malfunction | rvchk | 1 | ✓ |
| Linux | drbd/drbd_receiver.c | incorrect crypto_alloc_hash() check | malfunction | rvchk | 1 | ✓ |
| Linux | mlx4/mr.c | incorrect mlx4_alloc_cmd_mailbox() check | maintanence | rvchk | 1 | ✓ |
| Linux | usnic/usnic_ib_qp_grp.c | incorrect kzalloc() check | maintanence | rvchk | 2 | ✓ |
| Linux | aoe/aoecmd.c | incorrect kthread_run() check | maintanence | rvchk | 1 | ✓ |
| Linux | ipv4/tcp.c | incorrect crypto_alloc_hash() check | maintanence | rvchk | 1 | ✓ |
| Linux | mfd/bcm590xx.c | incorrect i2c_new_dummy() check | maintanence | rvchk | 1 | P |
| Linux | usnic/usnic_ib_main.c | incorrect ib_alloc_device() check | maintanence | rvchk | 1 | ✓ |
| Linux | usnic/usnic_ib_qp_grp.c | incorrect usnic_fwd_dev_alloc() check | maintanence | rvchk | 1 | ✓ |
| OpenSSL | dsa/dsa_gen.c | missing BN_CTX_end() | DoS | cpair | 1 | ✓ |
| OpenSSL | apps/req.c | missing EVP_PKEY_CTX_free() | DoS | cpair | 1 | ✓ |
| OpenSSL | dh/dh_pmeth.c | missing OPENSSL_memdup() check | system crash | rvchk | 1 | ✓ |
| PHP | standard/string.c | missing integer overflow check | code execution | intovfl | 3 | ✓ |
| PHP | phpdbg/phpdbg_prompt.c | format string bug | code execution | args | 1 | ✓ |
| Python | Modules/zipimport.c | missing integer overflow check | code execution | intovfl | 1 | ✓ |
| rabbitmq | librabbitmq/amqp_openssl.c | incorrect SSL_get_verify_result() use | MITM | cond | 1 | ✓ |
| hexchat | common/server.c | incorrect SSL_get_verify_result() use | MITM | cond | 1 | ✓ |
| lprng | auth/ssl_auth.c | incorrect SSL_get_verify_result() use | MITM | cond | 1 | P |
| afflib | lib/aftest.cpp | missing BIO_new_file() check | system crash | rvchk | 1 | ✓ |
| afflib | tools/aff_bom.cpp | missing BIO_new_file() check | system crash | rvchk | 1 | ✓ |

## From JUXTA (raw table)

This tool was from the paper "Cross-checking Semantic Correctness: The Case of Finding File System Bugs".

| FS | Module | Operation | Error |Impact | #bugs | Y | S |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ADFS | dir_fplus.c | data read | [E] incorrect return value | application | 1 | >10y | ✓ |
| ADFS | super.c | super operation | [E] incorrect return value | application | 5 | >10y | ✓ |
| AFS | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 1 | 8y | P |
| AFFS | file.c | page I/O | [C] missing unlock()/page_cache_release() | deadlock | 2 | >10y | ✓ |
| AFFS | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 1 | 10y | ✓ |
| BFS | dir.c | data read | [E] incorrect return value | application | 2 | >10y | ✓ |
| btrfs | extent_io.c | fiemap_next_extent() | [E] incorrect error handling | application | 1 | 4y | ✓ |
| Ceph | addr.c | page I/O | [S] missing page_cache_release() | DoS | 1 | 5y | ✓ |
| Ceph | dir.c | readdir(), symlink() | [E] missing kstrdup() return check | system crash | 2 | 6y | ✓ |
| Ceph | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 2 | 6y | ✓ |
| Ceph | xattr.c | set_xattr(), remove_xattr() | [E] missing kstrdup() return check | system crash | 2 | 6y | ✓ |
| CIFS | connect.c | mount option parsing | [M] missing kfree() | DoS | 3 | 6y | ✓ |
| CIFS | file.c | waiting for posix lock file | [E] missing check | consistency | 2 | 3y | ✓ |
| ext4 | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 2 | 5y | ✓ |
| CFS2 | glock.c | debugfs file and dir creation | [E] incorrect error handling | system crash | 5 | 8y | ✓ |
| HFS | dir.c | file / dir creation | [E] incorrect return value | application | 2 | >10y | ✓ |
| HFSplus | dir.c | symlink and mknod creation | [E] incorrect return value | application | 2 | 5y | ✓ |
| HFSplus | inode.c | metadata inode sync | [E] missing error check | system crash | 2 | >10y | P |
| HPFS | namei.c | rename | [S] missing update of ctime and mtime | application | 4 | >10y | ✓ |
| HPFS | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 1 | 7y | ✓ |
| JBD2 | † transaction.c | journal transaction | [C] try to unlock an unheld spinlock | deadlock, consistency | 2 | 9y | ✓ |
| LogFS | segment.c | read_page_cache() | [E] incorrect error handling | system crash | 2 | 5y | P |
| LogFS | super.c | read_page_cache() | [E] incorrect error handling | system crash | 2 | 6y | P |
| NFS | nfs4client.c | update NFS server | [E] missing kstrdup() return check | system crash | 1 | 2y | ✓ |
| NFS | nfs4proc.c | client ID hanlding | [E] missing kstrdup() return check | system crash | 5 | 1y | ✓ |
| NFSD | fault_inject.c | debugfs file and dir creation | [E] incorrect error handling | system crash | 2 | 4y | ✓ |
| OCFS2 | xattr.c | get xattr list in trusted domain | [S] missing CAP_SYS_ADMIN check | security | 1 | 6y | ✓ |
| ResierFS | super.c | mount option parsing | [E] missing kstrdup() return check | system crash | 1 | 7y | P |
| SquashFS | symlink.c | reading symlink information | [E] incorrect return value | application | 2 | 6y | P |
| UBIFS | dir.c | create/mkdir/mknod/symlink() | [C] incorrect mutex_unlock() and i_size update | deadlock, application | 4 | <1y | ✓ |
| UBIFS | file.c | page I/O | [E] missing kmalloc() return check | system crash | 1 | 7y | P |
| UDF | file.c | page I/O | [S] missing mark_inode_dirty() | consistency | 1 | 1y | P |
| UDF | inode.c | page I/O | [E] incorrect return value | application | 1 | 8y | ✓ |
| UDF | namei.c | symlink() operation | [E] missing return value | system crash | 1 | 8y | ✓ |
| UDF | namei.c | rename | [S] missing update of ctime and mtime | application | 2 | >10 y | ✓ |
| UFS | inode.c | update inode | [E] incorrect return value | application | 2 | 8y | P |
| XFS | xfs_acl.c | ACL handling | [C] incorrect kmalloc() flag in I/O context | deadlock | 3 | 7y | ✓ |
| XFS | xfs_mru_cache.c | disk block allocation | [C] incorrect kmalloc() flag in I/O context | deadlock | 1 | 8y | ✓ |

---

## Extracted (cleaned) specifications

These are ground-truth specifications extracted from the raw tables above. I've referenced the current kernel code (commit: `12ad143e1b803e541e48b8ba40f550250259ecdd`) to try and ensure these specifications
still hold. In some cases things may have been renamed/removed and in those cases I was not able to generate a specification.

```
tipc_bcast_lock tipc_bcast_unlock
clk_prepare_lock clk_prepare_unlock
pci_lock_rescan_remove pci_unlock_rescan_remove
mutex_lock_nested mutex_unlock
kmap kunmap
kobject_create_and_add kobject_create_and_add_$EQ_0|kobject_create_and_add_$NEQ_0
kmalloc kmalloc_$EQ_0|kmalloc_$NEQ_0
kzalloc kzalloc_$EQ_0|kzalloc_$NEQ_0
drm_property_create_range drm_property_create_range_$EQ_0|drm_property_create_range_$NEQ_0
kthread_create_on_node kthread_create_on_node_$EQ_0|kthread_create_on_node_$NEQ_0
skb_clone skb_clone_$EQ_0|skb_clone_$NEQ_0
qlcnic_alloc_mbx_args qlcnic_alloc_mbx_args_$EQ_0|qlcnic_alloc_mbx_args_$NEQ_0
vzalloc vzalloc_$EQ_0|vzalloc_$NEQ_0
kmemdup kmemdup_$EQ_0|kmemdup_$NEQ_0
rc_allocate_device rc_allocate_device_$EQ_0|rc_allocate_device_$NEQ_0
create_singlethread_workqueue create_singlethread_workqueue_$EQ_0|create_singlethread_workqueue_$NEQ_0
mxl111sf_enable_usb_output mxl111sf_enable_usb_output_$EQ_0|mxl111sf_enable_usb_output_$NEQ_0
xenbus_printf xenbus_printf_$EQ_0|xenbus_printf_$NEQ_0
crypto_alloc_ahash IS_ERR IS_ERR_$EQ_0|IS_ERR_$NEQ_0
mlx4_alloc_cmd_mailbox IS_ERR IS_ERR_$EQ_0|IS_ERR_$NEQ_0
i2c_new_dummy i2c_new_dummy_$EQ_0|i2c_new_dummy_$NEQ_0
ib_alloc_device ib_alloc_device_$EQ_0|ib_alloc_device_$NEQ_0
usnic_fwd_dev_alloc usnic_fwd_dev_alloc_$EQ_0|usnic_fwd_dev_alloc_$NEQ_0
kmalloc_$p1_$LT_4294967295 kmalloc
```

NOTES:
drm_dp_put_port (renamed and can't figure out if property still holds)
t4_alloc_mem (no references in current commit)
kthread_create macro for call to kthread_create_on_node
not sure about kthread_run check? Expands internally to kthread_create -> kthread_create_on_node
drm_alloc_coherent (no reference in current commit)

### From JUXTA:

An issue here: do these hold outside of the limited scope of different
filesystem implementations? 

```
kcalloc_$EQ_0 $RET_ENOMEM
kmalloc_$EQ_0 $RET_ENOMEM
sb_bread_$EQ_0 $RET_ERR_PTR(-EIO)|$RET_EIO
kstrdup kstrdup_$EQ_0|kstrdup_$NEQ_0
kstrdup_$EQ_0 $RET_ENOMEM

```