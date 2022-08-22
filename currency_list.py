import difflib


def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


currency_list = {"KZT": [0.0021, "tenge"], "RUB": [0.017, "ruble"], "USD": [1, "dollar"], "JPY": [0.0073, "yen"],
                 "CNY": [0.15, "yuan"], "GBP": [1.18, "pound"], "EUR": [1, "euro"], "TRL": [0.055, "lira"],
                 "FRF": [0.174, "frank"]}


def check_currency(expected_value):
    similar_key = ""
    similar_percent = 0
    for currency_k, currency_v in currency_list.items():
        if similar(expected_value, currency_v[1]) >= similar_percent and similar(expected_value, currency_v[1]) >= 0.7:
            similar_key = currency_k
            similar_percent = similar(expected_value, currency_v[1])

    if similar_key == "": return [None, None]
    return [similar_key, currency_list[similar_key]]
