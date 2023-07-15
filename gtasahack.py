from pymem.process import *
from pymem import *
processo = pymem.Pymem('gta-sa.exe')
gameModule = module_from_name(processo.process_handle, 'gta-sa.exe').lpBaseOfDll


def GetPtrAddr(base, offsets):
    endereço = processo.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            endereço = processo.read_int(endereço + offset)
    return endereço + offsets[-1]


def red(text):
    text_red = f'\033[31m{text}\033[m'
    return text_red


def text_with_line(text, linesnumber):
    print('-' * linesnumber)
    print(text)
    print('-' * linesnumber)


print('Digite "hack" para ver todos os hacks.')
while True:
    terminal = str(input('> '))
    if terminal == 'hack':
        text_with_line('|Jogador |', 10)
        text_with_line('|Teleport|', 10)
    elif terminal == 'Jogador':
        text_with_line('|Vida    |', 10)
        text_with_line('|Músculo |', 10)
        text_with_line('|Dinheiro|', 10)
        modificar_jogador = str(input('O que você gostaria de modificar do jogador ? '))
        if modificar_jogador == 'Vida':
            valor_da_vida = float(input('Qual valor você quer ter de vida ? '))
            processo.write_float(GetPtrAddr(gameModule + 0x07FC7D8, [0x540]), valor_da_vida)
        elif modificar_jogador == 'Dinheiro':
            valor_de_dinheiro = int(input('Qual valor você quer ter de dinheiro ? '))
            processo.write_int(gameModule + 0x810188, valor_de_dinheiro)
        elif modificar_jogador == 'Músculo':
            valor_de_músculo = float(input('Qual valor de músculo você quer ter ? '))
            processo.write_float(gameModule + 0x80C604, valor_de_músculo)
        elif modificar_jogador != 'Vida' and 'Músculo' and 'Dinheiro':
            print(red(f'{modificar_jogador} não é conhecido como um comando. Tente novamente.'))
    elif terminal == 'Teleport':
        text_with_line('|Grove Sreet     |', 18)
        text_with_line('|Academia        |', 18)
        text_with_line('|Loja de Roupas 1|', 18)
        text_with_line('|Loja de Roupas 2|', 18)
        local_de_teleport = str(input('Para qual local você quer se teleportar ? '))
        if local_de_teleport == 'Grove Street':
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x280]), -1661.451782)
            processo.write_float(GetPtrAddr(gameModule + 0x0080A11C, [0x14, 0xA0, 0x48, 0x14, 0x4C, 0x6C8]), 13.33623123)
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x27C]), 2473.178711)
        elif local_de_teleport == 'Academia':
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x280]), -1721.690796)
            processo.write_float(GetPtrAddr(gameModule + 0x0080A11C, [0x14, 0xA0, 0x48, 0x14, 0x4C, 0x6C8]), 13.56528854)
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x27C]), 2229.4646)
        elif local_de_teleport == 'Loja de Roupas 1':
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x280]), -1664.809082)
            processo.write_float(GetPtrAddr(gameModule + 0x0080A11C, [0x14, 0xA0, 0x48, 0x14, 0x4C, 0x6C8]), 15.4765625)
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x27C]), 2244.577637)
        elif local_de_teleport == 'Loja de Roupas 2':
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x280]), -1212.26709)
            processo.write_float(GetPtrAddr(gameModule + 0x0080A11C, [0x14, 0xA0, 0x48, 0x14, 0x4C, 0x6C8]), 23.96405411)
            processo.write_float(GetPtrAddr(gameModule + 0x00801748, [0x27C]), 2112.671143)
        elif local_de_teleport != 'Grove Street' and 'Academia' and 'Loja de Roupas 1' and 'Loja de Roupas 2':
            print(red(f'{local_de_teleport} não é conhecido como um comando. Tente novamente.'))
    elif terminal != 'hack' and 'Jogador' and 'Teleport':
        print(red(f'{terminal} não é conhecido como um comando. Tente novamente.'))
