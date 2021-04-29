from application.data.abstract.base_database import BaseDatabase
from application.data.models.json_database import JsonDatabase

database: BaseDatabase = JsonDatabase()
