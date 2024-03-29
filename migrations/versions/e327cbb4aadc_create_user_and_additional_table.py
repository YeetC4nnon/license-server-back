"""create_user_and_additional_table

Revision ID: e327cbb4aadc
Revises: 
Create Date: 2022-07-10 23:58:19.824895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e327cbb4aadc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history_service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('delete_at', sa.DateTime(), nullable=True),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('area', sa.Text(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_history_service_area'), 'history_service', ['area'], unique=False)
    op.create_index(op.f('ix_history_service_text'), 'history_service', ['text'], unique=False)
    op.create_index(op.f('ix_history_service_type'), 'history_service', ['type'], unique=False)
    op.create_table('users',
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('delete_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('surname', sa.Text(), nullable=False),
    sa.Column('second_name', sa.Text(), nullable=True),
    sa.Column('photo_url', sa.Text(), nullable=True),
    sa.Column('login', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('date_birthday', sa.Date(), nullable=True),
    sa.Column('last_active', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_surname'), 'users', ['surname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_surname'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_history_service_type'), table_name='history_service')
    op.drop_index(op.f('ix_history_service_text'), table_name='history_service')
    op.drop_index(op.f('ix_history_service_area'), table_name='history_service')
    op.drop_table('history_service')
    # ### end Alembic commands ###
