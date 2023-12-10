import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Client(Base):
    """Описание данных клиентов"""
    __tablename__ = "client"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    age = sa.Column(sa.Integer, nullable=False)
    gender = sa.Column(sa.Integer, nullable=False)
    education = sa.Column(sa.String(length=255), nullable=False)
    marital_status = sa.Column(sa.String(length=255), nullable=False)
    child_total = sa.Column(sa.Integer, nullable=False)
    dependants = sa.Column(sa.Integer, nullable=False)
    socstatus_work_fl = sa.Column(sa.Integer, nullable=False)
    socstatus_pens_fl = sa.Column(sa.Integer, nullable=False)
    fl_presence_fl = sa.Column(sa.Boolean, nullable=False)
    own_auto = sa.Column(sa.Integer, nullable=False)


class Agreement(Base):
    """Таблица с зафиксированными откликами клиентов на предложения банка"""
    __tablename__ = "agreement"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
    )
    target = sa.Column(sa.Boolean, nullable=False)


class Salary(Base):
    """Описание информации о заработной плате клиентов"""
    __tablename__ = "salary"

    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    personal_income = sa.Column(
        sa.Numeric(12, 2, asdecimal=True),
        nullable=True,
    )


class Loan(Base):
    """Информация о кредитной истории клиента"""
    __tablename__ = "loan"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
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
        nullable=False,
        unique=True,
    )
    closed_fl = sa.Column(
        sa.Boolean,
        nullable=False,
    )
