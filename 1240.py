# 1. 암호 코드표 (딕셔너리)
CODE_MAP = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

# 56비트 문자열을 8자리 숫자로 디코딩하는 함수
def decode_barcode(barcode):
    decoded_digits = []
    for i in range(8):
        # 7비트씩 자르기
        chunk = barcode[i*7 : (i+1)*7]
        
        if chunk in CODE_MAP:
            decoded_digits.append(CODE_MAP[chunk])
        else:
            # 코드표에 없는 조각이면, 유효하지 않은 바코드
            return None
    return decoded_digits

# --- 메인 로직 ---
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    grid = [input() for _ in range(N)]
    
    found_digits = None # 최종 8자리 숫자를 저장할 변수
    
    # 2. 암호 코드 탐색 (한 줄씩)
    for r in range(N):
        if found_digits: # 이미 찾았으면 중단
            break
            
        # 2-1. 오른쪽 끝부터 56칸씩 스캔
        for c in range(M - 1, 54, -1): # (M-1)부터 55까지
            
            # 2-2. 56비트 후보 추출
            barcode_candidate = grid[r][c - 55 : c + 1]
            
            # 2-3. 디코딩 시도
            decoded = decode_barcode(barcode_candidate)
            
            if decoded:
                # 2-4. 디코딩 성공 시 (8자리 모두 유효한 코드)
                found_digits = decoded
                break
                
    # 3. 유효성 검증 (Checksum)
    answer = 0
    if found_digits:
        d = found_digits
        
        odd_sum = d[0] + d[2] + d[4] + d[6]
        even_sum = d[1] + d[3] + d[5] + d[7]
        
        checksum = (odd_sum * 3) + even_sum
        
        # 4. 결과 계산
        if checksum % 10 == 0:
            answer = sum(d) # 유효하면 총합
        else:
            answer = 0 # 유효하지 않으면 0
            
    print(f"#{test_case} {answer}")