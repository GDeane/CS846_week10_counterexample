def parse_payment(line):
    parts = line.strip().split(",")

    if len(parts) < 4:
        raise ValueError("Malformed payment row")

    payment_id = parts[0]
    amount = float(parts[1])
    tax = float(parts[2])
    discount = float(parts[3])

    return {
        "id": payment_id,
        "amount": amount,
        "tax": tax,
        "discount": discount
    }


def validate_payment(payment):
    if payment["amount"] < 0:
        raise ValueError("Negative amount")

    if payment["tax"] < 0:
        raise ValueError("Negative tax")

    if payment["discount"] < 0 or payment["discount"] > 100:
        raise ValueError("Invalid discount")

    return True


def calculate_subtotal(payment):
    subtotal = payment["amount"] + payment["tax"]
    return subtotal


def apply_discount(subtotal, discount):
    return subtotal - (subtotal * discount / 100)


def calculate_total(payment):
    subtotal = calculate_subtotal(payment)
    total = apply_discount(subtotal, payment["discount"])
    return total


def process_payments(file_path):
    results = []

    with open(file_path) as f:
        for line in f:
            if not line.strip():
                continue

            payment = parse_payment(line)
            validate_payment(payment)
            total = calculate_total(payment)
            results.append(total)

    return results
