from data_loader import load_addresses
# data_loader.py의 테스트 코드 부분과 동일
file_path = 'data/addresses.txt'
addresses = load_addresses(file_path)

print("불러온 주소 목록:")
for addr in addresses:
    print("-", addr)
