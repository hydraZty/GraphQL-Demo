from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://zhangtianyi@localhost:5432/graph_example', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Department, Employee, Role
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    one_app = Department(name='One App（人工智能）')
    db_session.add(one_app)
    tire = Department(name='TireO2O（卖轮胎的）')
    db_session.add(tire)
    hr = Department(name='HR（协助人口买卖）')
    db_session.add(hr)

    manager = Role(name='product manager')
    db_session.add(manager)
    engineer = Role(name='engineer')
    db_session.add(engineer)

    hydra = Employee(name='Hydra', department=one_app, role=engineer)
    db_session.add(hydra)
    samuel = Employee(name='Samuel', department=one_app, role=engineer)
    db_session.add(samuel)
    tony = Employee(name='Tony', department=one_app, role=manager)
    db_session.add(tony)
    daisy = Employee(name='Daisy', department=tire, role=manager)
    db_session.add(daisy)
    kyle = Employee(name='Kyle', department=tire, role=engineer)
    db_session.add(kyle)
    xenia = Employee(name='Xenia', department=hr, role=manager)
    db_session.add(xenia)
    db_session.commit()

