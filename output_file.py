#!/usr/bin/env python
from ophyd import Device, Component as Cpt, EpicsMotor

# Auto-generated Ophyd device classes

class SampleStage(Device):
    """Ophyd Device for Sample Stage"""
    SAMPLE_X = Cpt(EpicsMotor, 'X}')
    SAMPLE_Y = Cpt(EpicsMotor, 'Y}')
    SAMPLE_Z = Cpt(EpicsMotor, 'Z}')
    _default_prefix = 'XF:31IDA-OP:1{Stg:'
    _default_read_attrs = ['SAMPLE_X', 'SAMPLE_Y', 'SAMPLE_Z']

# Instantiate Sample Stage
SAMPLE = SampleStage(name='SAMPLE')

class KBMirrors(Device):
    """Ophyd Device for KB Mirrors"""
    KB_VFM = Cpt(EpicsMotor, 'Ax:VFM}')
    KB_HFM = Cpt(EpicsMotor, 'Ax:HFM}')
    _default_prefix = 'XF:31IDA-OP:1{Mir:KB-'
    _default_read_attrs = ['KB_VFM', 'KB_HFM']

# Instantiate KB Mirrors
KB = KBMirrors(name='KB')

class Monochromator(Device):
    """Ophyd Device for Monochromator"""
    MONO_Energy = Cpt(EpicsMotor, 'Ax:Energy}')
    MONO_Bragg = Cpt(EpicsMotor, 'Ax:Bragg}')
    _default_prefix = 'XF:31IDA-OP:1{Mono:DCM-'
    _default_read_attrs = ['MONO_Energy', 'MONO_Bragg']

# Instantiate Monochromator
MONO = Monochromator(name='MONO')
