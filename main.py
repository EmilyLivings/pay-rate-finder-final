from flask import Flask, render_template, request

app = Flask(__name__)

# Full pay data
pay_data = {
    ("EBO Rep", "Charlotte, NC"): "$16-$18/hr",
    ("EBO Rep", "Sartell, MN"): "$17-$19/hr",
    ("EBO Rep", "Waco, TX"): "$15-$17/hr",
    ("EBO Rep", "Moline, IL"): "$17-$19/hr",
    ("EBO Rep", "Brea, CA"): "$18-$20/hr",
    ("EBO Rep", "Cleveland, OH"): "$16-$17",
    ("Insurance Rep", "Remote"): "$18-$21/hr",
    ("Bad Debt Rep", "Brea, CA"): "$16.50 - $18/hr",
    ("Digital Response Team Rep", "Remote"): "$17-$20/hr",
    ("Legal Collector", "Indianapolis, IN"): "$12/hr",
    ("Bad Debt Rep", "Des Plaines, IL"): "$15-$16/hr",
    ("Bad Debt Rep", "Indianapolis, IN"): "$15-$16/hr",
    ("Bad Debt Rep", "Sartell, MN"): "$15-$16/hr",
    ("Bad Debt Rep", "Waco, TX"): "$15-$16/hr",
    ("Legal Clerk", "Indianapolis, IN"): "$18/hr",
    ("Legal Assistant", "Indianapolis, IN"): "$18/hr",
    ("Medicaid Eligibility Rep", "Gaithersburg, MD"): "$19-$23/hr",
    ("Medicaid Eligibility Rep", "Atlanta, GA"): "$19-$23/hr",
    ("Medicaid Eligibility Rep", "Cincinnati, OH"): "$18-$20",
    ("Medicaid Eligibility Rep", "Dover, NH"): "$20-$22/hr",
    ("Medicaid Eligibility Rep", "Hagerstown, MD"): "$18-$20",
    ("Medicaid Eligibility Rep", "Washington, PA"): "$18-$20",
}

@app.route('/', methods=["GET", "POST"])
def index():
    selected_position = None
    selected_location = None
    pay_rate = None

    if request.method == "POST":
        selected_position = request.form["position"]
        selected_location = request.form["location"]
        key = (selected_position, selected_location)
        pay_rate = pay_data.get(key, "Pay rate not found.")

    return render_template(
        "index.html",
        positions=sorted(set(k[0] for k in pay_data.keys())),
        locations=sorted(set(k[1] for k in pay_data.keys())),
        pay_rate=pay_rate,
        selected_position=selected_position,
        selected_location=selected_location
    )

app.run(host='0.0.0.0', port=81)

