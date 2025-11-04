# 총 10개의 테스트 케이스
for test_case in range(1, 11):
    
    # 1. N과 비밀번호 문자열을 입력받음 (N은 사용하지 않음)
    N, pw_str = input().split()
    
    # 2. 스택으로 사용할 빈 리스트
    stack = []
    
    # 3. 비밀번호 문자열의 각 문자를 순회
    for char in pw_str:
        
        # 4. (조건 1) 스택이 비어있지 않고, 
        #    스택의 top과 현재 문자가 같다면
        if stack and stack[-1] == char:
            # 중복이므로 pop
            stack.pop()
        else:
        # 5. (조건 2) 스택이 비어있거나, top과 문자가 다르면
            # 스택에 push
            stack.append(char)
            
    # 6. 스택에 남은 문자들을 하나의 문자열로 합침
    result = "".join(stack)
    
    # 7. 형식에 맞춰 출력
    print(f"#{test_case} {result}")