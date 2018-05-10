def ram_dict_generator(raw_ram_dict):
    ram_dict={}
    slots_number = len(raw_ram_dict['type'])
    ram_dict['slots_number'] = slots_number
    ram_dict['size_in_slot'] = raw_ram_dict['size']

    ram_size_summary = 0
    for element in raw_ram_dict['size']:
        ram_size_summary = ram_size_summary + int(element)
    ram_dict['ram_size_summary'] = ram_size_summary

    ram_dict['type'] = []
    for element in raw_ram_dict['type']:
        if element != 'Empty slot':
            ram_dict['type'].append(element)
    ram_dict['type'] = ','.join(ram_dict['type'])

    ram_dict['freq'] = []
    for element in raw_ram_dict['freq']:
        if element != '0':
            ram_dict['freq'].append(element)
    ram_dict['freq'] = ','.join(ram_dict['freq'])
    return ram_dict


def cpu_dict_generator(raw_cpu_dict):
    cpu_dict = {}
    cpu_number = len(raw_cpu_dict["cpuname"])
    cpu_dict['name'] = []
    for element in raw_cpu_dict['cpuname']:
        cpu_dict['name'].append(element)

    cpu_dict['name'] = ','.join(cpu_dict['name'])
    cpu_dict['cpunumber'] = cpu_number
    cpu_dict['corenumber'] = ','.join(raw_cpu_dict['corenumber'])


    cpu_dict['cpusocket'] = []
    for element in raw_cpu_dict['socket']:
        cpu_dict['cpusocket'].append(element)
    cpu_dict['cpusocket'] = ', '.join(raw_cpu_dict['socket'])
    cpu_dict['cpuarch'] = ''.join(raw_cpu_dict['arch'][0])
    return cpu_dict

def storage_dict_generator(raw_storage_dict):
    storage_dict = {}
    for i in range(len(raw_storage_dict['name'])):
        storage_dict['device %d' % i] = []
        if 'Fixed hard disk media' in raw_storage_dict['type'][i]:
            storage_dict['device %d' % i].append(raw_storage_dict['name'][i])
            storage_dict['device %d' % i].append(raw_storage_dict['size'][i])
    return storage_dict