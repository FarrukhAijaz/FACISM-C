from lxml import etree
import xmltodict
import os

import chardet

# Detect file encoding
xml_file = "/home/saijaz/Downloads/Test1.xml"

with open(xml_file, "rb") as f:  # Read as binary
    raw_data = f.read()

# Detect encoding
encoding_detected = chardet.detect(raw_data)["encoding"]
print(f"Detected Encoding: {encoding_detected}")

# Open file with detected encoding
with open(xml_file, "r", encoding=encoding_detected) as file:
    xml_content = file.read()

print("File loaded successfully!")


# Convert XML to dictionary for easier processing
xmi_dict = xmltodict.parse(xml_content)

# Navigate through the XMI structure
uml_model = xmi_dict["xmi:XMI"]["uml:Model"]

# Extract components
components = []
for elem in uml_model.get("packagedElement", []):
    if "@xmi:type" in elem and elem["@xmi:type"] == "uml:Component":
        components.append({
            "name": elem["@name"],
            "id": elem["@xmi:id"]
        })

# Extract dependencies
dependencies = []
for elem in uml_model.get("packagedElement", []):
    if "@xmi:type" in elem and elem["@xmi:type"] == "uml:Dependency":
        dependencies.append({
            "client": elem["@client"],
            "supplier": elem["@supplier"]
        })

# Print extracted data
print("Components:", components)
print("Dependencies:", dependencies)
