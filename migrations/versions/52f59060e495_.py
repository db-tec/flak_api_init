"""empty message

Revision ID: 52f59060e495
Revises: 2d22d3610643
Create Date: 2020-04-09 09:30:12.813074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52f59060e495'
down_revision = '2d22d3610643'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('dt_expiracao', sa.String(length=50), nullable=False))
    op.drop_column('tarefa', 'dt_experacao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('dt_experacao', sa.DATE(), nullable=False))
    op.drop_column('tarefa', 'dt_expiracao')
    # ### end Alembic commands ###
