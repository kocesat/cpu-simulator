# Cpu simulator main function
# Python 3.10 is used
# @Author: Esat Koç
from cpu import CPU

INSTRUCTION_FILE = 'instruction_input.txt'
DATA_FILE = 'data_input.txt'

def fetch_instructions() -> list:
    """
    Get instructions from file
    :return: a list of instructions
    """
    print("---------- Fetching all instructions --------------")
    with open(INSTRUCTION_FILE, 'r') as file:
        instructions = file.readlines()
        instructions = list(map(lambda s: s.strip(), instructions))
    return instructions

def fetch_data() -> list:
    """
    Get data from input file
    :return: a list of data
    """
    print("---------- Fetching all initial data --------------")
    with open(DATA_FILE, 'r') as file:
        data = file.readlines()
        data = list(map(lambda row: row.strip(), data))
    return data

def send_instruction_to_cpu(cpu: CPU):
    """
    Send all instructions fetched from data and send to cpu
    :return: None
    """
    instructions = fetch_instructions()
    print("---------- Sending all instructions to the cpu --------------")
    for instruction in instructions:
        cpu.decode_instruction(instruction)

def main():
    cpu = CPU(initial_data=fetch_data())
    send_instruction_to_cpu(cpu)


if __name__ == '__main__':
    main()