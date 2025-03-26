from data_loader import load_addresses
from sorter import count_by_region

file_path = 'data/addresses.txt'
addresses = load_addresses(file_path)
region_counts = count_by_region(addresses)

print("지역별 택배 건수:")
for region, count in region_counts.items():
    print(f"{region}: {count}건")
