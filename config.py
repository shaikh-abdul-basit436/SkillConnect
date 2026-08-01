class Config:
    SECRET_KEY = "skillconnect_secret_key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:7762@localhost/skillconnect"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False