import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#postgresql://digimon_qxsz_user:ULYJQ96HVaGDM9HvMfDOz6dKLwsTlJ8O@dpg-cvn3ssumcj7s73c39ib0-a.oregon-postgres.render.com/digimon_qxsz
SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://digimon_qxsz_user:ULYJQ96HVaGDM9HvMfDOz6dKLwsTlJ8O@dpg-cvn3ssumcj7s73c39ib0-a.oregon-postgres.render.com/digimon_qxsz'
SQLALCHEMY_TRACK_MODIFICATIONS=False

