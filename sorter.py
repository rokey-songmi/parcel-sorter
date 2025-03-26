def extract_region(address):
    parts = address.split()
    if len(parts) > 0:
        return parts[0]
    return "알 수 없음"

def count_by_region(address_list):
    region_count = {}
    for addr in address_list:
        region = extract_region(addr)
        if region not in region_count:
            region_count[region] = 0
        region_count[region] += 1
    return region_count

# 🔽 여기서부터는 테스트 코드
if __name__ == "__main__":
    sample_addresses = [
        "서울특별시 강남구 역삼동",
        "경기도 수원시 영통구",
        "부산광역시 해운대구",
        "서울특별시 마포구 상암동",
    ]

    result = count_by_region(sample_addresses)
    print("테스트 결과:")
    for region, count in result.items():
        print(f"{region}: {count}건")
