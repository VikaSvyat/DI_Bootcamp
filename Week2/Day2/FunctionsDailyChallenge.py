MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''
i = j = 0 #index of row and column
martrix_code = []
row =[]
for char in MATRIX_STR.strip():
    if char != '\n':
        row.append(char)
    else:
        martrix_code.append(row)
        row = []
if row: #last row that wasn't add
    martrix_code.append(row)
# martrix_code = [list(row) for row in MATRIX_STR.strip().splitlines()]
print(martrix_code)

message_coded = " "

max_cols = max(len(row) for row in martrix_code)

for col in range(max_cols):
    for row in martrix_code:
        # print(f"row={row},col={col}")
        if col < len(row):#
            if row[col].isalpha():
                message_coded += row[col]
            elif message_coded[-1] != " ":
                message_coded += ' '
                

print(message_coded.strip())
# for char in message_coded:
#     print(f"char = {char}, code = {ord(char)}")
   
