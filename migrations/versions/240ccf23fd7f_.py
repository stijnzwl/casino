"""empty message

Revision ID: 240ccf23fd7f
Revises: c41b55c6e1c1
Create Date: 2024-02-21 22:09:04.752344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '240ccf23fd7f'
down_revision = 'c41b55c6e1c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balance', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('balance')

    # ### end Alembic commands ###
