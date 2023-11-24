from dotenv import load_dotenv, dotenv_values
from sqlalchemy import create_engine, text
load_dotenv()

env_variables = dotenv_values('.env')


db_username = env_variables.get('CORE_STEAMPIPE_DATABASE_USERNAME') or "steampipe"
db_password = env_variables.get('CORE_STEAMPIPE_DATABASE_PASSWORD') or "admin"
db_host = env_variables.get('CORE_STEAMPIPE_DATABASE_HOSTNAME') or "localhost"
db_name = env_variables.get('CORE_STEAMPIPE_DATABASE_NAME') or "steampipe"
db_port = env_variables.get('CORE_STEAMPIPE_PORT') or "9193"



class SteampipeDatabase:
    def __init__(self):
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
        self.db_port = db_port
        self.engine = self.init_engine()
        self.connection = self.engine.connect()

    def init_engine(self):
        # Create the database URL
        db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(db_url)
        return engine
    

# def connect_steampipe_database():
#     # Create the database URL
#     db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
#     engine = create_engine(db_url)
#     connection = engine.connect()
#     return engine

# # Create the database URL
# db_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"


# engine = create_engine(db_url)

# connection = engine.connect()

