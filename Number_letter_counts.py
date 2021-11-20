# Create 2 dictionaries
units={1:'one',
          2:'two',
          3:'three',
          4:'four',
          5:'five',
          6:'six',
          7:'seven',
          8:'eight',
          9:'nine',
          10:'ten',
          11:'eleven',
          12:'twelve',
          13:'thirteen',
          14:'fourteen',
          15:'fifteen',
          16:'sixteen',
          17:'seventeen',
          18:'eighteen',
          19:'nineteen'}

tens={2:'twenty',
         3:'thirty',
         4:'fourty',
         5:'fifty',
         6:'sixty',
         7:'seventy',
         8:'eighty',
         9:'ninety'}

def two_numbers(num):
  '''This function transform the numbers from 1 to 99 into text

  Arguments: num. A number between 1 and 99
  Return : string of the name of the number 
  ''' 
  global units, tens
  if num <=19:
    letters=units[num]
  elif (num>19 & num<100):
    num=str(num)
    # Split the number into two positions
    # Pos_2 corresponds with tens and pos_1 with units
    pos_2, pos_1 = int(num[-2]), int(num[-1])
    if pos_2 in tens.keys():
      pos_2 = tens[pos_2]
    if pos_1 in units.keys():
      pos_1 = units[pos_1]
    else:
      pos_1 =""
    # Concatenate two parts
    letters = pos_2 + pos_1
  return letters

tot_letters = len('onethousand')
for num in range(1,1000):
  # Transform num to string to count numbers 
  num = str(num)
  if len(num)==3:
    num = str(num)
    pos_3, pos_2, pos_1 = int(num[-3]), int(num[-2]), int(num[-1])
    if (pos_1==0 & pos_2==0):
      letters=units[pos_3]+'hundred'
    else:
      # Call to two_numbers function
      letters = two_numbers(int(num[1:]))
      letters = units[pos_3]+'hundredand' + cadena
  elif len(num)==2:
      letters = two_numbers(int(num))
  elif int(num)<=19:
    num = int(num)
    letters=units[num]
  tot_letters = tot_letters + len(letters)
print(f'For write the name of the numbers from 1 to 1000 you need {tot_letters} letters')
