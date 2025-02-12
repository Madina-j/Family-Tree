"""adds Person  model

Revision ID: 28509483df19
Revises: 
Create Date: 2025-01-27 11:13:06.892944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28509483df19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('dob', sa.String(), nullable=True),
    sa.Column('father_id', sa.Integer(), nullable=True),
    sa.Column('mother_id', sa.Integer(), nullable=True),
    sa.Column('place_of_birth', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['father_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['mother_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
