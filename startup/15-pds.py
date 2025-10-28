
from ophyd import Component as Cpt  # type: ignore[import-not-found]
from ophyd import Device, EpicsMotor, PseudoPositioner, PseudoSingle, Signal
from ophyd import DynamicDeviceComponent as DDC
from ophyd.pseudopos import pseudo_position_argument, real_position_argument

import numpy as np


# TODO evict to cditools
class Energy(PseudoPositioner):
    bragg = Cpt(EpicsMotor, "Mono:HDCM-Ax:Bragg}Mtr")
    cgap = Cpt(EpicsMotor, "Mono:HDCM-Ax:HG}Mtr")
    # Synthetic Axis
    energy = Cpt(PseudoSingle, egu="KeV")

    #Energy "limits"
    _low = 5.0 #TODO: CHECK THIS VALUE
    _high = 15.0 #TODO: CHECK THIS VALUE

    # Set up constants
    Xoffset = 20.0  # mm
    d_111 = 3.1286911960950756
    ANG_OVER_KEV = 12.3984


    def energy_to_positions(self, target_energy: float):
        """Compute undulator and mono positions given a target energy

        Parameters
        ----------
        target_energy : float
            Target energy in keV

        Returns
        -------
        bragg : float
            The angle to set the monocromotor in radians
        gap : float
            The gap position in millimeters
        """

        # Calculate Bragg RBV
        bragg = (
            np.arcsin((self.ANG_OVER_KEV / target_energy) / (2 * self.d_111))
        )

        # Calculate C2X
        gap = self.Xoffset / 2 / np.cos(bragg)

        return bragg, gap
    
    @pseudo_position_argument
    def forward(self, p_pos):
        energy = p_pos.energy # energy assumed in keV
        bragg, gap = self.energy_to_positions(energy)
        return self.RealPosition(bragg=np.rad2deg(bragg), cgap=gap)
    
    @real_position_argument
    def inverse(self, r_pos):
        bragg = np.deg2rad(r_pos.bragg)
        e = self.ANG_OVER_KEV / (
            2 * self.d_111 * np.sin(bragg)
        )
        return self.PseudoPosition(energy=float(e))
    
class DCMBase(Device):
    h = Cpt(EpicsMotor, "Mono:HDCM-Ax:TX}Mtr")
    v = Cpt(EpicsMotor, "Mono:HDCM-Ax:TY}Mtr")
    c2 = DDC(
        {
            "p": (EpicsMotor, "Mono:HDCM-Ax:Pitch}Mtr", {}),
            "r": (EpicsMotor, "Mono:HDCM-Ax:Roll}Mtr", {}),
            "fp": (EpicsMotor, "Mono:HDCM-Ax:FP}Mtr", {}),
        }
    )

dcm_base = DCMBase(prefix="XF:09IDA-OP:1{", name="dcm_base", labels=["motors", "dcm"])

energy = Energy(prefix="XF:09IDA-OP:1{", name="energy", labels=["dcm"])