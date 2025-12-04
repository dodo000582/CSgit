# [Radix Sort - Python]
## 1. 프로젝트 소개
 자료구조 시간에 배운 raidx sort를 C로 구현하는 과제가 있었는데, 이를 파이선으로도 한번 구현하며 공부해보고 싶었습니다.
## 2. 사용된 기술
 -digit(): 문자열 → 숫자한 총합을 변환 (a=1 ~ z=26)  
 -radix_sort(): 연결 리스트 기반 버킷 정렬 수행  
 -print_link(): 정렬된 문자열 출력
## 3. 대표 출력 예시(실행 결과)
 테스트 문자열: zero apple dog catalog zebra app bat banana car do   
 정렬한 문자열: app apple banana bat car catalog do dog zebra zero
```bash
python radix_sort.py
