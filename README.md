
# 📦 택배 주소 분류기 프로젝트

이 프로젝트는 **주소 데이터를 불러와 시/도 단위로 분류**하고,  
각 지역별로 택배 건수를 집계하는 간단한 파이썬 실습 예제입니다.

프로그래밍 입문자가 **문자열 처리**, **반복문**, **딕셔너리**, **함수 분리**, **모듈 구조**를 자연스럽게 익힐 수 있도록 구성되어 있습니다.

---

## 📁 프로젝트 폴더 구조

```
parcel_sorter/
├── data/                     # 주소 데이터 폴더
│   └── addresses.txt         # 샘플 주소 데이터
├── output/                   # 실행 결과 저장 폴더
├── data_loader.py            # 주소 파일 불러오기 함수
├── sorter.py                 # 시/도 추출 및 분류 함수
├── utils.py                  # (선택) 결과 저장 함수
├── main.py                   # 전체 실행 파일
├── test_data_loader.py       # 모듈 단위 테스트 스크립트
├── test_sorter.py            # 모듈 단위 테스트 스크립트
└── README.md                 # 프로젝트 설명 문서
```

---

## 🧾 샘플 주소 데이터 (`data/addresses.txt`)

```
서울특별시 강남구 역삼동 123-45
경기도 수원시 영통구 원천동 98
부산광역시 해운대구 우동 101
서울특별시 마포구 상암동 55
대구광역시 수성구 범어동 77
경기도 고양시 일산서구 탄현동 22
```

---

## ▶️ 실행 방법

1. Python 3.x 설치 필요
2. `main.py` 실행

```bash
python main.py
```

### 💡 실행 결과 (예시)

```
[1] 주소 데이터 불러오는 중...
[2] 지역별 택배 건수 분류 중...
[3] 결과 출력:
- 서울특별시: 2건
- 경기도: 2건
- 부산광역시: 1건
- 대구광역시: 1건
```

3. 실행 후 결과는 `output/sorted_result.txt`에도 저장됩니다.

---

## 🧪 테스트 파일 안내

본 프로젝트에는 간단한 **모듈별 단위 테스트용 파일**이 포함되어 있습니다:

| 파일명 | 설명 |
|--------|------|
| `test_data_loader.py` | 주소 파일을 불러오는 `load_addresses()` 함수 테스트 |
| `test_sorter.py` | 주소 리스트를 지역별로 분류하는 `count_by_region()` 함수 테스트 |

이 파일들은 공식 `unittest` 프레임워크는 아니지만,  
**초보자용 단위 테스트 흐름 학습용**으로 활용할 수 있도록 구성되었습니다.

---

## 🧠 학습 포인트

| 항목 | 설명 |
|------|------|
| 파일 입출력 | `with open()`, 파일 경로 이해 |
| 문자열 처리 | `split()`, `strip()` 사용 |
| 자료구조 | `list`, `dict` |
| 반복문 & 조건문 | `for`, `if`, `not in` 등 |
| 함수 분리 | 역할별 함수 정의 및 재사용 |
| 모듈 구조 | 파일별 기능 분리 및 `import` |
| main 함수 구조 | 실행 흐름 제어의 기본 익히기 |
| 테스트 스크립트 | 직접 테스트하며 로직 검증하기 |

---

## 📌 확장 아이디어

- '서울특별시' → '서울'처럼 이름 정제 기능 추가
- 동/읍/면 단위로도 분류해보기
- CSV 파일로 결과 저장
- 웹 페이지에서 업로드한 주소 파일 처리하기 (Flask 등)
- 실제 택배 데이터 연동 (API, DB 활용 등)

---

## 🙋‍♀️ 만든 사람

**두산 ROKEY BOOT CAMP**  
프로그래밍이 처음인 분들도 "나도 프로젝트 만들 수 있다!"는 경험을 할 수 있도록 설계된 입문용 자료입니다 😊

© 2025 Doosan ROKEY Bootcamp 
본 프로젝트는 교육 목적을 위해 제작되었습니다.  
비영리 목적의 학습 및 참고는 자유롭게 가능하며,  
상업적 이용 또는 2차 배포 시 반드시 두산 ROKEY BOOT CAMP의 사전 동의를 받아야 합니다.