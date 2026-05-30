total_cost = float(input("Enter your total cost: "))
selling_price = float(input("Enter your selling price: "))
if total_cost == selling_price:
  print("No profit, no loss")
elif selling_price > total_cost:
  profit = selling_price-total_cost
  profit_percentage = profit*100/total_cost
  print(f"Profit: {profit} Rs and profit percentage: {profit_percentage}%")
else:
  loss = total_cost - selling_price
  loss_percentage = loss*100/total_cost
  print(f"Loss: {loss} Rs and loss percentage: {loss_percentage}%")