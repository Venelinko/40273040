"""Title attrubute added to Article

Revision ID: 4bd40e1de96f
Revises: 83e5751f4699
Create Date: 2019-12-03 16:35:34.888734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bd40e1de96f'
down_revision = '83e5751f4699'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('title', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'title')
    # ### end Alembic commands ###