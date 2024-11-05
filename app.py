from flask import Flask, send_file
from flask_cors import CORS  # Import CORS
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/chart2')
def generate_chart():
    labels = ['Sent mail to registered', 'Paid for register']
    sizes = [120, 85]
    colors = ['#140C73', '#3A96C9']
    plt.style.use('ggplot')
    plt.title("Students' activation")
    plt.pie(sizes, labels=labels, autopct='%.2f%%', startangle=90, colors=colors)
    plt.axis('equal')
    circle = plt.Circle((0, 0), 0.75, color='white')
    plt.gca().add_artist(circle)
    img = BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
