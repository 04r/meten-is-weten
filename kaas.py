goed = input("Is de kaas geel?")

if goed == "ja": 
    gaten = input("Zitten er gaten in?")
    if gaten == "nee":
        hard = input("Is de kaas hard als steen?")
        if hard == "nee":
            print("Jouw kaas is Goudse kaas")
        if hard == "ja":
            print("Jouw kaas is Parmigiano Reggiano")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur?")
        if duur == "ja":
            print("Jouw kaas is emmenthaler.")

elif goed == "nee": 
    schimmels = input("Heeft de kaas blauwe schimmels?")
    if schimmels == "nee":
        korst2 = input("Heeft de kaas een korst?")
        if korst2 == "nee":
            print("Jouw kaas is Mozzarella")
        if korst2 == "ja":
            print("Jouw kaas is Camambert")
    if schimmels == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print("Jouw kaas is Bleu de Rochbaron")
