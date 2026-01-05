import pandas as pd

def generate_suggestions(data):
    df = pd.DataFrame(data)

    suggestions = []

    for _, row in df.iterrows():
        reason = []

        if row["age"] >= 18 and not row["mobile_linked"]:
            reason.append("Link mobile number")

        if row["address_changed"]:
            reason.append("Update address")

        suggestions.append({
            "aadhaar_number": row["aadhaar_number"],
            "suggestions": reason if reason else ["No update required"]
        })

    return suggestions
