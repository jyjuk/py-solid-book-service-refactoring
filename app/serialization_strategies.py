import json
import xml.etree.ElementTree as ET
from app.interfaces import ISerializationStrategy


class JsonSerializer(ISerializationStrategy):
    def serialize(self, data: dict) -> str:
        return json.dumps(data)


class XmlSerializer(ISerializationStrategy):
    def serialize(self, data: dict) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = data.get("title", "")
        content = ET.SubElement(root, "content")
        content.text = data.get("content", "")
        return ET.tostring(root, encoding="unicode")
