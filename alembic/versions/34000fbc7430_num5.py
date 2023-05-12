"""num5

Revision ID: 34000fbc7430
Revises: 24dd5b863374
Create Date: 2023-05-11 21:05:48.628925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34000fbc7430'
down_revision = '24dd5b863374'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videohashs')
    op.drop_table('videocards')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videocards',
    sa.Column('id', sa.SMALLINT(), server_default=sa.text("nextval('videocards_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='videocards_pkey'),
    sa.UniqueConstraint('name', name='videocards_name_key')
    )
    op.create_table('videohashs',
    sa.Column('id', sa.SMALLINT(), server_default=sa.text("nextval('videohashs_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='videohashs_pkey'),
    sa.UniqueConstraint('name', name='videohashs_name_key')
    )
    # ### end Alembic commands ###
