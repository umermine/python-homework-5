temp = int(input("What is the temperature? "))
if temp <= 5:
    print("Clothing Type: Heavy layers.\nSuggestions:\nA warm coat.\nThick sweater or thermal top underneath.\nJeans or trousers with thermal leggings if necessary.\nScarf, gloves, and a hat.\nInsulated boots.")
elif temp <= 15:
    print("Clothing Type: Light layers.\nSuggestions:\nLight jacket or sweater (e.g., leather jacket).\nLong-sleeved shirt or T-shirt.\nJeans or pants.\nClosed-toe shoes or sneakers.")
elif temp <= 25:
    print("Clothing Type: Summer attire.\nSuggestions:\nT-shirts\nShorts or breathable trousers.\nLightweight fabrics like cotton or linen.\nSandals or sneakers.")
elif temp <= 35:
    print("Clothing Type: Very light and breathable clothing.\nSuggestions:\nSleeveless T-shirt.\nShorts or loose, breathable pants.\nOpen-toed shoes or sandals.\nLight colors to reflect sunlight.")
else:
    print("Temperature is outside the common range provided.")
