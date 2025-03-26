from data_loader import load_addresses
from sorter import count_by_region
from utils import save_result

def main():
    file_path = 'data/addresses.txt'
    print("[1] 주소 데이터 불러오는 중...")
    addresses = load_addresses(file_path)

    if not addresses:
        print("[!] 주소 데이터가 없습니다.")
        return

    print("[2] 지역별 택배 건수 분류 중...")
    region_counts = count_by_region(addresses)

    print("[3] 결과 출력:")
    for region, count in region_counts.items():
        print(f"- {region}: {count}건")

    # 결과 파일 저장
    save_result(region_counts, 'output/sorted_result.txt')

if __name__ == "__main__":
    main()