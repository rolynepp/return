# fuction 

#fuction 是用來收納程式碼的
#他是個功能

def wash(dry=False, water=8): #定義函式名稱  dry在這裡為參數
	print('加水', water, '分滿')
	print('旋轉')
	if dry:
		print('烘衣')
wash()  #執行


#利用fuction 可以增加程式碼的重複使用性

def say_hi():
	print('hi')

# say_hi

def add(x=0, y=0):
	return x + y

result = add(3, 4) #沒設定的時候都是投給X 
print(result)

def average(numbers):

	avg = sum(numbers) / len (numbers)
	return avg

a = average([1, 2, 3])

print(a)
print(average([23, 32, 6]))
print(average([180, 35, 92]))