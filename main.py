from vshaurme import create_app
from vshaurme.extensions import db
from dotenv import load_dotenv

load_dotenv()
app = create_app()
db.create_all(app=app)
app.run(port='5000', host='0.0.0.0')
