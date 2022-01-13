from app import create_app
from app import db
import os

app = create_app()

if __name__ == "__main__":
    #Fazendo db caso não tenha um
    if not os.path.exists('./app/app.db'):
        db.create_all(app=create_app())
    app.run(debug=True)