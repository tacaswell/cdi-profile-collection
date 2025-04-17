#!/usr/bin/env python
from ophyd import Device, Component as Cpt, EpicsMotor

# Auto-generated Ophyd device classes

class SampleStageSAMPLE(Device):
    """Ophyd Device for Sample Stage SAMPLE"""
    SAMPLE_X = Cpt(EpicsMotor, 'X}')
    SAMPLE_Y = Cpt(EpicsMotor, 'Y}')
    SAMPLE_Z = Cpt(EpicsMotor, 'Z}')
    _default_prefix = 'XF:31IDA-OP:1{Stg:'
    _default_read_attrs = ['SAMPLE_X', 'SAMPLE_Y', 'SAMPLE_Z']

# Instantiate Sample Stage
SAMPLE = SampleStageSAMPLE(name='SAMPLE')

class KBMirrorsKB(Device):
    """Ophyd Device for KB Mirrors KB"""
    KB_VFM = Cpt(EpicsMotor, 'Ax:VFM}')
    KB_HFM = Cpt(EpicsMotor, 'Ax:HFM}')
    _default_prefix = 'XF:31IDA-OP:1{Mir:KB-'
    _default_read_attrs = ['KB_VFM', 'KB_HFM']

# Instantiate KB Mirrors
KB = KBMirrorsKB(name='KB')

class MonochromatorMONO(Device):
    """Ophyd Device for Monochromator MONO"""
    MONO_Energy = Cpt(EpicsMotor, 'Ax:Energy}')
    MONO_Bragg = Cpt(EpicsMotor, 'Ax:Bragg}')
    _default_prefix = 'XF:31IDA-OP:1{Mono:DCM-'
    _default_read_attrs = ['MONO_Energy', 'MONO_Bragg']

# Instantiate Monochromator
MONO = MonochromatorMONO(name='MONO')

class IntegerIDComponent123(Device):
    """Ophyd Device for Integer ID Component 123"""
    123_Motor = Cpt(EpicsMotor, 'Motor}')
    _default_prefix = 'XF:31IDA-OP:1{Int:'
    _default_read_attrs = ['123_Motor']

# Instantiate Integer ID Component
123 = IntegerIDComponent123(name='123')

class AnotherInteger456(Device):
    """Ophyd Device for Another Integer 456"""
    456_Test = Cpt(EpicsMotor, 'Test}')
    _default_prefix = 'XF:31IDA-OP:1{NumID:'
    _default_read_attrs = ['456_Test']

# Instantiate Another Integer
456 = AnotherInteger456(name='456')
