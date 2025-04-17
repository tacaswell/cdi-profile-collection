#!/usr/bin/env python
import pandas as pd

# Create sample data for the Excel file
data = [
    {
        'Component Name': 'Sample Stage',
        'Component ID': 'SAMPLE',
        'Full component name': 'XF:31IDA-OP:1{Stg:',
        'Full axis name': 'XF:31IDA-OP:1{Stg:X}',
        'Axis ID': 'X',
        'IOC Name': 'ioc-op-sample'
    },
    {
        'Component Name': 'Sample Stage',
        'Component ID': 'SAMPLE',
        'Full component name': 'XF:31IDA-OP:1{Stg:',
        'Full axis name': 'XF:31IDA-OP:1{Stg:Y}',
        'Axis ID': 'Y',
        'IOC Name': 'ioc-op-sample'
    },
    {
        'Component Name': 'Sample Stage',
        'Component ID': 'SAMPLE',
        'Full component name': 'XF:31IDA-OP:1{Stg:',
        'Full axis name': 'XF:31IDA-OP:1{Stg:Z}',
        'Axis ID': 'Z',
        'IOC Name': 'ioc-op-sample'
    },
    {
        'Component Name': 'KB Mirrors',
        'Component ID': 'KB',
        'Full component name': 'XF:31IDA-OP:1{Mir:KB-',
        'Full axis name': 'XF:31IDA-OP:1{Mir:KB-Ax:VFM}',
        'Axis ID': 'VFM',
        'IOC Name': 'ioc-op-mirrors'
    },
    {
        'Component Name': 'KB Mirrors',
        'Component ID': 'KB',
        'Full component name': 'XF:31IDA-OP:1{Mir:KB-',
        'Full axis name': 'XF:31IDA-OP:1{Mir:KB-Ax:HFM}',
        'Axis ID': 'HFM',
        'IOC Name': 'ioc-op-mirrors'
    },
    {
        'Component Name': 'Monochromator',
        'Component ID': 'MONO',
        'Full component name': 'XF:31IDA-OP:1{Mono:DCM-',
        'Full axis name': 'XF:31IDA-OP:1{Mono:DCM-Ax:Energy}',
        'Axis ID': 'Energy',
        'IOC Name': 'ioc-op-mono'
    },
    {
        'Component Name': 'Monochromator',
        'Component ID': 'MONO',
        'Full component name': 'XF:31IDA-OP:1{Mono:DCM-',
        'Full axis name': 'XF:31IDA-OP:1{Mono:DCM-Ax:Bragg}',
        'Axis ID': 'Bragg',
        'IOC Name': 'ioc-op-mono'
    },
    # Integer Component ID - this should be skipped
    {
        'Component Name': 'Integer ID Component',
        'Component ID': '123',
        'Full component name': 'XF:31IDA-OP:1{Int:',
        'Full axis name': 'XF:31IDA-OP:1{Int:Motor}',
        'Axis ID': 'Motor',
        'IOC Name': 'ioc-op-integer'
    },
    # Add another integer ID
    {
        'Component Name': 'Another Integer',
        'Component ID': 456,  # Numeric without quotes
        'Full component name': 'XF:31IDA-OP:1{NumID:',
        'Full axis name': 'XF:31IDA-OP:1{NumID:Test}',
        'Axis ID': 'Test',
        'IOC Name': 'ioc-op-integer'
    },
    # Add MC component that should be skipped
    {
        'Component Name': 'MC',
        'Component ID': 'MCDEVICE',
        'Full component name': 'XF:31IDA-OP:1{MC:',
        'Full axis name': 'XF:31IDA-OP:1{MC:Motor}',
        'Axis ID': 'Motor',
        'IOC Name': 'ioc-op-mc'
    },
    # Add another MC component
    {
        'Component Name': 'MC',
        'Component ID': 'MC2',
        'Full component name': 'XF:31IDA-OP:1{MC:',
        'Full axis name': 'XF:31IDA-OP:1{MC:Other}',
        'Axis ID': 'Other',
        'IOC Name': 'ioc-op-mc'
    },
    # Add some empty rows and incomplete data to test filtering
    {
        'Component Name': '',
        'Component ID': '',
        'Full component name': '',
        'Full axis name': '',
        'Axis ID': '',
        'IOC Name': ''
    },
    {
        'Component Name': 'Incomplete',
        'Component ID': 'INC',
        'Full component name': '',
        'Full axis name': '',
        'Axis ID': '',
        'IOC Name': ''
    }
]

# Create DataFrame
df = pd.DataFrame(data)

# Add some extra columns that we don't care about
df['Extra Column 1'] = 'Not important'
df['Extra Column 2'] = 123

# Make sure sheet name matches what the parser expects
excel_file = 'example_components.xlsx'
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Motion axis summary', index=False)

print(f"Created example Excel file: {excel_file}")
print("You can now run the parser with:")
print(f"python parse_excel.py {excel_file}") 