import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:

    def __init__(self, filepath):
        self.data = dict()

        with open(filepath, mode='r') as f:
            self.data = json.load(f)
        
    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


# Factory method 
def data_extraction_factory(filepath):
    
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


if __name__ == "__main__":
    
    json_data = extract_data_from("./movies.json")
    print(json_data.parsed_data)

    xml_tree = extract_data_from("./person.xml")
    print(xml_tree.parsed_data)

