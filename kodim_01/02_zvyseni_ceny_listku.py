number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100} %")

print(f"Celková cena nákupu je {total_price} Kč.")
print(f"Zaokrouhlená cena je: {round(total_price)} Kč")