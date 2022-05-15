deposit_sum = float(input())
months = int(input())
interest = float(input())
percent_interest = interest*0.01
total_sum = deposit_sum + months*((deposit_sum*percent_interest)/12)
print(total_sum)