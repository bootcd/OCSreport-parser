from htmlgenerator import createPage
from generators import *

import xml.etree.cElementTree as ET

tree = ET.parse("12.xml")
root = tree.getroot()

netparams = {'speed': 'SPEED', 'ipaddress': 'IPADDRESS', 'macaddrres': 'MACADDR'}
cpuparams = {'cpuname': 'TYPE', 'freq': 'SPEED', 'corenumber': 'CORES', 'socket': 'SOCKET', 'arch': 'CPUARCH'}
ramparams = {'type': 'TYPE', 'freq': 'SPEED', 'size': 'CAPACITY'}
storeparams = {'name': 'NAME', 'size': 'DISKSIZE', 'type': 'TYPE'}
videoparams = {'name': 'NAME'}
softparams = {'name': 'NAME'}
searchwords = {'office': 'Office', 'AV': 'Антивирус'}
monitorparams = {'name': 'CAPTION'}
osparams = {'name': 'OSNAME', 'servicepack': 'OSCOMMENTS', 'arch': 'ARCH'}


def getparams(item, params_dict_template):
    for item_list in root.findall("CONTENT"):
        item_tags = item_list.findall(item)
    params_dict = params_dict_template
    for param in params_dict:
        obj_param_list = []
        for item_tag in item_tags:
            obj_param_list.append(item_tag.find(params_dict[param]))
        text_param_list = []
        for item in obj_param_list:
            text_param_list.append(item.text)
            params_dict[param] = text_param_list
    return params_dict


def getOtherParams(key):
    params_dict={}
    for item_list in root.findall("CONTENT"):
        item_tags = item_list.findall("SOFTWARES")
        text_param_list = []
        for item_tag in item_tags:
            software_obj_param = item_tag.find(softparams['name'])
            if searchwords[key] in software_obj_param.text:
                text_param_list.append(software_obj_param.text)
            params_dict['name'] = text_param_list
    return params_dict



raw_ram_dict = getparams("MEMORIES", ramparams)
raw_cpu_dict = getparams("CPUS", cpuparams)
raw_storages_dict = getparams("STORAGES", storeparams)
video_dict = getparams("VIDEOS", videoparams)
networks_dict = getparams("NETWORKS", netparams)
office_dict = getOtherParams('office')
avir_dict = getOtherParams('AV')
monitor_dict = getparams("MONITORS", monitorparams)
osparams_dict = getparams("HARDWARE", osparams)

cpu_dict = cpu_dict_generator(raw_cpu_dict)
ram_dict = ram_dict_generator(raw_ram_dict)
storage_dict = storage_dict_generator(raw_storages_dict)


print(raw_storages_dict)
# print(ram_dict_generator(raw_ram_dict))
# print(cpu_dict_generator(raw_cpu_dict))
print(storage_dict_generator(raw_storages_dict))




createPage("PC_Summary", cpu_dict, ram_dict, storage_dict)





