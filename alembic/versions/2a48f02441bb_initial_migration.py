"""Initial migration

Revision ID: 2a48f02441bb
Revises: 
Create Date: 2023-12-10 19:40:37.842610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a48f02441bb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('pens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flag', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flag', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('education', sa.String(), nullable=False),
    sa.Column('martial_status', sa.String(), nullable=False),
    sa.Column('child_total', sa.Integer(), nullable=False),
    sa.Column('dependants', sa.Integer(), nullable=False),
    sa.Column('socstatus_work_fl', sa.Integer(), nullable=False),
    sa.Column('socstatus_pens_fl', sa.Integer(), nullable=False),
    sa.Column('reg_address_province', sa.Text(), nullable=True),
    sa.Column('fact_address_province', sa.Text(), nullable=True),
    sa.Column('postal_address_province', sa.Text(), nullable=True),
    sa.Column('fl_presence_fl', sa.Integer(), nullable=False),
    sa.Column('own_auto', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['socstatus_pens_fl'], ['pens.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['socstatus_work_fl'], ['work.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agreement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('target', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gen_industry', sa.Text(), nullable=False),
    sa.Column('gen_title', sa.Text(), nullable=False),
    sa.Column('job_dir', sa.Text(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('last_credit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('credit_amount', sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column('term', sa.Integer(), nullable=False),
    sa.Column('first_payment', sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('family_income_from', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('family_income_to', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.Column('personal_income', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('close_loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('close_loan')
    op.drop_table('salary')
    op.drop_table('loan')
    op.drop_table('last_credit')
    op.drop_table('job')
    op.drop_table('agreement')
    op.drop_table('client')
    op.drop_table('work')
    op.drop_table('pens')
