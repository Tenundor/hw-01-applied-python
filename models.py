import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Work(Base):
    """Описание статусов относительно работы"""
    __tablename__ = 'work'

    id = sa.Column(sa.Integer, primary_key=True)
    flag = sa.Column(sa.Integer, nullable=False)
    comment = sa.Column(sa.String, nullable=True)


class Pens(Base):
    """Описание статусов относительно пенсии"""
    __tablename__ = 'pens'

    id = sa.Column(sa.Integer, primary_key=True)
    flag = sa.Column(sa.Integer, nullable=False)
    comment = sa.Column(sa.String, nullable=True)


class Client(Base):
    """Описание данных клиентов"""
    __tablename__ = "client"

    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Integer, nullable=False)
    gender = sa.Column(sa.Integer, nullable=False)
    education = sa.Column(sa.String, nullable=False)
    martial_status = sa.Column(sa.String, nullable=False)
    child_total = sa.Column(sa.Integer, nullable=False)
    dependants = sa.Column(sa.Integer, nullable=False)
    socstatus_work_fl = sa.Column(
        sa.Integer,
        sa.ForeignKey(
            "work.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    socstatus_pens_fl = sa.Column(
        sa.Integer,
        sa.ForeignKey(
            "pens.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    reg_address_province = sa.Column(sa.Text, nullable=True)
    fact_address_province = sa.Column(sa.Text, nullable=True)
    postal_address_province = sa.Column(sa.Text, nullable=True)
    fl_presence_fl = sa.Column(sa.Integer, nullable=False)
    own_auto = sa.Column(sa.Integer, nullable=False)


class Agreement(Base):
    """Таблица с зафиксированными откликами клиентов на предложения банка"""
    __tablename__ = "agreement"

    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )
    target = sa.Column(sa.Boolean, nullable=False)


class Job(Base):
    """Описание информации о работе клиентов"""
    __tablename__ = "job"

    id = sa.Column(sa.Integer, primary_key=True)
    gen_industry = sa.Column(sa.Text, nullable=False)
    gen_title = sa.Column(sa.Text, nullable=False)
    job_dir = sa.Column(sa.Text, nullable=False)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )


class Salary(Base):
    """Описание информации о заработной плате клиентов"""
    __tablename__ = "salary"

    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )
    family_income_from = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=True,
    )
    family_income_to = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=True
    )
    personal_income = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=True,
    )


class LastCredit(Base):
    """Информация о последнем займе клиента"""
    __tablename__ = "last_credit"

    id = sa.Column(sa.Integer, primary_key=True)
    credit_amount = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=False,
    )
    term = sa.Column(sa.Integer, nullable=False)
    first_payment = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=False,
    )
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )


class Loan(Base):
    """Информация о кредитной истории клиента"""
    __tablename__ = "loan"

    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )


class CloseLoan(Base):
    """Информация о статусах кредита (ссуд)"""
    __tablename__ = "close_loan"

    id = sa.Column(sa.Integer, primary_key=True)
    loan_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("loan.id", ondelete="CASCADE"),
        nullable=False
    )
