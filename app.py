from flask import Flask
from main import main
from datetime import timedelta
import config
from exts import db
from models import Share

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
app.config.from_object(config)
app.register_blueprint(main)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=8080)
