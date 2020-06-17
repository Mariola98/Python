# przykładowa aplikacja zakupu owoców

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}


def compute_bill(food):
  total=0
  for i in food:
    if stock[i]>0:
      
      total=total+prices[i]
      stock[i]-=1
  return total

p=compute_bill(shopping_list)
print (p)
print (stock)

input("wciśnij Enter")
