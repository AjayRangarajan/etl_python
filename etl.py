import os
from dotenv import loadenv
from etlalchemy import ETLAlchemySource, ETLAlchemyTarget

loadenv()

SOURCE_DATABASE_URI = os.environ.get("SOURCE_DATABASE_URI")
DESTINATION_DATABASE_URI = os.environ.get("DESTINATION_DATABASE_URI")

source = ETLAlchemySource(SOURCE_DATABASE_URI)
target = ETLAlchemyTarget(DESTINATION_DATABASE_URI, drop_database=True)
target.addSource(source)
target.migrate()