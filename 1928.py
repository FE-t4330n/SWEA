def create_decoding_table():
    """ Base64 디코딩 테이블(딕셔너리)을 생성합니다. """
    # A-Z (0-25), a-z (26-51), 0-9 (52-61), + (62), / (63)
    table = {}
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i, char in enumerate(chars):
        table[char] = i
    return table

# 1. 디코딩 테이블을 미리 생성
DECODING_TABLE = create_decoding_table()

# 2. 테스트 케이스 개수 T를 입력받습니다.
T = int(input())

for test_case in range(1, T + 1):
    
    encoded_string = input()
    decoded_text = ""
    
    # 3. 4글자씩 묶어서 처리
    for i in range(0, len(encoded_string), 4):
        # 4글자 묶음을 가져옴 (예: 'TGlm')
        chunk = encoded_string[i : i+4]
        
        # 4. 4개의 문자를 6비트 정수 4개로 변환
        val1 = DECODING_TABLE[chunk[0]]
        val2 = DECODING_TABLE[chunk[1]]
        
        # 5. 6비트 정수 4개를 24비트 정수 1개로 합침
        # (val1 << 18) | (val2 << 12) | ...
        combined_24bit = (val1 << 18) | (val2 << 12)
        
        # 6. 24비트를 8비트 3개로 쪼개서 아스키코드로 변환
        
        # 첫 번째 8비트 (무조건 존재)
        # (24비트에서 상위 8비트를 가져옴)
        byte1 = (combined_24bit >> 16) & 0xFF  # 0xFF는 11111111 (8비트 마스크)
        decoded_text += chr(byte1)
        
        # 7. 패딩 '=' 처리
        if chunk[2] != '=':
            # 두 번째 8비트
            val3 = DECODING_TABLE[chunk[2]]
            combined_24bit |= (val3 << 6)
            
            byte2 = (combined_24bit >> 8) & 0xFF
            decoded_text += chr(byte2)
            
            if chunk[3] != '=':
                # 세 번째 8비트
                val4 = DECODING_TABLE[chunk[3]]
                combined_24bit |= val4
                
                byte3 = combined_24bit & 0xFF
                decoded_text += chr(byte3)

    # 8. 최종 결과 출력
    print(f"#{test_case} {decoded_text}")