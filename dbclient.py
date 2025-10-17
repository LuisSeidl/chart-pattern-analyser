from datetime import datetime, timedelta, date
from sqlalchemy import create_engine, select, and_, update, delete, desc, func, text
from sqlalchemy.orm import sessionmaker, joinedload


class DatabaseClient:

    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)

    def test_connection(self):
        """Returns True if it is able to connect to the Database, False if not"""
        with self.Session() as session:
            try:
                session.execute(text('SELECT 1'))
                print('\n\n----------- Connection successful !')
                return True
            
            except Exception as e:
                print('\n\n----------- Connection failed ! ERROR : ', e)
                return False


    def merge_instances(self, instances: list):
        """Inserts or updates the given fixtures in the database
        Uses SQLAlchemy merge(), which will insert if not found, or update if exists, based on the primary key"""

        with self.Session() as session:
            try:
                for instance in instances:
                    session.merge(instance)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                print(f"Finished updating instances: {instance}")

    def merge_one_by_one(self, instances: list):
        """Inserts or updates the given instances in the database """

        with self.Session() as session:
            try:
                for instance in instances:
                    session.merge(instance)
                    session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                print(f"Finished updating instances: {instance}")