from flask import Flask, send_file
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/chart2')
def generate_chart():
    # Data for the chart
    labels = ['Sent mail to registered', 'Paid for register']
    sizes = [120, 85]
    colors = ['#140C73', '#3A96C9']



    # Create the plot
    plt.style.use('ggplot')
    plt.title("Students' activation")
    plt.pie(x=sizes,labels=labels,autopct='%.2f%%',startangle=90,colors=colors)
    plt.axis('equal')
    plt.legend(loc='upper right')

    circle = plt.Circle(xy=(0,0),radius=.75, facecolor='white')
    plt.gca().add_artist(circle)
    plt.show()


    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)