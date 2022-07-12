"""change_license_table

Revision ID: 7b85cd166eae
Revises: 27ca3285a8ac
Create Date: 2022-07-11 15:07:39.938569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b85cd166eae'
down_revision = '27ca3285a8ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('licenses_group_uuid_key', 'licenses', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('licenses_group_uuid_key', 'licenses', ['group_uuid'])
    # ### end Alembic commands ###