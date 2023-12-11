"""Add agreement_summary table

Revision ID: 77766034c35e
Revises: 7f0ce4499f11
Create Date: 2023-12-11 11:50:08.505318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77766034c35e'
down_revision: Union[str, None] = '7f0ce4499f11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('agreement_summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agreement_id', sa.Integer(), nullable=False),
    sa.Column('target', sa.Boolean(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('child_total', sa.Integer(), nullable=False),
    sa.Column('dependants', sa.Integer(), nullable=False),
    sa.Column('socstatus_work_fl', sa.Integer(), nullable=False),
    sa.Column('socstatus_pens_fl', sa.Integer(), nullable=False),
    sa.Column('fl_presence_fl', sa.Boolean(), nullable=False),
    sa.Column('own_auto', sa.Integer(), nullable=False),
    sa.Column('personal_income', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('loan_num_total', sa.Integer(), nullable=False),
    sa.Column('loan_num_closed', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agreement_id'], ['agreement.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('agreement_id')
    )


def downgrade() -> None:
    op.drop_table('agreement_summary')
