f = open('9_of_hearts.png', 'rb')
data = f.read()
f.close()

f = open('9_of_hearts_fixed.png', 'wb')
file_len = len(data)
for i in range(0, file_len, 2 ):
	if i+2 < file_len:
		tuple_str = data[i:i+2]
		f.write(tuple_str[1])
		f.write(tuple_str[0])
	else:
		f.write(data[i])
f.close()