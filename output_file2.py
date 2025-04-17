#!/usr/bin/env python
from ophyd import Device, Component as Cpt, EpicsMotor

# Auto-generated Ophyd device classes

class SltWB1(Device):
    """Ophyd Device for Slt WB1"""
    i = Cpt(EpicsMotor, '-Ax:I}Mtr')
    o = Cpt(EpicsMotor, '-Ax:O}Mtr')
    b = Cpt(EpicsMotor, '-Ax:B}Mtr')
    t = Cpt(EpicsMotor, '-Ax:T}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Slt:WB1}'
    _default_read_attrs = ['i', 'o', 'b', 't', 'hg', 'hc', 'vg', 'vc']

# Instantiate slt_wb1
slt_wb1 = SltWB1(prefix='XF:09IDA-OP:1{Slt:WB1', name='slt_wb1')

class FltrDM1(Device):
    """Ophyd Device for Fltr DM1"""
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Fltr:DM1}'
    _default_read_attrs = ['y']

# Instantiate fltr_dm1
fltr_dm1 = FltrDM1(prefix='XF:09IDA-OP:1{Fltr:DM1', name='fltr_dm1')

class FSVPM(Device):
    """Ophyd Device for FS VPM"""
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{FS:VPM}'
    _default_read_attrs = ['y']

# Instantiate fs_vpm
fs_vpm = FSVPM(prefix='XF:09IDA-OP:1{FS:VPM', name='fs_vpm')

class FSHPM(Device):
    """Ophyd Device for FS HPM"""
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{FS:HPM}'
    _default_read_attrs = ['y']

# Instantiate fs_hpm
fs_hpm = FSHPM(prefix='XF:09IDA-OP:1{FS:HPM', name='fs_hpm')

class FSDM2(Device):
    """Ophyd Device for FS DM2"""
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{FS:DM2}'
    _default_read_attrs = ['y']

# Instantiate fs_dm2
fs_dm2 = FSDM2(prefix='XF:09IDA-OP:1{FS:DM2', name='fs_dm2')

class MonoDMM(Device):
    """Ophyd Device for Mono DMM"""
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    bragg = Cpt(EpicsMotor, '-Ax:Bragg}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    tz = Cpt(EpicsMotor, '-Ax:TZ}Mtr')
    fp = Cpt(EpicsMotor, '-Ax:FP}Mtr')
    fr = Cpt(EpicsMotor, '-Ax:FR}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Mono:DMM}'
    _default_read_attrs = ['tx', 'ty', 'bragg', 'roll', 'hg', 'pitch', 'tz', 'fp', 'fr']

# Instantiate mono_dmm
mono_dmm = MonoDMM(prefix='XF:09IDA-OP:1{Mono:DMM', name='mono_dmm')

class MonoHDCM(Device):
    """Ophyd Device for Mono HDCM"""
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    bragg = Cpt(EpicsMotor, '-Ax:Bragg}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    fp = Cpt(EpicsMotor, '-Ax:FP}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Mono:HDCM}'
    _default_read_attrs = ['tx', 'ty', 'bragg', 'hg', 'pitch', 'roll', 'fp']

# Instantiate mono_hdcm
mono_hdcm = MonoHDCM(prefix='XF:09IDA-OP:1{Mono:HDCM', name='mono_hdcm')

class SltVPM(Device):
    """Ophyd Device for Slt VPM"""
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Slt:VPM}'
    _default_read_attrs = ['hg', 'hc', 'vg', 'vc']

# Instantiate slt_vpm
slt_vpm = SltVPM(prefix='XF:09IDA-OP:1{Slt:VPM', name='slt_vpm')

class SltHPM(Device):
    """Ophyd Device for Slt HPM"""
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Slt:HPM}'
    _default_read_attrs = ['hg', 'hc', 'vg', 'vc']

# Instantiate slt_hpm
slt_hpm = SltHPM(prefix='XF:09IDA-OP:1{Slt:HPM', name='slt_hpm')

class MirVPM(Device):
    """Ophyd Device for Mir VPM"""
    yuc = Cpt(EpicsMotor, '-Ax:YUC}Mtr')
    ydi = Cpt(EpicsMotor, '-Ax:YDI}Mtr')
    ydo = Cpt(EpicsMotor, '-Ax:YDO}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ub = Cpt(EpicsMotor, '-Ax:UB}Mtr')
    db = Cpt(EpicsMotor, '-Ax:DB}Mtr')
    bnd = Cpt(EpicsMotor, '-Ax:Bnd}Mtr')
    bndoff = Cpt(EpicsMotor, '-Ax:BndOff}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Mir:VPM}'
    _default_read_attrs = ['yuc', 'ydi', 'ydo', 'pitch', 'roll', 'ty', 'tx', 'ub', 'db', 'bnd', 'bndoff']

# Instantiate mir_vpm
mir_vpm = MirVPM(prefix='XF:09IDA-OP:1{Mir:VPM', name='mir_vpm')

class IMDM2(Device):
    """Ophyd Device for IM DM2"""
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{IM:DM2}'
    _default_read_attrs = ['y']

# Instantiate im_dm2
im_dm2 = IMDM2(prefix='XF:09IDA-OP:1{IM:DM2', name='im_dm2')

class MirHPM(Device):
    """Ophyd Device for Mir HPM"""
    yuc = Cpt(EpicsMotor, '-Ax:YUC}Mtr')
    ydi = Cpt(EpicsMotor, '-Ax:YDI}Mtr')
    ydo = Cpt(EpicsMotor, '-Ax:YDO}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    ub = Cpt(EpicsMotor, '-Ax:UB}Mtr')
    db = Cpt(EpicsMotor, '-Ax:DB}Mtr')
    bnd = Cpt(EpicsMotor, '-Ax:Bnd}Mtr')
    bndoff = Cpt(EpicsMotor, '-Ax:BndOff}Mtr')
    xu = Cpt(EpicsMotor, '-Ax:XU}Mtr')
    xd = Cpt(EpicsMotor, '-Ax:XD}Mtr')
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    yaw = Cpt(EpicsMotor, '-Ax:Yaw}Mtr')
    _default_prefix = 'XF:09IDA-OP:1{Mir:HPM}'
    _default_read_attrs = ['yuc', 'ydi', 'ydo', 'pitch', 'roll', 'ty', 'ub', 'db', 'bnd', 'bndoff', 'xu', 'xd', 'tx', 'yaw']

# Instantiate mir_hpm
mir_hpm = MirHPM(prefix='XF:09IDA-OP:1{Mir:HPM', name='mir_hpm')

class SltDM3(Device):
    """Ophyd Device for Slt DM3"""
    i = Cpt(EpicsMotor, '-Ax:I}Mtr')
    o = Cpt(EpicsMotor, '-Ax:O}Mtr')
    b = Cpt(EpicsMotor, '-Ax:B}Mtr')
    t = Cpt(EpicsMotor, '-Ax:T}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDB-OP:1{Slt:DM3}'
    _default_read_attrs = ['i', 'o', 'b', 't', 'hg', 'hc', 'vg', 'vc']

# Instantiate slt_dm3
slt_dm3 = SltDM3(prefix='XF:09IDB-OP:1{Slt:DM3', name='slt_dm3')

class BPMDM3(Device):
    """Ophyd Device for BPM DM3"""
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    foil = Cpt(EpicsMotor, '-Ax:Foil}Mtr')
    _default_prefix = 'XF:09IDB-OP:1{BPM:DM3}'
    _default_read_attrs = ['tx', 'ty', 'foil']

# Instantiate bpm_dm3
bpm_dm3 = BPMDM3(prefix='XF:09IDB-OP:1{BPM:DM3', name='bpm_dm3')

class FSDM3(Device):
    """Ophyd Device for FS DM3"""
    fs = Cpt(EpicsMotor, '-Ax:FS}Mtr')
    _default_prefix = 'XF:09IDB-OP:1{FS:DM3}'
    _default_read_attrs = ['fs']

# Instantiate fs_dm3
fs_dm3 = FSDM3(prefix='XF:09IDB-OP:1{FS:DM3', name='fs_dm3')

class MirKBv(Device):
    """Ophyd Device for Mir KBv"""
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    yuc = Cpt(EpicsMotor, '-Ax:YUC}Mtr')
    ydi = Cpt(EpicsMotor, '-Ax:YDI}Mtr')
    ydo = Cpt(EpicsMotor, '-Ax:YDO}Mtr')
    yaw = Cpt(EpicsMotor, '-Ax:Yaw}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    tz = Cpt(EpicsMotor, '-Ax:TZ}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    fs = Cpt(EpicsMotor, '-Ax:FS}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Mir:KBv}'
    _default_read_attrs = ['hg', 'hc', 'vg', 'vc', 'yuc', 'ydi', 'ydo', 'yaw', 'roll', 'ty', 'tx', 'tz', 'pitch', 'fs']

# Instantiate mir_kbv
mir_kbv = MirKBv(prefix='XF:09IDC-OP:1{Mir:KBv', name='mir_kbv')

class MirKBh(Device):
    """Ophyd Device for Mir KBh"""
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    yuc = Cpt(EpicsMotor, '-Ax:YUC}Mtr')
    ydi = Cpt(EpicsMotor, '-Ax:YDI}Mtr')
    ydo = Cpt(EpicsMotor, '-Ax:YDO}Mtr')
    yaw = Cpt(EpicsMotor, '-Ax:Yaw}Mtr')
    roll = Cpt(EpicsMotor, '-Ax:Roll}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    tz = Cpt(EpicsMotor, '-Ax:TZ}Mtr')
    pitch = Cpt(EpicsMotor, '-Ax:Pitch}Mtr')
    fs = Cpt(EpicsMotor, '-Ax:FS}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Mir:KBh}'
    _default_read_attrs = ['hg', 'hc', 'vg', 'vc', 'yuc', 'ydi', 'ydo', 'yaw', 'roll', 'ty', 'tx', 'tz', 'pitch', 'fs']

# Instantiate mir_kbh
mir_kbh = MirKBh(prefix='XF:09IDC-OP:1{Mir:KBh', name='mir_kbh')

class BPMDM4(Device):
    """Ophyd Device for BPM DM4"""
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{BPM:DM4}'
    _default_read_attrs = ['tx', 'ty']

# Instantiate bpm_dm4
bpm_dm4 = BPMDM4(prefix='XF:09IDC-OP:1{BPM:DM4', name='bpm_dm4')

class WndExit(Device):
    """Ophyd Device for Wnd Exit"""
    tx = Cpt(EpicsMotor, '-Ax:TX}Mtr')
    ty = Cpt(EpicsMotor, '-Ax:TY}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Wnd:Exit}'
    _default_read_attrs = ['tx', 'ty']

# Instantiate wnd_exit
wnd_exit = WndExit(prefix='XF:09IDC-OP:1{Wnd:Exit', name='wnd_exit')

class Gon1(Device):
    """Ophyd Device for Gon 1"""
    rx1 = Cpt(EpicsMotor, '-Ax:Rx1}Mtr')
    rz1 = Cpt(EpicsMotor, '-Ax:Rz1}Mtr')
    rx2 = Cpt(EpicsMotor, '-Ax:Rx2}Mtr')
    rz2 = Cpt(EpicsMotor, '-Ax:Rz2}Mtr')
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    ry = Cpt(EpicsMotor, '-Ax:Ry}Mtr')
    x1 = Cpt(EpicsMotor, '-Ax:X1}Mtr')
    z1 = Cpt(EpicsMotor, '-Ax:Z1}Mtr')
    x2 = Cpt(EpicsMotor, '-Ax:X2}Mtr')
    z2 = Cpt(EpicsMotor, '-Ax:Z2}Mtr')
    rx3 = Cpt(EpicsMotor, '-Ax:Rx3}Mtr')
    rz3 = Cpt(EpicsMotor, '-Ax:Rz3}Mtr')
    x3 = Cpt(EpicsMotor, '-Ax:X3}Mtr')
    y3 = Cpt(EpicsMotor, '-Ax:Y3}Mtr')
    z3 = Cpt(EpicsMotor, '-Ax:Z3}Mtr')
    visual = Cpt(EpicsMotor, '-Ax:Visual}Mtr')
    xp = Cpt(EpicsMotor, '-Ax:XP}Mtr')
    yp = Cpt(EpicsMotor, '-Ax:YP}Mtr')
    zp = Cpt(EpicsMotor, '-Ax:ZP}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Gon:1}'
    _default_read_attrs = ['rx1', 'rz1', 'rx2', 'rz2', 'y', 'ry', 'x1', 'z1', 'x2', 'z2', 'rx3', 'rz3', 'x3', 'y3', 'z3', 'visual', 'xp', 'yp', 'zp']

# Instantiate gon_1
gon_1 = Gon1(prefix='XF:09IDC-OP:1{Gon:1', name='gon_1')

class SltBCUU(Device):
    """Ophyd Device for Slt BCUU"""
    i = Cpt(EpicsMotor, '-Ax:I}Mtr')
    o = Cpt(EpicsMotor, '-Ax:O}Mtr')
    b = Cpt(EpicsMotor, '-Ax:B}Mtr')
    t = Cpt(EpicsMotor, '-Ax:T}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Slt:BCUU}'
    _default_read_attrs = ['i', 'o', 'b', 't', 'hg', 'hc', 'vg', 'vc']

# Instantiate slt_bcuu
slt_bcuu = SltBCUU(prefix='XF:09IDC-OP:1{Slt:BCUU', name='slt_bcuu')

class SltBCUD(Device):
    """Ophyd Device for Slt BCUD"""
    i = Cpt(EpicsMotor, '-Ax:I}Mtr')
    o = Cpt(EpicsMotor, '-Ax:O}Mtr')
    b = Cpt(EpicsMotor, '-Ax:B}Mtr')
    t = Cpt(EpicsMotor, '-Ax:T}Mtr')
    hg = Cpt(EpicsMotor, '-Ax:HG}Mtr')
    hc = Cpt(EpicsMotor, '-Ax:HC}Mtr')
    vg = Cpt(EpicsMotor, '-Ax:VG}Mtr')
    vc = Cpt(EpicsMotor, '-Ax:VC}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Slt:BCUD}'
    _default_read_attrs = ['i', 'o', 'b', 't', 'hg', 'hc', 'vg', 'vc']

# Instantiate slt_bcud
slt_bcud = SltBCUD(prefix='XF:09IDC-OP:1{Slt:BCUD', name='slt_bcud')

class Qstar1(Device):
    """Ophyd Device for Qstar 1"""
    1 = Cpt(EpicsMotor, '-Ax:1}Mtr')
    2 = Cpt(EpicsMotor, '-Ax:2}Mtr')
    3 = Cpt(EpicsMotor, '-Ax:3}Mtr')
    _default_prefix = 'XF:09IDC-OP:1{Qstar:1}'
    _default_read_attrs = ['1', '2', '3']

# Instantiate qstar_1
qstar_1 = Qstar1(prefix='XF:09IDC-OP:1{Qstar:1', name='qstar_1')
