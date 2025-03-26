def save_result(result_dict, file_path):
    """분류 결과를 텍스트 파일로 저장"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for region, count in result_dict.items():
                f.write(f"{region}: {count}건\n")
        print(f"[✔] 결과가 저장되었습니다: {file_path}")
    except Exception as e:
        print(f"[오류] 저장 실패: {e}")
