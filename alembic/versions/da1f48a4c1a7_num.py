"""num

Revision ID: da1f48a4c1a7
Revises: 
Create Date: 2023-05-02 14:52:58.835500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da1f48a4c1a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('role', sa.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role')
    )
    op.create_table('start',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('texts',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=256), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('start_id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['start_id'], ['start.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('role_id', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brands',
    sa.Column('category_id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('models',
    sa.Column('brand_id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('models')
    op.drop_table('brands')
    op.drop_table('users')
    op.drop_table('categories')
    op.drop_table('texts')
    op.drop_table('start')
    op.drop_table('roles')
    # ### end Alembic commands ###
