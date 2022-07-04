from waitress import serve
from main import app

host = "192.168.2.206"
port = 80

from main.routes import home_page, json_image_page, json_image_ids_page

if __name__ == "__main__":
    serve(app, host=host, port=port)
    #app.run(host=host, port=port, debug=True)