def solution(arr, intervals):
    answer = []


    # extend: 기존 리스트 객체에 요소 추가 (메모리 효율적)
    # += : 새로운 리스트 객체 생성 후 할당 (추가 메모리 사용)
    for start, end in intervals:
        answer.extend(arr[start:end+1])
    
    return answer
