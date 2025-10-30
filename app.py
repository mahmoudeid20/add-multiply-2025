from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-key"

def parse_number(value):
    if not value.strip():
        return False, "This field cannot be empty."
    try:
        return True, float(value.replace(",", "."))
    except ValueError:
        return False, "Invalid number format."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    a_input = b_input = ""
    if request.method == 'POST':
        a_input = request.form.get('a', '').strip()
        b_input = request.form.get('b', '').strip()
        ok_a, val_a = parse_number(a_input)
        ok_b, val_b = parse_number(b_input)
        if not ok_a:
            flash(f"Error in A: {val_a}")
        if not ok_b:
            flash(f"Error in B: {val_b}")
        if ok_a and ok_b:
            result = {'a': val_a, 'b': val_b, 'sum': val_a + val_b, 'product': val_a * val_b}
    return render_template('index.html', result=result, a_input=a_input, b_input=b_input)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
