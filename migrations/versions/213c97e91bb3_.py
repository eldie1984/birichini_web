"""empty message

Revision ID: 213c97e91bb3
Revises: 
Create Date: 2019-06-22 00:56:09.015886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213c97e91bb3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alimento',
    sa.Column('codigo', sa.String(length=10), nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=True),
    sa.Column('categoria', sa.String(length=20), nullable=True),
    sa.Column('proveedor', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('kg', sa.String(length=8), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('ean', sa.String(length=13), nullable=True),
    sa.Column('arriba', sa.Integer(), nullable=True),
    sa.Column('abajo', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('codigo')
    )
    op.create_table('venta',
    sa.Column('codigo', sa.String(length=10), nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=True),
    sa.Column('categoria', sa.String(length=20), nullable=True),
    sa.Column('proveedor', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('kg', sa.String(length=8), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('ean', sa.String(length=13), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta')
    op.drop_table('alimento')
    # ### end Alembic commands ###