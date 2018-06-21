#!/usr/bin/env python

import os
import sys
import gensim.models

TESTS = [
  ('16 / 32', 'Calls', [
    ('store16','store32'),
    ('b43_piorx_read16','b43_piorx_read32'),
    ('__er16flash','__ew32flash'),
    ('si2165_writereg16','si2165_writereg32'),
    ('atmel_wmem16','atmel_wmem32'),
    ('oxygen_set_bits16','oxygen_set_bits32'),
    ('sil_iowrite16','sil_iowrite32'),
    ('vringh16_to_cpu','vringh32_to_cpu'),
    ('oxygen_write16','oxygen_write32'),
    ('skge_write16','skge_read32'),
    ('isp116x_read_reg16','isp116x_read_reg32'),
    ('xm_write16','xm_write32'),
    ('rtl8723au_write16','rtl8723au_write32'),
    ('virtio_cread16','virtio_cread32'),
    ('vmcs_write16','vmcs_write32'),
    ('put_unaligned_be16','put_unaligned_be32'),
    ('brcmu_maskget16','brcmu_maskget32'),
    ('__swab16s','__swab32s')
  ], 0),
  ('Add / Remove', 'Calls', [
    ('ntb_list_add','ntb_list_rm'),
    ('dev_exception_add','dev_exception_rm'),
    ('rmap_add','rmap_recycle'),
    ('qfq_add_to_agg','qfq_deact_rm_from_agg'),
    ('nbp_vlan_add','nbp_vlan_delete'),
    ('wimax_dev_add','wimax_dev_rm'),
    ('iwl_mvm_add_sta','iwl_mvm_rm_sta'),
    ('ieee80211_add_chanctx','ieee80211_del_chanctx'),
    ('sctp_assoc_add_peer','sctp_assoc_rm_peer')
  ], 0),
  ('Create / Destroy', 'Calls', [
    ('device_create','device_destroy'),
    ('CreateOSDWindow','DestroyOSDWindow'),
    ('bus_create','bus_destroy'),
    ('mlx5_core_create_psv','mlx5_core_destroy_psv'),
    ('lpfc_cq_create','lpfc_cq_destroy'),
    ('lpfc_create_shost','lpfc_destroy_shost'),
    ('lpfc_eq_create','lpfc_eq_destroy'),
    ('asd_create_ha_caches','asd_destroy_ha_caches'),
    ('lpfc_create_vport_work_array','lpfc_destroy_vport_work_array'),
    ('lpfc_wq_create','lpfc_wq_destroy'),
    ('lpfc_mq_create','lpfc_mq_destroy'),
    ('eb_create','eb_destroy'),
    ('macvlan_port_create','macvlan_port_destroy'),
    ('create_qp','destroy_qp'),
    ('bitmap_create','bitmap_destroy'),
    ('ib_create_ah','ib_destroy_ah'),
    ('i915_gem_obj_lookup_or_create_vma','i915_gem_vma_destroy'),
    ('ib_create_cm_id','ib_destroy_cm_id'),
    ('dma_pool_create','dma_pool_destroy')
  ], 0),
  ('Enable / Disable', 'Calls', [
    ('nv_enable_irq','nv_disable_irq'),
    ('bna_rxf_allmulti_enable','bna_rxf_allmulti_disable'),
    ('acpi_ec_burst_enable','acpi_ec_burst_disable'),
    ('bnx2_enable_bmsr1','bnx2_disable_bmsr1'),
    ('_rtl8821ae_enable_bcn_sub_func','_rtl8821ae_disable_bcn_sub_func'),
    ('tc358743_enable_edid','tc358743_disable_edid'),
    ('rtl92e_enable_nic','rtl92e_disable_nic'),
    ('iwl_scd_txq_enable_agg','iwl_scd_txq_disable_agg'),
    ('e1000_enable_phy_wakeup_reg_access_bm','e1000_disable_phy_wakeup_reg_access_bm'),
    ('_gk20a_pllg_enable','_gk20a_pllg_disable'),
    ('wm8996_bg_enable','wm8996_bg_disable'),
    ('b43_short_slot_timing_enable','b43_short_slot_timing_disable'),
    ('nvt_efm_enable','nvt_efm_disable'),
    ('qat_hal_enable_ctx','qat_hal_disable_ctx'),
    ('sctp_spp_sackdelay_enable','sctp_spp_sackdelay_disable'),
    ('b43legacy_short_slot_timing_enable','b43legacy_short_slot_timing_disable'),
    ('bnx2_test_and_enable_2g5','bnx2_test_and_disable_2g5'),
    ('perf_ibs_enable_event','perf_ibs_disable_event'),
    ('bnx2x_8483x_enable_eee','bnx2x_8483x_disable_eee'),
    ('dev_pm_enable_wake_irq','dev_pm_disable_wake_irq'),
    ('bcm_uart_enable','bcm_uart_disable'),
    ('bnx2_enable_nvram_access','bnx2_disable_nvram_access'),
    ('ixgbe_vlan_strip_enable','ixgbe_vlan_strip_disable'),
    ('cz_ih_enable_interrupts','cz_ih_disable_interrupts'),
    ('vmx_enable_intercept_msr_read_x2apic','vmx_disable_intercept_msr_read_x2apic'),
    ('iceland_ih_enable_interrupts','iceland_ih_disable_interrupts'),
    ('r8153_enable_aldps','r8153_disable_aldps'),
    ('vnt_mac_enable_protect_mode','vnt_mac_disable_protect_mode'),
    ('ahci_platform_enable_clks','ahci_platform_disable_clks'),
    ('bnx2_enable_forced_2g5','bnx2_disable_forced_2g5'),
    ('svnic_wq_enable','svnic_wq_disable'),
    ('rspi_enable_irq','rspi_disable_irq'),
    ('bnx2x_napi_enable','bnx2x_napi_disable'),
    ('xd_fill_pull_ctl_enable','xd_fill_pull_ctl_disable'),
    ('qla2x00_flash_enable','qla2x00_flash_disable'),
    ('i2c_int_enable','i2c_int_disable'),
    ('tonga_ih_enable_interrupts','tonga_ih_disable_interrupts'),
    ('vhost_enable_notify','vhost_disable_notify'),
    ('sony_pic_enable','sony_pic_disable'),
    ('enable_parport_interrupts','disable_parport_interrupts'),
    ('raw_enable_filters','raw_disable_filters'),
    ('enable_pipe_irq','disable_pipe_irq'),
    ('rsxx_enable_ier_and_isr','rsxx_disable_ier_and_isr'),
    ('intel_runtime_pm_enable_interrupts','intel_runtime_pm_disable_interrupts'),
    ('perf_pmu_enable','perf_pmu_disable'),
    ('nicvf_enable_intr','nicvf_disable_intr'),
    ('camif_hw_enable_scaler','camif_hw_disable_capture'),
    ('enable_transmit_ul','disable_transmit_ul'),
    ('usb_enable_interface','usb_disable_interface'),
    ('static_key_enable','static_key_disable'),
    ('nv_enable_hw_interrupts','nv_disable_hw_interrupts'),
    ('enable_irq_lockdep','disable_irq_lockdep'),
    ('local_bh_enable','local_bh_disable'),
    ('mlx5_ib_qp_enable_pagefaults','mlx5_ib_qp_disable_pagefaults'),
    ('bnx2x_napi_enable_cnic','bnx2x_napi_disable_cnic'),
    ('snd_soc_dapm_force_enable_pin','snd_soc_dapm_disable_pin'),
    ('efx_soft_enable_interrupts','efx_soft_disable_interrupts'),
    ('usb_enable_lpm','usb_disable_lpm'),
    ('pipe_irq_enable','disable_pipe_irq'),
    ('tg3_napi_enable','tg3_napi_disable'),
    ('tasklet_enable','tasklet_disable'),
    ('clk_prepare_enable','clk_disable_unprepare')
  ], 0),
  ('Enter / Exit', 'Calls', [
    ('otp_enter','otp_exit'),
    ('iwl_tt_enter_ct_kill','iwl_tt_exit_ct_kill'),
    ('trace_nfs_atomic_open_enter','trace_nfs_atomic_open_exit'),
    ('trace_nfs_lookup_revalidate_enter','trace_nfs_lookup_revalidate_exit'),
    ('trace_nfs_rename_enter','trace_nfs_rename_exit'),
    ('trace_ext4_truncate_enter','trace_ext4_truncate_exit'),
    ('mdc_enter_request','mdc_exit_request'),
    ('trace_ext4_ext_map_blocks_enter','trace_ext4_ext_map_blocks_exit'),
    ('acpi_ex_enter_interpreter','acpi_ex_exit_interpreter'),
    ('idle_enter_fair','idle_exit_fair'),
    ('lu_context_enter','lu_context_exit'),
    ('ist_enter','ist_exit')
  ], 0),
  ('In / Out', 'Calls', [
    ('add_in_dtd','add_out_dtd'),
    ('c2port_poll_in_busy','c2port_poll_out_ready'),
    ('nd_cmd_in_size','nd_cmd_out_size'),
    ('ep0_end_in_req','ep0_end_out_req'),
    ('fotg210_in_fifo_handler','fotg210_out_fifo_handler')
  ], 0),
  ('Inc / Dec', 'Calls', [
    ('cifs_in_send_inc','cifs_in_send_dec'),
    ('empty_child_inc','empty_child_dec'),
    ('rv6xx_step_voltage_if_increasing','rv6xx_step_voltage_if_decreasing'),
    ('increment_prob','decrement_prob'),
    ('hb_waiters_inc','hb_waiters_dec'),
    ('inc_mm_counter','dec_mm_counter'),
    ('inet_inc_convert_csum','inet_dec_convert_csum'),
    ('binder_inc_ref','binder_dec_ref'),
    ('static_key_slow_inc','static_key_slow_dec'),
    ('iscsit_inc_conn_usage_count','iscsit_dec_conn_usage_count')
  ], 0),
  ('Input / Output', 'Calls', [
    ('ivtv_get_input','ivtv_get_output'),
    ('ivtv_get_audio_input','ivtv_get_audio_output'),
    ('neo_set_no_input_flow_control','neo_set_no_output_flow_control'),
    ('DMAbuf_inputintr','DMAbuf_outputintr'),
    ('vou_adjust_input','vou_adjust_output')
  ], 0),
  ('Join / Leave', 'Calls', [
    ('handle_join_req','handle_leave_req'),
    ('f2fs_join_shrinker','f2fs_leave_shrinker'),
    ('drv_join_ibss','drv_leave_ibss'),
    ('cfg80211_ibss_wext_join','__cfg80211_leave_ibss')
  ], 0), 
  ('Lock / Unlock', 'Calls', [
    ('mutex_lock_nested','mutex_unlock'),
    ('lock_page','unlock_page'),
    ('fh_lock_nested','fh_unlock'),
    ('xfs_ilock','xfs_iunlock'),
    ('btrfs_tree_lock','btrfs_tree_unlock'),
    ('double_lock_hb','double_unlock_hb'),
    ('_raw_spin_lock_irqsave','_raw_spin_unlock_irqrestore'),
    ('lock_task_sighand','unlock_task_sighand'),
    ('netif_addr_lock','netif_addr_unlock'),
    ('task_rq_lock','task_rq_unlock'),
    ('xfs_dqlock','xfs_dqunlock'),
    ('cgroup_kn_lock_live','cgroup_kn_unlock'),
    ('lock_rsb','unlock_rsb'),
    ('ocfs2_rw_lock','ocfs2_rw_unlock'),
    ('spin_lock','spin_unlock'),
    ('rcu_read_lock','rcu_read_unlock'),
    ('_raw_spin_lock_irqsave','spin_unlock_irqrestore'),
    ('spin_lock_irq','spin_unlock_irq'),
    ('rcu_read_lock_sched_notrace','rcu_read_unlock_sched_notrace'),
    ('lock_buffer','unlock_buffer'),
    ('ipmi_ssif_lock_cond','ipmi_ssif_unlock_cond'),
    ('reiserfs_write_lock','reiserfs_write_unlock'),
    ('_raw_write_lock','_raw_write_unlock'),
    ('_raw_read_lock_irqsave','_raw_read_unlock_irqrestore'),
    ('ocfs2_inode_lock_full_nested','ocfs2_inode_unlock'),
    ('_raw_spin_lock_irq','_raw_spin_unlock_irq'),
    ('_raw_write_lock_irqsave','_raw_write_unlock_irqrestore'),
    ('ext4_lock_group','ext4_unlock_group'),
    ('spin_lock_bh','spin_unlock_bh'),
    ('_raw_read_lock','_raw_read_unlock'),
    ('reiserfs_write_lock_nested','reiserfs_write_unlock_nested'),
    ('lock_chunks','unlock_chunks'),
    ('srcu_read_lock','srcu_read_unlock'),
    ('task_lock','task_unlock'),
    ('f2fs_lock_op','f2fs_unlock_op'),
    ('_raw_spin_lock','_raw_spin_unlock'),
    ('queued_spin_lock','queued_spin_unlock'),
    ('btrfs_dev_replace_lock','btrfs_dev_replace_unlock'),
    ('gfs2_log_lock','gfs2_log_unlock'),
    ('write_seqlock','write_sequnlock'),
    ('_raw_write_lock_irq','_raw_write_unlock_irq'),
    ('console_lock','console_unlock'),
    ('rcu_read_lock_sched','rcu_read_unlock_sched'),
    ('lock_device_hotplug','unlock_device_hotplug'),
    ('pps_lock','pps_unlock'),
    ('drm_modeset_lock_all','drm_modeset_unlock_all'),
    ('amdgpu_ring_lock','amdgpu_ring_unlock_commit'),
    ('radeon_ring_lock','radeon_ring_unlock_commit'),
    ('bit_spin_lock','bit_spin_unlock'),
    ('threadgroup_lock','threadgroup_unlock'),
    ('mlx4_ib_lock_cqs','mlx4_ib_unlock_cqs'),
    ('hpfs_lock','hpfs_unlock'),
    ('lock_rename','unlock_rename')
  ], 0),
  ('On / Off', 'Calls', [
    ('b43_led_turn_on','b43_led_turn_off'),
    ('SiS_Chrontel701xBLOn','SiS_Chrontel701xBLOff'),
    ('vlv_force_pll_on','vlv_force_pll_off'),
    ('SiS_SiS30xBLOn','SiS_SiS30xBLOff'),
    ('__ieee80211_idle_on','__ieee80211_idle_off'),
    ('cfi_qry_mode_on','cfi_qry_mode_off'),
    ('neo_set_ixon_flow_control','neo_set_ixoff_flow_control'),
    ('probe_irq_on','probe_irq_off'),
    ('smiapp_power_on','smiapp_power_off'),
    ('mxser_set_must_xon1_value','mxser_set_must_xoff1_value'),
    ('lmc_led_on','lmc_led_off'),
    ('card_power_on','card_power_off'),
    ('vnt_mac_reg_bits_on','vnt_mac_reg_bits_off'),
    ('pmac_ohci_on','pmac_ohci_off'),
    ('netif_dormant_on','netif_dormant_off'),
    ('trace_hardirqs_on','trace_hardirqs_off'),
    ('phy_power_on','phy_power_off'),
    ('netif_carrier_on','netif_carrier_off'),
    ('lockdep_on','lockdep_off')
  ], 0),
  ('Read / Write', 'Calls', [
    ('memory_read','memory_write'),
    ('vt1724_midi_read','vt1724_midi_write'),
    ('hw_read_pci','hw_write_pci'),
    ('ftdi_elan_read_pcimem','ftdi_elan_write_pcimem'),
    ('intel_sbi_read','intel_sbi_write'),
    ('cyapa_i2c_read','cyapa_i2c_write'),
    ('ahd_read_flexport','ahd_write_flexport'),
    ('_rtl8723be_mdio_read','_rtl8723be_mdio_write'),
    ('ssb_chipco_pll_read','ssb_chipco_pll_write'),
    ('ntb_spad_read','ntb_peer_spad_write'),
    ('net2272_read_fifo','net2272_write_fifo'),
    ('ds1wm_read','ds1wm_write'),
    ('atl1c_read_phy_dbg','atl1c_write_phy_dbg'),
    ('rtl92de_read_dword_dbi','rtl92de_write_dword_dbi'),
    ('neo_flush_uart_read','neo_flush_uart_write'),
    ('friq_read_regr','friq_write_regr'),
    ('e1000_read_kmrn_reg_80003es2lan','e1000_write_kmrn_reg_80003es2lan'),
    ('vsp1_wpf_read','vsp1_wpf_write'),
    ('dsp3780I_ReadMsaCfg','dsp3780I_WriteMsaCfg'),
    ('af9015_read_reg_i2c','af9015_write_reg_i2c'),
    ('cls_flush_uart_read','cls_flush_uart_write'),
    ('bcmgenet_ext_readl','bcmgenet_ext_writel'),
    ('sr_read_rx_ctl','sr_write_rx_ctl'),
    ('cp2112_i2c_write_read_req','cp2112_i2c_write_req'),
    ('vid_blk_read_word','vid_blk_write_word'),
    ('vlv_bunit_read','vlv_bunit_write'),
    ('ocp_read_dword','ocp_write_dword'),
    ('amd_ec_read','amd_ec_write'),
    ('e1000e_read_kmrn_reg','e1000e_write_kmrn_reg'),
    ('rts51x_read_mem','rts51x_write_mem'),
    ('frpw_read_regr','frpw_write_regr'),
    ('winbond_readcfg','winbond_writecfg'),
    ('config_readw','config_writew'),
    ('__sst_read','__sst_write'),
    ('dw_mci_read_data_pio','dw_mci_write_data_pio'),
    ('bcmgenet_rdma_readl','bcmgenet_rdma_writel'),
    ('cit_read_reg','cit_write_reg'),
    ('nolock_regw_read','nolock_regw_write'),
    ('on26_read_regr','on26_write_regr'),
    ('b43legacy_hf_read','b43legacy_hf_write'),
    ('sata_pmp_read','sata_pmp_write'),
    ('ahd_pci_read_config','ahd_pci_write_config'),
    ('bfa_flash_read_send','bfa_flash_write_send'),
    ('rtl8187se_rf_readreg','rtl8187se_rf_writereg'),
    ('dib0090_fw_read_reg','dib0090_fw_write_reg'),
    ('__iwl_read_prph','__iwl_write_prph'),
    ('max8952_read_reg','max8952_write_reg'),
    ('pc87427_read8_bank','pc87427_write8_bank'),
    ('hw_read_id_reg','hw_write_id_reg'),
    ('cmu_rd','cmu_wr'),
    ('rd_reg16','wr_reg16'),
    ('spi_sh_read','spi_sh_write'),
    ('r852_read_reg','r852_write_reg'),
    ('musb_read_ulpi_buscontrol','musb_write_ulpi_buscontrol'),
    ('tifm_ms_read_data','tifm_ms_write_data'),
    ('smsc911x_mac_read','smsc911x_mac_write'),
    ('mtdchar_readoob','mtdchar_writeoob'),
    ('freecom_readdata','freecom_writedata'),
    ('cx24123_i2c_readreg','cx24123_i2c_writereg'),
    ('bcmgenet_tdma_readl','bcmgenet_tdma_writel'),
    ('r8152_mdio_read','r8152_mdio_write'),
    ('ast_read32','ast_write32'),
    ('bgx_reg_read','bgx_reg_write'),
    ('skd_reg_read32','skd_reg_write32')
  ], 0),
  ('Set / Get', 'Calls', [
    ('set_arg','get_arg'),
    ('m88rs2000_set_fec','m88rs2000_get_fec'),
    ('cifs_setlk','cifs_getlk'),
    ('mt2063_set_dnc_output_enable','mt2063_get_dnc_output_enable'),
    ('e1000_pcix_set_mmrbc','e1000_pcix_get_mmrbc'),
    ('mcs_set_reg','mcs_get_reg'),
    ('bcmgenet_bp_mc_set','bcmgenet_bp_mc_get'),
    ('tun_get_vnet_be','tun_set_vnet_be'),
    ('ivtvfb_get_osd_coords','ivtvfb_set_osd_coords'),
    ('obd_getattr','obd_setattr'),
    ('ODM_GetRFReg','ODM_SetRFReg'),
    ('cyapa_gen6_get_interval_setting','cyapa_gen6_set_interval_setting'),
    ('bcmgenet_bp_mc_get','bcmgenet_bp_mc_set'),
    ('i2400m_cmd_get_state','i2400m_set_init_config'),
    ('mcs_get_reg','mcs_set_reg'),
    ('xfs_ioc_getxflags','xfs_ioc_setxflags'),
    ('con_get_trans_new','con_set_trans_new'),
    ('maven_get_reg','maven_set_reg'),
    ('con_get_cmap','con_set_cmap'),
    ('ess_getmixer','ess_setmixer'),
    ('compat_get_fd_set','compat_set_fd_set'),
    ('gpiod_get_raw_value_cansleep','gpiod_set_raw_value_cansleep')
  ], 0), 
  ('Start / Stop', 'Calls', [
    ('nv_start_tx','nv_stop_tx'),
    ('nv_start_rx','nv_stop_rx'),
    ('hw_dac_start','hw_dac_stop'),
    ('wl1273_fm_start','wl1273_fm_stop'),
    ('iwlagn_tx_agg_start','iwlagn_tx_agg_stop'),
    ('iwl_mvm_sta_tx_agg_start','iwl_mvm_sta_tx_agg_stop'),
    ('lpphy_start_tx_tone','lpphy_stop_tx_tone'),
    ('pca_start','pca_stop'),
    ('dsp_dma_start','dsp_dma_stop'),
    ('sctp_cmd_hb_timers_start','sctp_cmd_hb_timers_stop'),
    ('tpu_pwm_timer_start','tpu_pwm_timer_stop'),
    ('start_preview','stop_preview'),
    ('i2c_start','i2c_stop'),
    ('pcnet32_netif_start','pcnet32_netif_stop'),
    ('vhost_poll_start','vhost_poll_stop'),
    ('mlx4_en_start_port','mlx4_en_stop_port'),
    ('rtllib_start_send_beacons','rtllib_stop_send_beacons'),
    ('ieee80211_start_tx_ba_cb','ieee80211_stop_tx_ba_cb'),
    ('start_ap_mode23a','stop_ap_mode23a'),
    ('hid_device_io_start','hid_device_io_stop'),
    ('start_ap_mode','stop_ap_mode'),
    ('__i2400m_dev_start','__i2400m_dev_stop'),
    ('bnx2_netif_start','bnx2_netif_stop'),
    ('lapb_start_t1timer','lapb_stop_t1timer'),
    ('start_sync_thread','stop_sync_thread'),
    ('efx_start_eventq','efx_stop_eventq'),
    ('ieee80211_start_send_beacons_rsl','ieee80211_stop_send_beacons_rsl'),
    ('hfa384x_drvr_start','hfa384x_drvr_stop'),
    ('start_timing','stop_timing'),
    ('efx_start_all','efx_stop_all'),
    ('__ext4_journal_start','__ext4_journal_stop')
  ], 0),
  ('Up / Down', 'Calls', [
    ('ixgbevf_up','ixgbevf_down'),
    ('bnx2x_update_link_up','bnx2x_update_link_down'),
    ('efx_reset_up','efx_reset_down'),
    ('odm_RateUp_8188E','odm_RateDown_8188E'),
    ('dwceqos_link_up','dwceqos_link_down'),
    ('ext4_double_up_write_data_sem','ext4_double_down_write_data_sem'),
    ('ipoib_ib_dev_up','ipoib_ib_dev_down'),
    ('walk_up_reloc_tree','walk_down_reloc_tree'),
    ('snd_hdac_power_up','snd_hdac_power_down'),
    ('walk_up_tree','walk_down_tree'),
    ('igb_up','igb_down'),
    ('i40e_up','i40e_down'),
    ('cpu_up','cpu_down'),
    ('__vxge_hw_device_handle_link_up_ind','__vxge_hw_device_handle_link_down_ind'),
    ('snd_hdac_power_up_pm','snd_hdac_power_down_pm'),
    ('__tipc_node_link_up','__tipc_node_link_down'),
    ('atl1_up','atl1_down'),
    ('up_read','down_read'),
    ('__qlcnic_up','__qlcnic_down'),
    ('e1000e_up','e1000e_down'),
    ('up_write','down_write'),
    ('vortex_up','vortex_down'),
    ('e1000_up','e1000_down'),
    ('up','down')
  ], 0),
  ('Ret Check / Call', 'Complex', [
    ('kzalloc_$NEQ_0','kzalloc'),
    ('devm_kzalloc_$NEQ_0','devm_kzalloc'),
    ('kmalloc_$NEQ_0','kmalloc'),
    ('alloc_pages_$NEQ_0','alloc_pages'),
    ('fb_alloc_cmap_$NEQ_0','fb_alloc_cmap'),
    ('alloc_etherdev_mqs_$NEQ_0','alloc_etherdev_mqs'),
    ('kcalloc_$NEQ_0','kcalloc'),
    ('comedi_alloc_subdev_readback_$NEQ_0','comedi_alloc_subdev_readback'),
    ('pci_alloc_consistent_$NEQ_0','pci_alloc_consistent'),
    ('vmalloc_$NEQ_0','vmalloc'),
    ('dev_alloc_skb_$NEQ_0','dev_alloc_skb'),
    ('alloc_skb_$NEQ_0','alloc_skb'),
    ('debugfs_create_file_$NEQ_0','debugfs_create_file'),
    ('proc_create_data_$NEQ_0','proc_create_data'),
    ('ioremap_$NEQ_0','ioremap'),
    ('kmem_cache_create_$NEQ_0','kmem_cache_create'),
    ('proc_mkdir_$NEQ_0','proc_mkdir'),
    ('add_uevent_var_$NEQ_0','add_uevent_var'),
    ('dma_alloc_coherent_$NEQ_0','dma_alloc_coherent'),
    ('ceph_buffer_new_$NEQ_0','ceph_buffer_new'),
    ('devm_input_allocate_device_$NEQ_0','devm_input_allocate_device')
  ], 0), 
  ('Ret Error / Prop', 'Comples', [
    ('write_bbt_$LT_0','$RET_write_bbt'),
    ('chipio_write_$LT_0','$RET_chipio_write'),
    ('ad9523_io_update_$LT_0','$RET_ad9523_io_update'),
    ('stb6100_write_reg_$LT_0','$RET_stb6100_write_reg'),
    ('smsc95xx_write_reg_$LT_0','$RET_smsc95xx_write_reg'),
    ('tm6000_i2c_recv_regs_$LT_0','$RET_tm6000_i2c_recv_regs'),
    ('rj54n1_sensor_scale_$LT_0','$RET_rj54n1_sensor_scale'),
    ('lowpan_nhc_do_compression_$LT_0','$RET_lowpan_nhc_do_compression'),
    ('add_automute_mode_enum_$LT_0','$RET_add_automute_mode_enum'),
    ('efx_filter_insert_filter_$LT_0','$RET_efx_filter_insert_filter'),
    ('sg_common_write_$LT_0','$RET_sg_common_write'),
    ('tm6000_i2c_recv_regs16_$LT_0','$RET_tm6000_i2c_recv_regs16'),
    ('stv0680_set_video_mode_$LT_0','$RET_stv0680_set_video_mode'),
    ('m5602_write_bridge_$LT_0','$RET_m5602_write_bridge'),
    ('adap_init0_tweaks_$LT_0','$RET_adap_init0_tweaks'),
    ('af9035_rd_reg_$LT_0','$RET_af9035_rd_reg'),
    ('soc_mbus_bytes_per_line_$LT_0','$RET_soc_mbus_bytes_per_line'),
    ('qsfp_cks_$LT_0','$RET_qsfp_cks'),
    ('ad9523_write_$LT_0','$RET_ad9523_write'),
    ('af9033_wr_reg_mask_$LT_0','$RET_af9033_wr_reg_mask'),
    ('f1x_lookup_addr_in_dct_$LT_0','$RET_f1x_lookup_addr_in_dct'),
    ('af9033_wr_reg_$LT_0','$RET_af9033_wr_reg'),
    ('usbduxfast_send_cmd_$LT_0','$RET_usbduxfast_send_cmd'),
    ('mv88e6xxx_reg_write_$LT_0','$RET_mv88e6xxx_reg_write'),
    ('scan_write_bbt_$LT_0','$RET_scan_write_bbt')
  ], 0),
  ('Check / Check', 'Fields', [
    ('?->dmaops','?->dmaops->altera_dtype'),
    ('?->dev->dev_private->mode_info.crtcs[0]','?->dev->dev_private->mode_info.crtcs[0]->enabled'),
    ('?->dev->ext_priv->tea6415c->ops->video','?->dev->ext_priv->tea6415c->ops->video->s_routing'),
    ('?->private->settings','?->private->settings->name'),
    ('?(&(*)->fl_list)','?(&(*)->fl_list)->next'),
    ('?->contexts[0].vif','?->contexts[0].vif->bss_conf.beacon_int'),
    ('?(*(&->mdsc->pool_perm_tree.rb_node))','?(*(&->mdsc->pool_perm_tree.rb_node))->pool'),
    ('?(*->dd_data)->phba->pport','?(*->dd_data)->phba->pport->cfg_log_verbose'),
    ('?->pool->busy_hash[0].first','?->pool->busy_hash[0].first->current_pwq'),
    ('?->txdata_ptr[0]','?->txdata_ptr[0]->tx_cons_sb'),
    ('?.PhysicalDeviceInformation[0]','?.PhysicalDeviceInformation[0]->TargetID'),
    ('?(&.RfDependCmd[?])','?(&.RfDependCmd[?])->CmdID'),
    ('?->dev->ext_priv->tea6415c','?->dev->ext_priv->tea6415c->ops->video'),
    ('?->sd_extmux','?->sd_extmux->ops->audio'),
    ('?->data->queue.card','?->data->queue.card->state'),
    ('?->sd_cx25840->ops->video','?->sd_cx25840->ops->video->s_routing'),
    ('?(*)->i_itemp','?(*)->i_itemp->li_flags'),
    ('?->sd_cx25840->ops->audio','?->sd_cx25840->ops->audio->s_routing'),
    ('?(*(&(&->link)->defaults))','?(*(&(&->link)->defaults))->level'),
    ('?->crypt[?]','?->crypt[?]->ops'),
    ('?(&.PreCommonCmd[?])','?(&.PreCommonCmd[?])->CmdID'),
    ('?->l_iclog','?->l_iclog->ic_next'),
    ('?->irm_node->data','?->irm_node->data->config_rom'),
    ('?(*)->tparent','?(*)->tparent->common.classid'),
    ('?->table[?]->ht[?]','?->table[?]->ht[?]->handle'),
    ('?->bss_conf.beacon_rate','?->bss_conf.beacon_rate->bitrate'),
    ('?->ichd[4].pcm','?->ichd[4].pcm->r[0].codec[1]'),
    ('?->ext_priv->saa7111a->ops->core','?->ext_priv->saa7111a->ops->core->s_gpio'),
    ('?->fw_dump_trig','?->fw_dump_trig->mode'),
    ('?->ibc_cmid','?->ibc_cmid->qp'),
    ('?->driver_data->dlc','?->driver_data->dlc->session'),
    ('?->sd_cx25840->ops->core','?->sd_cx25840->ops->core->load_fw'),
    ('?(&->uart_port.state->port)->tty','?(&->uart_port.state->port)->tty->termios.c_cflag'),
    ('?->private_data->q.list.next','?->private_data->q.list.next->reader'),
    ('?(&->lq_sta)','?(&->lq_sta)->pers.drv'),
    ('?(&[?])->adapter','?(&[?])->adapter->type'),
    ('?->task->dev->parent','?->task->dev->parent->dev_type'),
    ('?->dev->mfc_cmds','?->dev->mfc_cmds->cmd_host2risc'),
    ('?->prev->sym->prop','?->prev->sym->prop->menu'),
    ('?->dev_data->atm_dev->phy','?->dev_data->atm_dev->phy->start'),
    ('?(*(&(*(&->dev[?].towrite))->bi_next))','?(*(&(*(&->dev[?].towrite))->bi_next))->bi_iter.bi_sector'),
    ('?(&->priv->op_mode_specific)->csa_vif','?(&->priv->op_mode_specific)->csa_vif->csa_active'),
    ('?->intf->handlers','?->intf->handlers->dec_usecount'),
    ('?->sd_ir->ops->core','?->sd_ir->ops->core->interrupt_service_routine'),
    ('?.crypt->ops','?.crypt->ops->encrypt_mpdu'),
    ('?.driver_data[0]->vif','?.driver_data[0]->vif->type'),
    ('?->mdio_bus->phy_map[?]','?->mdio_bus->phy_map[?]->drv'),
    ('?->sd_video->ops->core','?->sd_video->ops->core->load_fw'),
    ('?(*)->cl_parent','?(*)->cl_parent->cl_common.classid'),
    ('?->ext_priv->tea6415c->ops->video','?->ext_priv->tea6415c->ops->video->s_routing')
  ], 0),
  ('Next / Prev', 'Fields', [
    ('!.task_list.next','!.task_list.prev'),
    ('!->t_cpnext','!->t_cpprev'),
    ('?->nl_entry.next','?->nl_entry.prev'),
    ('!.hn_item.next','!.hn_item.prev'),
    ('!.pending.next','!.pending.prev'),
    ('!.ns_node_item.next','!.ns_node_item.prev'),
    ('!.src_csets.next','!.src_csets.prev'),
    ('!.list.next','!.list.prev'),
    ('!.dst_csets.next','!.dst_csets.prev'),
    ('?->waitnext','?->waitprev'),
    ('!->fib_next','!->fib_prev'),
    ('?->conf->mlist.next->dsp->rx_R','?->conf->mlist.prev->dsp->rx_R'),
    ('?->async.next','?->async.prev'),
    ('!.next','!.prev'),
    ('?->pending_locks.next','?->pending_locks.prev'),
    ('?->modelist.next','?->modelist.prev')
  ], 0),
  ('Test / Set', 'Fields', [
    ('?->at_current','!->at_current'),
    ('?->kar','!->kar'),
    ('?->old_discards','!->old_discards'),
    ('?->bankw','!->bankw'),
    ('?->field_width','!->field_width'),
    ('?->rq.queue','!->rq.queue'),
    ('?->unblock_action','!->unblock_action'),
    ('?->ctl_efx_send_volume','!->ctl_efx_send_volume'),
    ('?->sbuf','!->sbuf'),
    ('?->bmme_flags','!->bmme_flags'),
    ('?->phwi_ctrlr','!->phwi_ctrlr'),
    ('?->eq_table.uar_map','!->eq_table.uar_map'),
    ('?->restore_user','!->restore_user'),
    ('?->nic_vbase','!->nic_vbase'),
    ('?->tmr_req','!->tmr_req'),
    ('?->gpr_map','!->gpr_map'),
    ('?->mtilea','!->mtilea'),
    ('?->ctl_attn','!->ctl_attn'),
    ('?->ctl_efx_attn','!->ctl_efx_attn'),
    ('?->dec_mem','!->dec_mem'),
    ('?->dmab','!->dmab'),
    ('?->gp_max','!->gp_max'),
    ('?->swizzle_mode','!->swizzle_mode'),
    ('?->fminterval','!->fminterval'),
    ('?->slowpath','!->slowpath'),
    ('?.auto_white_balance','!.auto_white_balance'),
    ('?->ctrl_buff','!->ctrl_buff'),
    ('?.exposure_auto','!.exposure_auto'),
    ('?->ctl_send_volume','!->ctl_send_volume'),
    ('?->peb_buf','!->peb_buf'),
    ('?->maxpressure','!->maxpressure'),
    ('?->ext_caps','!->ext_caps'),
    ('?->init_ops_offsets','!->init_ops_offsets'),
    ('?->gtt.mappable','!->gtt.mappable'),
    ('?->port_array','!->port_array'),
    ('?->creg','!->creg'),
    ('?->usb3_ports','!->usb3_ports'),
    ('?->no_ldrive','!->no_ldrive'),
    ('?->maxtilt_Y','!->maxtilt_Y')
  ], 0)
]


def solve_analogy(passed, failed, total, oov, A, B, C, D, K, M):
  '''
  solve_analogy: 
    1. Solves the analogy A is to B as C is to ??
    2. Checks to see if any of the top-K solution match 
       the ground truth (D). 
    3. Increments counters appropriately
  '''
  # Did we find our match
  found = False

  try:
    # Go through the K most similar 
    for w,_ in M.wv.most_similar(topn=K, positive=[B,C], negative=[A]):
      # See if the result matches the ground-truth
      if w == D:
        # It does! break out se we can do some tallying
        found=True
        break
    
    # If we found it great!
    if found:
      return (passed+1, failed, total+1, oov)
    else:
      # Not found :( 
      return (passed, failed+1, total+1, oov)
  
  # Exceptions are triggered when a word is OOV (out-of-vocabulary)
  except Exception as e:
    # In this case we increment the OOV count
    return (passed, failed, total, oov+1)
    

def run_suite(suite, passed_in, failed_in, total_in, oov_in, K, M):
  '''
  run_suite:
    1. Prints a header for the given test suite
    2. Initializes counters for the test suite
    3. Ensures suite is non-empty
    4. Takes all pairs-of-pairs of functions in the suite 
       and forms analogies
    5. Increments all counters appropriately
  '''
  print('  Running {} ({}):'.format(
    suite[0], 
    len(suite[2])
  ))

  # Initialize counters!
  suiteSize = len(suite[2]) * len(suite[2]) - len(suite[2])
  passed = 0
  failed = 0
  total = 0
  oov = 0

  # Ensure suite is non-empty
  if suiteSize == 0:
    print('    Suite empty')
    return (passed_in, failed_in, total_in, oov_in)

  # Run through pairs-of-pairs
  for A,B in suite[2]:
    for C,D in suite[2]:
      # Ignore diagonal (trivial)
      if A == C and B == D: 
        continue

      # Run analogy solver and increment counts
      passed, failed, total, oov = \
        solve_analogy(
          passed, failed, total, oov, # Counters
          A, B, C, D,                 # Ground-truth
          K, M                        # Model params
        )

  # Don't divide by zero!
  if total != 0:
    print('    Passed {}/{} ({:.2%})'.format(
      passed, total, float(passed) / float(total)
    ))
  else:
    print('    Passed {}/{} (0.00%)'.format(
      passed, total
    ))

  # If there were any OOV words, print the count now
  if oov > 0:
    print('    Note: {}/{} out of vocabulary'.format(oov,suiteSize))
  
  # Return aggregate counters
  return (
    passed_in + passed, 
    failed_in + failed, 
    total_in + total, 
    oov_in + oov
  )


def run_all(tests, K, M):
  '''
  run_all:
    Runs all tests in our analogies benchmark. 
    Keeps track of aggregate stats.
  '''
  print('Running {} tests:'.format(len(tests)))

  benchmarkSize = 0
  passed = 0
  failed = 0
  total = 0
  oov = 0

  # Do each test
  for suite in tests:
    # Keep track of running totals
    passed, failed, total, oov = \
      run_suite(suite, passed, failed, total, oov, K, M)
    benchmarkSize = \
      benchmarkSize + (len(suite[2]) * len(suite[2]) - len(suite[2]))

  # Print a nice summary
  print('SUMMARY:')
  # Again, don't divide by zero
  if total != 0:
    print('  Passed {}/{} ({:.2%})'.format(
      passed, total, float(passed) / float(total)
    ))
  else:
    print('  Passed {}/{} (0.00%)'.format(
      passed, total
    ))
  print('  {}/{} out of vocabulary'.format(oov, benchmarkSize))


# Actual entrypoint
if __name__ == '__main__':
  if len(sys.argv) <= 1:
    print(
      'Error: please specify (at a minimum) the path to the gensim compatible'
      + ' non-binary vectors you wish to use'
    )

  # Two params, word vectors (stored in gensim compatible non-binary format)
  P = sys.argv[1]
  # K value (defaults to 1, so top-1 performance)
  K = int(sys.argv[2]) if len(sys.argv) > 2 else 1

  # Print parameters
  print('Loading model from: {}'.format(P))
  print('K is set to: {}'.format(K))
  
  # Load model (CAN BE VERY SLOW)
  M = gensim.models.KeyedVectors.load_word2vec_format(P, binary=False)
  
  # Run the tests!
  run_all(TESTS, K, M)
  