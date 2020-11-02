credit_scrore = False
house_rate = 10000


def downpayment():
    if credit_scrore == True:
        rate = 10/100*house_rate
        print(rate)
    else:
        print("Dowpayment of this customer is")
        rate = 20/100*house_rate
        print(rate)


downpayment()
