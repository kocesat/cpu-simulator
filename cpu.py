from cache import Cache
from memorybus import MemoryBus
from enum import Enum


class InstructionType(Enum):
    ADD = 'ADD',
    ADDI = 'ADDI'
    SUB = 'SUB'
    SLT = 'SLT'
    BNE = 'BNE'
    J = 'J'
    JAL = 'JAL'
    LW = 'LW'
    SW = 'SW'
    CACHE = 'CACHE'
    HALT = 'HALT'

    @classmethod
    def get_enum_from_val(cls, enum_val):
        return cls[enum_val]


class CPU:
    """
    CPU class
    """
    def __init__(self, initial_data: list):
        print('CPU Simulator initializing...')
        self.cache = Cache()
        self.memory = MemoryBus(initial_data)
        print('*** Initialization successfull ***')
        print('*** CPU Simulator is ready to take instructions ***')

    def decode_instruction(self, instruction: str):
        instruction_type = InstructionType.get_enum_from_val(instruction.split(',')[0])
        match instruction_type:
            case InstructionType.ADD:
                self.__parse_and_call_add_instruction(instruction)
            case InstructionType.ADDI:
                self.__parse_and_call_addi_instruction(instruction)
            case InstructionType.J:
                self.__parse_and_call_j_instruction(instruction)
            case InstructionType.HALT:
                self.__halt_instruction()
            # TODO: Cover all cases

    def __parse_and_call_add_instruction(self, instruction: str) -> None:
        add_instruction = instruction.split(',', maxsplit=4)
        first_arg_source = add_instruction[1]
        second_arg_source = add_instruction[2]
        destination_source = add_instruction[3]
        self.__add_instruction(first_arg_source, second_arg_source, destination_source)

    def __parse_and_call_addi_instruction(self, instruction: str) -> None:
        addi_instruction = instruction.split(',', maxsplit=4)
        arg_source = addi_instruction[1]
        destination_source = addi_instruction[2]
        immediate = addi_instruction[3]
        self.__addi_instruction(arg_source, immediate, destination_source)

    def __parse_and_call_j_instruction(self, instruction: str) -> None:
        out_instruction = instruction.split(',', maxsplit=2)
        source = out_instruction[1]
        self.__j_instruction(source)

    def __j_instruction(self, where_to_jump):
        # j execution
        pass

    def __add_instruction(self, first_arg_source, second_arg_source, destination_source):
        # add execution
        first_arg = int(self.memory.get_from_memory(first_arg_source))
        second_arg = int(self.memory.get_from_memory(second_arg_source))
        self.memory.write(destination_source, first_arg + second_arg)

    def __addi_instruction(self, arg_source, immediate, destination_source):
        # addi execution
        pass

    def __halt_instruction(self):
        self.memory.dump_memory()
        print('*** Cpu is halting... ***')
