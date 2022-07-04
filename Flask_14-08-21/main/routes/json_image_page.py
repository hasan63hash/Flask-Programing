from main import app
from main.models import Image
import json

@app.route("/images/<int:id>")
def json_image_page(id):
    try:
        image = Image.query.filter_by(id=id).first()

        if image is None:
            return "Bu id'ye sahip bir resim yok"

        jsonstr = json.dumps(image.as_dict())
        return jsonstr
    except:
        return "Hata"
