import pandas as pd
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Baca data dari file CSV
df = pd.read_csv('Cleaned_Laptop_data.csv')

@app.route('/')
def index():
    # Script untuk menggambar grafik
    top10 = df.nlargest(10, 'ratings')
    plt.figure(figsize=(10, 6))
    plt.bar(top10['brand'], top10['ratings'], color='green', alpha=0.6)
    plt.ylabel('Ratings', fontsize=10)
    plt.xlabel("Brand", fontsize=10)
    plt.title("10 Brand Laptop Dengan Rating Tertinggi", fontsize=14)

    # Konversi grafik menjadi format gambar
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Konversi format gambar menjadi format yang dapat ditampilkan di HTML
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Render template HTML dengan gambar grafik
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
