
def classify_merchant(description):

    description = str(description).lower().strip()

    essential_keywords = [
        "grocery", "groceries", "supermarket",
        "medicine", "medical", "pharmacy",
        "electricity", "eb bill", "tneb",
        "tax", "gst", "recharge",
        "metro", "bus", "train",
        "public transport"
    ]

    discretionary_keywords = [
        "restaurant", "swiggy", "zomato",
        "movie", "cinema", "entertainment",
        "gaming", "netflix", "spotify",
        "shopping", "cafe", "tea shop"
    ]

    if any(word in description for word in essential_keywords):
        return "Essential"

    if any(word in description for word in discretionary_keywords):
        return "Discretionary"

    return "Needs Review"
