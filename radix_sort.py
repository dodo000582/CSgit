# 2025005608 최명헌

def string_to_digit(word, idx):
    """문자열 word에서 idx번째 문자(a~z)를 숫자로 변환 (a=1 ~ z=26). 없으면 0."""
    if idx < len(word):
        return ord(word[idx]) - ord('a') + 1
    else:
        return 0


def print_link(words, link, first):#link에 저장된 순서대로 words에서 차례로 출력
    cur = first
    print("sorted words:\n[",end=" ")
    while cur != 0:
        print(words[cur], end=" ")
        cur = link[cur]
    print("]",end=" ")


def radix_sort(words, max_len, r, n):
    """문자열이 나열된 words, 최대 문자열 길이, 비교할 기수(radix) 개수, 총 문자 개수(n) 을 받음
    LSD radix sort방식으로, 가장 뒤의 알파벳부터 가장 앞의 알파벳까지 비교해나가며 정렬하고, 사전순으로 정렬된 문자열을 반환
    ex) dog<dogs 인것으로 간주"""

    front = [0] * r #각 알파벳bin에 저장된 첫번째 문자열 인덱스
    rear = [0] * r  #각 알파벳bin에 저장된 마지막 문자열 인덱스
    link = [0] * (n + 1) #연결리스트같은 방식으로, 문자열 순서를 저장, words[3] 다음 문자열이 words[5]라면 link[3]=5
    
    first = 1 #단어는 [1]부터 저장되있음
    for i in range(1, n):
        link[i] = i + 1
    link[n] = 0 # 초기 link 세팅 1->2를, 2->3, ... n->0으로 반복 끝

    # 알파벳을 뒤에서 앞으로(Lesat Significant Digit-LSD)
    for i in range(max_len - 1, -1, -1):

        # bin 초기화
        for b in range(r):
            front[b] = 0
            rear[b] = 0

        # link를 돌면서 bin에 분배
        cur = first
        while cur != 0:
            b = string_to_digit(words[cur], i)

            if front[b] == 0:
                front[b] = cur
            else:
                link[rear[b]] = cur

            rear[b] = cur
            cur = link[cur]
        
        # 첫 번째로 비어있지 않은 bin 찾기
        bin_idx = 0
        while bin_idx < r and front[bin_idx] == 0:
            bin_idx += 1
        first = front[bin_idx] # for i in range... 의 반복문에서 다음 반복을 위해 first저장

        last = rear[bin_idx]

        # 나머지 bin을 연결한 것을 link에 저장해두고, link로 연결해둔 가장 마지막 문자열은 0을 가리키도록
        for b in range(bin_idx + 1, r):
            if front[b] != 0:
                link[last] = front[b]
                last = rear[b]

        link[last] = 0

    print_link(words, link, first)


# 테스트 데이터
words = ["\0", "zero", "apple", "dog", "catalog", "zebra", "app", "bat", "banana", "car", "do"]
row = len(words)
try:
    max_length = max(len(w) for w in words[1:])  # 첫 번째 "\0" 제외 이후 단어 중 가장 긴 문자열 길이
    radix_sort(words, max_length, 27, row - 1) #단어, 최대 길이, 알파벳 개수+\0 개, 총 비교할 단어 수
except ValueError as e:
    print("empty words")
    print(e)
except Exception as e:    
    print('예외가 발생했습니다.', e)
