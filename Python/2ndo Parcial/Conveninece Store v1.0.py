print('welcome to Walmart cashier')
name=(input('Assistant Name:'))
item1=(input('adress item 1:'))
price1=int(input('address price 1:'))
print(item1, '$',price1)
item2=(input('adress item 2:'))
price2=int(input('address price 2:'))
print(item2, '$',price2)
item3=(input('adress item 3:'))
price3=int(input('address price 3:'))
print(item3, '$',price3)
item4=(input('adress item 4:'))
price4=int(input('address price 4:'))
print(item4, '$',price4)
item5=(input('adress item 5:'))
price5=int(input('address price 5:'))
print(item5, '$',price5)

print('ticket')
print('assisted by:',name)
print('items:')
print(item1, '$',price1)
print(item2, '$',price2)
print(item3, '$',price3)
print(item4, '$',price4)
print(item5, '$',price5)
suma=(price1+price2+price3+price4+price5)
print('subtotal:',suma)
taxes=(suma*0.16)
print('taxes:', taxes)
print('total to pay:', suma*1.16)
