import xml.etree.ElementTree as ET


class Xmlable:
    def to_xml(self):
        root = ET.Element(self.__class__.__name__)
        for k, v in self.__dict__.items():
            k = ET.SubElement(root, k)
            k.text = str(v)
        return ET.tostring(root).decode('utf8')

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)
        data = {}
        for child in root:
            data[child.tag] = child.text

        return cls(**data)
