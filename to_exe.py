import struct
from to_asm import to_asm
# pack expected 18 items for packing (got 19)

def parse_asm(asm_filename):
    with open(asm_filename, 'r') as file:
        lines = file.readlines()

    instructions = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith(';') or line.startswith('.'):
            continue
        parts = line.split()
        instructions.append(parts)

    return instructions


def assemble(instructions):
    # Define a simple instruction to machine code mapping
    instruction_set = {
        'movl': b'\xb8',   # Move to EAX
        'addl': b'\x01',   # Add
        'subl': b'\x29',   # Subtract
        'call': b'\xe8',   # Call
        'ret': b'\xc3',    # Return
        'pushq': b'\x50',  # Push to stack
        'popq': b'\x58',   # Pop from stack
        'leave': b'\xc9',  # Leave
        'cltq': b'\x98',   # Convert long to quad
        'cmp': b'\x3d',    # Compare
        'jmp': b'\xe9',    # Jump
        'jle': b'\x7e',    # Jump if less or equal
        'jg': b'\x7f',     # Jump if greater
        'movb': b'\xb0',   # Move byte to AL
        'movq': b'\x48\xb8'  # Move to RAX
    }

    machine_code = b''

    for instr in instructions:
        op = instr[0]
        if op in instruction_set:
            machine_code += instruction_set[op]
            if len(instr) > 1:
                operands = instr[1].split(',')
                for operand in operands:
                    if operand.startswith('$'):
                        # Immediate value
                        machine_code += struct.pack('<I', int(operand[1:]))
                    elif operand.startswith('%'):
                        if operand == '%eax':
                            machine_code += b'\x00'
                        elif operand == '%ebx':
                            machine_code += b'\x03'
                        elif operand == '%ecx':
                            machine_code += b'\x01'
                        elif operand == '%edx':
                            machine_code += b'\x02'
                        elif operand == '%rbp':
                            machine_code += b'\x45'
                        elif operand == '%rsp':
                            machine_code += b'\x54'

    return machine_code


def create_executable(machine_code, exe_filename):
    # DOS header
    dos_header = struct.pack(
        '<2sHHLHHHHHHHHHH8sHH20sL',
        b'MZ',        # Magic number
        0x0090,      # Bytes on last page of file
        0x0003,      # Pages in file
        0x0000,      # Relocations
        0x0004,      # Size of header in paragraphs
        0x0000,      # Minimum extra paragraphs needed
        0xFFFF,      # Maximum extra paragraphs needed
        0x0000,      # Initial (relative) SS value
        0x00B8,      # Initial SP value
        0x0000,      # Checksum
        0x0000,      # Initial IP value
        0x0000,      # Initial (relative) CS value
        0x0040,      # File address of relocation table
        0x0000,      # Overlay number
        b'\x00' * 8,  # Reserved words
        0x0000,      # OEM identifier (for e_oeminfo)
        0x0000,      # OEM information; e_oemid specific
        b'\x00' * 20,  # Reserved words
        0x00000080   # File address of new exe header
    )

    # PE header
    pe_header = (
        b'PE\0\0'                # PE Signature
        b'\x4C\x01'              # Machine (x86)
        b'\x01\x00'              # Number of sections
        b'\x00\x00\x00\x00'      # TimeDateStamp
        b'\x00\x00\x00\x00'      # Pointer to symbol table
        b'\x00\x00\x00\x00'      # Number of symbols
        b'\xE0\x00'              # Size of optional header
        b'\x02\x01'              # Characteristics
    )

    # Optional header
    optional_header = (
        b'\x0B\x01'              # Magic (PE32)
        b'\x01\x00'              # MajorLinkerVersion
        b'\x00\x00'              # MinorLinkerVersion
        b'\x00\x10\x00\x00'      # SizeOfCode
        b'\x00\x00\x00\x00'      # SizeOfInitializedData
        b'\x00\x00\x00\x00'      # SizeOfUninitializedData
        b'\x00\x10\x00\x00'      # AddressOfEntryPoint
        b'\x00\x10\x00\x00'      # BaseOfCode
        b'\x00\x00\x00\x00'      # BaseOfData
        b'\x00\x00\x40\x00'      # ImageBase
        b'\x00\x10\x00\x00'      # SectionAlignment
        b'\x00\x10\x00\x00'      # FileAlignment
        b'\x04\x00'              # MajorOperatingSystemVersion
        b'\x00\x00'              # MinorOperatingSystemVersion
        b'\x00\x00'              # MajorImageVersion
        b'\x00\x00'              # MinorImageVersion
        b'\x00\x00'              # MajorSubsystemVersion
        b'\x00\x00'              # MinorSubsystemVersion
        b'\x00\x00\x00\x00'      # Win32VersionValue
        b'\x00\x10\x00\x00'      # SizeOfImage
        b'\x00\x20\x00\x00'      # SizeOfHeaders
        b'\x00\x00\x00\x00'      # CheckSum
        b'\x02\x00'              # Subsystem (Windows GUI)
        b'\x00\x00'              # DllCharacteristics
    )

    # Section header
    section_header = (
        b'.text\x00\x00\x00'     # Section name
        b'\x00\x10\x00\x00'      # Virtual size
        b'\x00\x10\x00\x00'      # Virtual address
        b'\x00\x10\x00\x00'      # Size of raw data
        b'\x00\x20\x00\x00'      # Pointer to raw data
        b'\x00\x00\x00\x00'      # Pointer to relocations
        b'\x00\x00\x00\x00'      # Pointer to line numbers
        b'\x00\x00\x00\x00'      # Number of relocations
        b'\x00\x00\x00\x00'      # Number of line numbers
        b'\x60\x00\x00\x20'      # Characteristics
    )

    headers = dos_header + pe_header + optional_header + section_header

    # Align the machine code to the file alignment
    while len(machine_code) % 0x200 != 0:
        machine_code += b'\x00'

    with open(exe_filename, 'wb') as file:
        file.write(headers + machine_code)

    print(f"Successfully created {exe_filename}")


def to_exe(filename):
    """
    解析汇编文件: parse_asm 函数读取汇编文件并解析指令。
    汇编指令到机器码: assemble 函数将指令转换为机器码。指令集映射扩展了更多的指令。
    创建可执行文件: create_executable 函数生成包含 DOS 头、PE 头、可选头和节头的 PE 文件格式，并将机器码写入其中。
    """
    # to_asm(filename)
    asm_filename = filename[:-1] + "s" 
    exe_filename = filename[:-1] + "exe"
    instructions = parse_asm(asm_filename)
    machine_code = assemble(instructions)
    create_executable(machine_code, exe_filename)

if __name__ == "__main__":
    to_exe("./test/test.c")
