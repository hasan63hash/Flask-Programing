from main import app
from main.models import Image
import json

@app.route("/images/ids")
def json_image_ids_page():
    ids = [id_tuple[0] for id_tuple in Image.query.with_entities(Image.id).order_by(Image.id.desc()).all()]
    jsonstr = json.dumps(ids)
    return jsonstr