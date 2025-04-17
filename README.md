# CDI Profile Collection

A collection of tools for generating Ophyd device classes for beamline control systems.

## Excel to Ophyd Device Generator

This tool converts information from an Excel spreadsheet into Ophyd Device classes for use in beamline control systems.

### Requirements

- Python 3.7+
- pandas
- ophyd

Install the required packages:

```bash
pip install pandas ophyd
```

### Usage

The `parse_excel.py` script reads component and axis information from an Excel file and generates Ophyd device classes.

```bash
python parse_excel.py path/to/your/excel_file.xlsx -o output_file.py
```

#### Arguments:

- `filename`: Path to the Excel file containing component information
- `-o, --output`: Optional. Output Python file (default: ophyd_devices.py)

### Excel File Format

The Excel file should contain these required columns:
- `Component Name` - The general type of the component
- `Component ID` - The unique identifier for the component
- `Full component name` - The full PV prefix for the component
- `Full axis name` - The full PV name for each motor axis
- `Axis ID` - The identifier for each motor axis
- `IOC Name` - The IOC name for the component

### Filtering Rules

The script applies the following filtering rules to rows in the Excel file:
- Rows with missing values in any required column are skipped
- Rows with `Component Name` equal to "MC" are skipped
- Rows where `Component ID` is an integer are skipped

### Generated Output

The script generates Ophyd Device classes according to these rules:
- A new Ophyd `Device` class for each distinct `Component Name`
- Class names are created by concatenating `Component Name` and `Component ID` (e.g., "SampleStageSAMPLE")
- Each class has one or many `EpicsMotor` components
- Motor PV prefixes are derived from `Full axis name` without the `Full component name` part
- `EpicsMotor` components are named "<Component ID>_<Axis ID>"
- `Device` instances are named "<Component ID>"

### Example

For an Excel file with these rows:

```
Component Name | Component ID | Full component name | Full axis name       | Axis ID
Sample Stage   | SAMPLE       | XF:31IDA-OP:1{Stg:  | XF:31IDA-OP:1{Stg:X} | X
Sample Stage   | SAMPLE       | XF:31IDA-OP:1{Stg:  | XF:31IDA-OP:1{Stg:Y} | Y
```

The generated code would be:

```python
from ophyd import Device, Component as Cpt, EpicsMotor

class SampleStageSAMPLE(Device):
    """Ophyd Device for Sample Stage SAMPLE"""
    SAMPLE_X = Cpt(EpicsMotor, 'X}')
    SAMPLE_Y = Cpt(EpicsMotor, 'Y}')
    _default_prefix = 'XF:31IDA-OP:1{Stg:'
    _default_read_attrs = ['SAMPLE_X', 'SAMPLE_Y']

# Instantiate Sample Stage
SAMPLE = SampleStageSAMPLE(name='SAMPLE')
```