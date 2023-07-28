# Função para calcular o endereço de rede
def gera_endereco_rede(end_ip, mask):
    ip_binario = ''
    ip_octetos = end_ip.split('.') # tira os pontos do ip e deixa em um lsta

    # converte o ip para binario, e usa a funcao zfill para deixar os octetos com 32 bits
    for i in ip_octetos:
        ip_binario += bin(int(i))[2:].rjust(8, "0")

    # calcula a mascara do ip
    ip_binario = ip_binario[:mask] + '0' * (32 - mask)

    #return ip_decimal
    return int(f'0b{ip_binario}',2)

# Função para calcular o endereço de broadcast
def gera_endereco_broadcast(ip, mask):
    #calcula a mascara
    mascara = '1' * mask

    # ljust ira colocar os 0 a direita ate 32 bits para deixar o ip valido
    mascara = mascara.ljust(32, "0")

    mak8 = list()
    # uma lista o ip da mascara separando em octetos

    for i in range(0, 32, 8) :
        mak8.append(int(mascara[i: i+8]))

  #separando o ip em octetos
    ip8 = [int(i) for i in ip.split('.')]

    #endereco de broadcast ip ou (nao mask) (nega a mascara)
    #calcula o broadcast
    broadcast = list() #[192, 24, 246, 255]
    for i in range(4):
        numero = (256 + (ip8[int(i)] | (~int(f'0b{mak8[int(i)]}', 2))))
        broadcast.append(numero)

    broadcast_bin = ''
    for i in broadcast:
        broadcast_bin += bin(i)[2:].rjust(8, "0") # deixa em binario e n pega a parte do '0b' e deixa com 8 bits
    # return broadcast
    return int(broadcast_bin, 2)

# Função para gerar todos os endereços IP possíveis de serem utilizados em hosts na sub-rede.
def hosts_addr(ip, mask):
    end_rede = gera_endereco_rede(ip,mask) # obter o endereco de rede
    end_broadcast = gera_endereco_broadcast(ip,mask) # obter o endereco de broadcast

    for i in range(end_rede, end_broadcast): # pega o i do for transforma pra bin cm 32 bits, dps separa 4 octetos, dai pra int, e dai da yeld
        end_bin = str(bin(i)[2:]).rjust(8, "0")
        end_bin = end_bin.ljust(32, "0") # deixa o ip com 32 bits

        list_end_bin = [str(int(end_bin[i:i+8], 2)) for i in range(0, 32, 8)] # o ip binario vira uma lista, ex: de '11000000101010001111011000000000' para ['192', '255', '255', '254']

        aux = '.'.join(list_end_bin) # separar o ip por '.' e junta tudo em uma string, ex: 192.255.255.254

        yield aux

ip="192.168.10.10" # endereco de ip
mascara = 18 # mascara de rede

for ip in hosts_addr(ip, mascara):
    print(ip)
