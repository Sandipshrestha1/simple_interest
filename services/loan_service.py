def calculate_simple_interest(principal, rate, time):

    interest = (principal * rate * time) / 100
    total = principal + interest

    return interest, total