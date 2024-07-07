A = int(input())
B = int(input())

B_units = B % 10
B_tens = (B // 10) % 10
B_hundreds = B // 100

result1 = A * B_units
result2 = A * B_tens
result3 = A * B_hundreds

result_final = A * B

# 결과 출력
print(result1)
print(result2)
print(result3)
print(result_final)
