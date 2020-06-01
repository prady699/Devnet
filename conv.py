import xmltodict
import json
import yaml

with open('sample.json') as file:
    temp=file.read()
json_file=json.loads(temp)
file.close()

yaml_file=yaml.safe_dump(json_file)
with open('smaple.yaml','w+') as file:
    file.write(yaml_file)
file.close()

xml_file=xmltodict.unparse((json_file))
with open('sample.xml','w+') as file:
    file.write(xml_file)
file.close()