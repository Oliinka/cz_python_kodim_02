flight_number = input("Zadejte číslo letu: ").upper()
prefix = flight_number[0] + flight_number[1]
if prefix == "BA":
    company = "British Airways"
elif prefix == "LH":
    company = "Lufthansa"
else:
    company = "Neznámá společnost"
print(f"Letíte se společností {company}")

