N = int(input("Nhập số phương án nghiên cứu: "))

matrix = [[0 for j in range(2)] for i in range(N)]

x = float(input("Nhập xác suất trường hợp tốt: "))
y = 1 - x 
# Nhập các giá trị của ma trận
for i in range (N):
    for j in range (2):
        matrix[i][j] = int(input())

EVM = []
for i in range(N):
    EVM.append(matrix[i][0]*x + matrix[i][1]*y)

MaxEVM = max(EVM)
print("EVM: ", end = "")
print(EVM)

OL = [[0 for j in range(2)] for i in range(N)]
maxOL = [-999999999]*2
for j in range(2):
    for i in range(N):
        if(matrix[i][j] > maxOL[j]):
            maxOL[j] = matrix[i][j]

for i in range(N):
    for j in range(2):
        OL[i][j] = maxOL[j] - matrix[i][j]

print("OL: ", end = "")
print(OL)

EOL = []

for i in range(N):
    EOL.append(OL[i][0]*x + OL[i][1]*y)

print("EOL: ",end = "")
print(EOL)