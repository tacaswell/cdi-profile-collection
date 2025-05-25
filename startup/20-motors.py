from cditools.motors import (
    BPMDM3,
    BPMDM4,
    FSDM2,
    FSDM3,
    FSHPM,
    FSVPM,
    IMDM2,
    FltrDM1,
    Gon1,
    MirHPM,
    MirKBh,
    MirKBv,
    MirVPM,
    MonoDMM,
    MonoHDCM,
    Qstar1,
    SltBCUD,
    SltBCUU,
    SltDM3,
    SltHPM,
    SltVPM,
    SltWB1,
    WndExit,
)

slt_wb1 = SltWB1(prefix="XF:09IDA-OP:1{Slt:WB1", name="slt_wb1", labels=["motors"])
slt_wb1.wait_for_connection(timeout=10.0)

fltr_dm1 = FltrDM1(prefix="XF:09IDA-OP:1{Fltr:DM1", name="fltr_dm1", labels=["motors"])
fltr_dm1.wait_for_connection(timeout=10.0)

fsvpm = FSVPM(prefix="XF:09IDA-OP:1{FS:VPM", name="fsvpm", labels=["motors"])
fsvpm.wait_for_connection(timeout=10.0)

fshpm = FSHPM(prefix="XF:09IDA-OP:1{FS:HPM", name="fshpm", labels=["motors"])
fshpm.wait_for_connection(timeout=10.0)

fsdm2 = FSDM2(prefix="XF:09IDA-OP:1{FS:DM2", name="fsdm2", labels=["motors"])
fsdm2.wait_for_connection(timeout=10.0)

# mono_dmm = MonoDMM(prefix="XF:09IDA-OP:1{Mono:DMM", name="mono_dmm", labels=["motors"])
# mono_dmm.wait_for_connection(timeout=10.0)

mono_hdcm = MonoHDCM(
    prefix="XF:09IDA-OP:1{Mono:HDCM", name="mono_hdcm", labels=["motors"]
)
mono_hdcm.wait_for_connection(timeout=10.0)

slt_vpm = SltVPM(prefix="XF:09IDA-OP:1{Slt:VPM", name="slt_vpm", labels=["motors"])
slt_vpm.wait_for_connection(timeout=10.0)

slt_hpm = SltHPM(prefix="XF:09IDA-OP:1{Slt:HPM", name="slt_hpm", labels=["motors"])
slt_hpm.wait_for_connection(timeout=10.0)

mir_vpm = MirVPM(prefix="XF:09IDA-OP:1{Mir:VPM", name="mir_vpm", labels=["motors"])
mir_vpm.wait_for_connection(timeout=10.0)

imdm2 = IMDM2(prefix="XF:09IDA-OP:1{IM:DM2", name="imdm2", labels=["motors"])
imdm2.wait_for_connection(timeout=10.0)

mir_hpm = MirHPM(prefix="XF:09IDA-OP:1{Mir:HPM", name="mir_hpm", labels=["motors"])
mir_hpm.wait_for_connection(timeout=10.0)

slt_dm3 = SltDM3(prefix="XF:09IDB-OP:1{Slt:DM3", name="slt_dm3", labels=["motors"])
slt_dm3.wait_for_connection(timeout=10.0)

bpm_dm3 = BPMDM3(prefix="XF:09IDB-OP:1{BPM:DM3", name="bpm_dm3", labels=["motors"])
bpm_dm3.wait_for_connection(timeout=10.0)

fsdm3 = FSDM3(prefix="XF:09IDB-OP:1{FS:DM3", name="fsdm3", labels=["motors"])
fsdm3.wait_for_connection(timeout=10.0)

# mir_kbv = MirKBv(prefix="XF:09IDC-OP:1{Mir:KBv", name="mir_kbv", labels=["motors"])
# mir_kbv.wait_for_connection(timeout=10.0)
#
# mir_kbh = MirKBh(prefix="XF:09IDC-OP:1{Mir:KBh", name="mir_kbh", labels=["motors"])
# mir_kbh.wait_for_connection(timeout=10.0)
#
# bpm_dm4 = BPMDM4(prefix="XF:09IDC-OP:1{BPM:DM4", name="bpm_dm4", labels=["motors"])
# bpm_dm4.wait_for_connection(timeout=10.0)
#
# wnd_exit = WndExit(prefix="XF:09IDC-OP:1{Wnd:Exit", name="wnd_exit", labels=["motors"])
# wnd_exit.wait_for_connection(timeout=10.0)
#
# gon1 = Gon1(prefix="XF:09IDC-OP:1{Gon:1", name="gon1", labels=["motors"])
# gon1.wait_for_connection(timeout=10.0)
#
# slt_bcuu = SltBCUU(prefix="XF:09IDC-OP:1{Slt:BCUU", name="slt_bcuu", labels=["motors"])
# slt_bcuu.wait_for_connection(timeout=10.0)
#
# slt_bcud = SltBCUD(prefix="XF:09IDC-OP:1{Slt:BCUD", name="slt_bcud", labels=["motors"])
# slt_bcud.wait_for_connection(timeout=10.0)
#
# qstar1 = Qstar1(prefix="XF:09IDC-OP:1{Qstar:1", name="qstar1", labels=["motors"])
# qstar1.wait_for_connection(timeout=10.0)
