import xml.etree.ElementTree as ET
import yaml

def xml_to_yaml(xml_file, yaml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def xml_to_dict(element):
        d = {}
        for key, value in element.attrib.items():
            d[key] = value
        for child in element:
            child_dict = xml_to_dict(child)
            if child.tag in d:
                if type(d[child.tag]) is list:
                    d[child.tag].append(child_dict)
                else:
                    d[child.tag] = [d[child.tag], child_dict]
            else:
                d[child.tag] = child_dict
        if element.text and element.text.strip():
            d["#text"] = element.text.strip()
        return d

    data = {root.tag: xml_to_dict(root)}

    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

# 사용 예시
xml_to_yaml("P1025_07.xml", "P1025_07.yaml")