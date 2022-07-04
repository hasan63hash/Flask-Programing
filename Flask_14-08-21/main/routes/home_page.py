from flask import render_template
from main import app
from main.models import Image
import datetime
import os

@app.route('/')
def index():
   images = Image.query.all()
   img_dict = {}

   # Resimleri tarih keylerine göre sözlüğe doldur
   for image in images:
      date = image.entry_date
      if date in img_dict:
         date_list = img_dict[date]
         date_list.append(image)
      else:
         img_dict[date] = [image]

   # Tarih listesini al
   dates = img_dict.keys()

   # Tarihleri yeniden eskiye sırala
   dates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'), reverse=True)

   return render_template("index.html", img_dict=img_dict, sorted_dates=dates)