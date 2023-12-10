"""Initial migration

Revision ID: 7f0ce4499f11
Revises: 
Create Date: 2023-12-10 21:51:14.756817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f0ce4499f11'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('education', sa.String(length=255), nullable=False),
    sa.Column('marital_status', sa.String(length=255), nullable=False),
    sa.Column('child_total', sa.Integer(), nullable=False),
    sa.Column('dependants', sa.Integer(), nullable=False),
    sa.Column('socstatus_work_fl', sa.Integer(), nullable=False),
    sa.Column('socstatus_pens_fl', sa.Integer(), nullable=False),
    sa.Column('fl_presence_fl', sa.Boolean(), nullable=False),
    sa.Column('own_auto', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agreement',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('target', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('personal_income', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('client_id')
    )
    op.create_table('close_loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_id', sa.Integer(), nullable=False),
    sa.Column('closed_fl', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loan_id')
    )


def downgrade() -> None:
    op.drop_table('close_loan')
    op.drop_table('salary')
    op.drop_table('loan')
    op.drop_table('agreement')
    op.drop_table('client')
