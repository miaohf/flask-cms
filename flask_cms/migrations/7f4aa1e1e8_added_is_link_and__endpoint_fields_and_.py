"""added is_link and _endpoint fields and endpoint hybrid_property to page.models.Button

Revision ID: 7f4aa1e1e8
Revises: 3635cb739a3d
Create Date: 2014-08-02 03:24:55.879886

"""

# revision identifiers, used by Alembic.
revision = '7f4aa1e1e8'
down_revision = '3635cb739a3d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buttons', sa.Column('_endpoint', sa.String(length=255), nullable=True))
    op.add_column('buttons', sa.Column('is_link', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buttons', 'is_link')
    op.drop_column('buttons', '_endpoint')
    ### end Alembic commands ###