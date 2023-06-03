import gzip
from sh import pg_dump
with gzip.open(f'G:\Mi unidad\\backup\dump-postgres', 'wb') as f:
  pg_dump('-h', 'localhost', '-U', 'postgres', 'my_dabatase', _out=f)