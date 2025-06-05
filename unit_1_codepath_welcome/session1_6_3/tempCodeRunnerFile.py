def calculate_tip1(bill,service_quality):
    rates = {"poor":0.1,"average":0.15,"excellent":0.2}
    for rate in rates:
        if rate == service_quality:
            return bill * rate.get()
  