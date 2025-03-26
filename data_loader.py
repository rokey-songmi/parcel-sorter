def load_addresses(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            addresses = [line.strip() for line in f if line.strip()]
        return addresses
    except FileNotFoundError:
        print(f"[오류] 파일을 찾을 수 없습니다: {file_path}")
        return []

# 🔽 여기서부터는 테스트 코드
if __name__ == "__main__":
    file_path = 'data/addresses.txt'
    addresses = load_addresses(file_path)
    print("불러온 주소:")
    for addr in addresses:
        print("-", addr)
