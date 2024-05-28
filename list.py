import boto3

# Cria um cliente para o serviço EC2
ec2_client = boto3.client('ec2')

# Lista todos os volumes
response = ec2_client.describe_volumes()
volumes = response['Volumes']

print("Volumes:")
total_size = 0  # Inicializa a variável para armazenar o tamanho total

for volume in volumes:
    print(f"\tID: {volume['VolumeId']}")
    print(f"\tTamanho: {volume['Size']} GB")
    print(f"\tTipo: {volume['VolumeType']}")
    print(f"\tZona de disponibilidade: {volume['AvailabilityZone']}")
    print(f"\tEstado: {volume['State']}")
    total_size += volume['Size']  # Acumula o tamanho de cada volume
    print()

# Imprime o tamanho total
print(f"Tamanho total de todos os volumes: {total_size} GB")

# Lista todos os snapshots
response = ec2_client.describe_snapshots()
snapshots = response['Snapshots']

print("Snapshots:")
for snapshot in snapshots:
    print(f"\tID: {snapshot['SnapshotId']}")
    print(f"\tVolume ID: {snapshot['VolumeId']}")
    print(f"\tTamanho: {snapshot['VolumeSize']} GB")
    print(f"\tEstado: {snapshot['State']}")
    print(f"\tData de início: {snapshot['StartTime']}")
    print()