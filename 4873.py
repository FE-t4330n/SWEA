# 1. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    # 2. 문자열을 입력받습니다.
    s = input()
    
    # 3. 스택으로 사용할 빈 리스트를 생성
    stack = []
    
    # 4. 문자열의 각 문자를 순회
    for char in s:
        
        # 5. (조건 1)
        #    스택이 비어있지 않고(if stack)
        #    스택의 top과 현재 문자가 같다면(stack[-1] == char)
        if stack and stack[-1] == char:
            # 반복 문자를 만났으므로 스택에서 제거(pop)
            stack.pop()
        else:
        # 6. (조건 2)
        #    스택이 비어있거나, top과 문자가 다르면
            # 스택에 추가(push)
            stack.append(char)
            
    # 7. 순회가 끝난 후, 스택에 남은 문자의 개수를 출력
    result_length = len(stack)
    
    print(f"#{test_case} {result_length}")