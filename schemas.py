import enum

from pydantic import BaseModel, Field, constr, conint, confloat


class Gender(enum.Enum):
    male = "1"
    female = "0"


class SocStatusWorkType(enum.Enum):
    employed = "0"
    unemployed = "1"
    unknown = "2"


class SocStatusPensType(enum.Enum):
    pensioner = "0"
    not_pensioner = "1"


class ClientModel(BaseModel):
    id: conint(gt=0) = Field(validation_alias="ID")
    age: conint(gt=0) = Field(validation_alias="AGE")
    gender: Gender = Field(validation_alias="GENDER")
    education: constr(max_length=255) = Field(validation_alias="EDUCATION")
    marital_status: constr(max_length=255) = Field(validation_alias="MARITAL_STATUS")
    child_total: conint(ge=0) = Field(validation_alias="CHILD_TOTAL")
    dependants: conint(ge=0) = Field(validation_alias="DEPENDANTS")
    socstatus_work_fl: SocStatusWorkType = Field(validation_alias="SOCSTATUS_WORK_FL")
    socstatus_pens_fl: SocStatusPensType = Field(validation_alias="SOCSTATUS_PENS_FL")
    fl_presence_fl: bool = Field(validation_alias="FL_PRESENCE_FL")
    own_auto: conint(ge=0) = Field(validation_alias="OWN_AUTO")

    class Config:
        use_enum_values = True


class AgreementModel(BaseModel):
    id: conint(gt=0) = Field(validation_alias="AGREEMENT_RK")
    client_id: conint(gt=0) = Field(validation_alias="ID_CLIENT")
    target: bool = Field(validation_alias="TARGET")


class SalaryModel(BaseModel):
    client_id: conint(gt=0) = Field(validation_alias="ID_CLIENT")
    personal_income: confloat(gt=0) = Field(validation_alias="PERSONAL_INCOME")


class LoanModel(BaseModel):
    id: conint(gt=0) = Field(validation_alias="ID_LOAN")
    client_id: conint(gt=0) = Field(validation_alias="ID_CLIENT")


class CloseLoanModel(BaseModel):
    loan_id: conint(gt=0) = Field(validation_alias="ID_LOAN")
    closed_fl: bool = Field(validation_alias="CLOSED_FL")
