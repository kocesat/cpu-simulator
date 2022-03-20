import json

class MemoryBus:

    def __init__(self, initial_data: list):
        self.memory = {}
        self.__load_initial_memory(initial_data)

    def __load_initial_memory(self, initial_data: list):
        for row in initial_data:
            row_spliited = row.split(',', maxsplit=2)
            self.memory[row_spliited[0]] = row_spliited[1]

    def get_from_memory(self, address):
        return self.memory.get(address)

    def write(self, address, value):
        self.memory[address] = value

    def dump_memory(self):
        print('Dumping memory...')
        print(json.dumps(self.memory, indent=4))
