# stationxml1.0-1.1-converter
Convert FDSN StationXML 1.0 to FDSN StationXML 1.1

### Usage
###### As script
```shell script
# Individual file
python xslt_converter.py StationXML-1.0to1.1.xslt path/to/inputStation.xml path/to/output/directory/

# Directory
python xslt_converter.py StationXML-1.0to1.1.xslt path/to/input/ path/to/output/directory/

# Wildcard matching glob syntax
python xslt_converter.py StationXML-1.0to1.1.xslt path/to/IU.*.xml path/to/output/directory/

```

###### As library
```python
from lxml import etree
from stationxml.xslt_converter import convert_single_file, convert_from_paths

xslt_file = 'StationXML-1.0to1.1.xslt'
with open(xslt_file, 'r') as f:
    xslt_parsed = etree.parse(f)
    transform = etree.XSLT(xslt_parsed)

# Test single file
input_file = 'test/xslt/source/C0/C0_Q24A.xml'
output_path = 'test/xslt/result/C0/'
convert_single_file(transform=transform, input_file_path=input_file, output_dir=output_path)

# Test entire directory
input_path = 'test/xslt/source/GS/GS_A*'
output_path = 'test/xslt/result/GS/'
convert_from_paths(xslt=xslt_file, input=input_path, output=output_path)
print('Done')
```