from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the input field
        input_data = request.form.get('input_field')

        # Process the data and generate the table data
        table_data = [
            {
                'property1': 'Product A',
                'property2': '$49.99',
                'property3': 'In Stock',
                'property4': '4.5 out of 5',
                'property5': '125 reviews'
            },
            {
                'property1': 'Product B',
                'property2': '$79.99',
                'property3': 'Out of Stock',
                'property4': '4.2 out of 5',
                'property5': '89 reviews'
            },
            {
                'property1': 'Product C',
                'property2': '$29.99',
                'property3': 'In Stock',
                'property4': '3.8 out of 5',
                'property5': '42 reviews'
            },
            {
                'property1': 'Product D',
                'property2': '$99.99',
                'property3': 'In Stock',
                'property4': '4.7 out of 5',
                'property5': '201 reviews'
            },
            {
                'property1': input_data,
                'property2': '$59.99',
                'property3': 'In Stock',
                'property4': '4.1 out of 5',
                'property5': '78 reviews'
            }
        ]

        return render_template('index.html', table_data=table_data)
    else:
        return render_template('index.html', table_data=None)


if __name__ == '__main__':
    app.run(debug=True)
