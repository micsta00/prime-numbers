import sys

primary_numbers_arr = [2]
min = int(input("Primary numbers from: "))
max = int(input("to: "))

if min<=max and min>=0:
    start_arr = list(range (2,max))
else:
    print("Wrong scope")
    sys.exit(0)

def check_if_div_by(num, arr):
  z=0
  for x in arr:
    if num == 1 or num == x or num % x == 0:
      z+=1
  if z>0:
    pass
  else:
    arr.append(num)

for i in start_arr:
  check_if_div_by(i, primary_numbers_arr)

def clean_arr(arr_to_clean, min):
  clean_list=[]
  for x in arr_to_clean:
    if x >= min:
      clean_list.append(x)
  return clean_list

clean_list = clean_arr(primary_numbers_arr, min)
print(f'Primary numbers in scope {min} - {max}: {clean_list}')