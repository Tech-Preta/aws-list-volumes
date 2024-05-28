import boto3
import json

# Cria um cliente para o serviço EC2
ec2_client = boto3.client('ec2')

# Lista todos os volumes
response = ec2_client.describe_volumes()
volumes = response['Volumes']

output = []  # Inicializa a lista para armazenar a saída
total_size = 0  # Inicializa a variável para armazenar o tamanho total

for volume in volumes:
    volume_info = {
        'ID': volume['VolumeId'],
        'Tamanho': f"{volume['Size']} GB",
        'Tipo': volume['VolumeType'],
        'Zona de disponibilidade': volume['AvailabilityZone'],
        'Estado': volume['State']
    }
    output.append(volume_info)
    total_size += volume['Size']  # Acumula o tamanho de cada volume

# Lista todos os snapshots
response = ec2_client.describe_snapshots()
snapshots = response['Snapshots']

for snapshot in snapshots:
    snapshot_info = {
        'ID': snapshot['SnapshotId'],
        'Volume ID': snapshot['VolumeId'],
        'Tamanho': f"{snapshot['VolumeSize']} GB",
        'Estado': snapshot['State'],
        'Data de início': str(snapshot['StartTime'])
    }
    output.append(snapshot_info)
    total_size += snapshot['VolumeSize']  # Acumula o tamanho de cada snapshot

# Adiciona o total de volumes, snapshots e o tamanho total à saída
output.append({
    'Total de volumes': len(volumes),
    'Total de snapshots': len(snapshots),
    'Tamanho total': f"{total_size} GB"
})

# Escreve a saída em um arquivo .json
with open('output.json', 'w') as f:
    json.dump(output, f)

# Ou se você quiser escrever em um arquivo .txt
with open('output.txt', 'w') as f:
    f.write(json.dumps(output))