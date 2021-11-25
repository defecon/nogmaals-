# name of student: Timo Sneijder
# number of student: 99067236
# function of program: wisselgeld toegeven met munten

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
if paid < toPay:
    print(f"Je hebt niet alles betaald. U moet nog {toPay-paid} centen bijbetalen")
    exit()
else:
    print("Je krijgt wisselgeld")

change = paid - toPay #

nrcvalue200 = 0
nrcvalue100 = 0
nrcvalue50 = 0
nrcvalue20 = 0
nrcvalue10 = 0
nrcvalue5 = 0
nrcvalue2 = 0
nrcvalue1 = 0


coinValue = 200 #

if change > 0: #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
        nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? ')) #


        change -= nrCoinsReturned * coinValue #

    if coinValue == 200:
      CoinValue200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      CoinValue100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      CoinValue50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      CoinValue20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      CoinValue10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      CoinValue5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      CoinValue2 = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      CoinValue1 = nrCoinsReturned
      coinValue = 0

if change > 0:
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')


print("""----------------------------------""")
print(f'2 euro munten terug gegeven:    {CoinValue200}')
print(f'1 euro munten terug gegeven:    {CoinValue100}')
print(f'50 cent munten terug gegeven:   {CoinValue50}')
print(f'20 cent munten terug gegeven:   {CoinValue20}')
print(f'10 cent munten terug gegeven:   {CoinValue10}')
print(f'5 cent munten terug gegeven:    {CoinValue5}')
print(f'2 cent munten terug gegeven:    {CoinValue2}')
print(f'1 cent munten terug gegeven:    {CoinValue1}')
print("""----------------------------------""")