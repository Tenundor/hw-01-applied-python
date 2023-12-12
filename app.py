import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from PIL import Image

from services import engine


@st.cache_data
def load_data():
    with engine.connect() as connection:
        return pd.read_sql(
            """
            SELECT target, age, gender, child_total, dependants,
                   socstatus_work_fl, socstatus_pens_fl, fl_presence_fl,
                   own_auto, personal_income, loan_num_total, loan_num_closed 
            FROM agreement_summary
            """,
            connection
        )


def write_feature_distribution_graphs(df: pd.DataFrame):
    st.write("## Распределение признаков")

    fig, axs = plt.subplots(nrows=6, ncols=2, figsize=(10, 20))
    axs = axs.flatten()

    axs[0].set_title("по возрастам")
    sns.histplot(data=df, x="age", kde=True, ax=axs[0])

    axs[1].set_title("по доходам")
    sns.histplot(data=df, x="personal_income", kde=True, ax=axs[1])

    axs[2].set_title("по полу")
    sns.countplot(data=df, x="gender", ax=axs[2])

    axs[3].set_title("по количеству детей")
    sns.countplot(data=df, x="child_total", ax=axs[3])

    axs[4].set_title("по количеству иждивенцев")
    sns.countplot(data=df, x="dependants", ax=axs[4])

    axs[5].set_title("по количеству авто в собственности")
    sns.countplot(data=df, x="own_auto", ax=axs[5])

    axs[6].set_title("по статусу трудоустройства")
    work_statuses = ("работает", "не работает")
    sns.countplot(data=df, x="socstatus_work_fl", ax=axs[6], order=[1, 0])
    axs[6].set_xticks([1, 0])
    axs[6].set_xticklabels(work_statuses)

    axs[7].set_title("по пенсионному статусу")
    pens_statuses = ("пенсионер", "не пенсионер")
    sns.countplot(data=df, x="socstatus_pens_fl", ax=axs[7], order=[1, 0])
    axs[7].set_xticks([1, 0])
    axs[7].set_xticklabels(pens_statuses)

    axs[8].set_title("по наличию недвижимости")
    presence_labels = ("да", "нет")
    sns.countplot(data=df, x="fl_presence_fl", ax=axs[8], order=[True, False])
    axs[8].set_xticks([True, False])
    axs[8].set_xticklabels(presence_labels)

    axs[9].set_title("по кредитной истории")
    sns.countplot(data=df, x="loan_num_total", ax=axs[9])

    axs[10].set_title("по количеству закрытых кредитов")
    sns.countplot(data=df, x="loan_num_closed", ax=axs[10])

    axs[11].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig)


def write_df_correlations(df: pd.DataFrame):
    st.write("## Матрица корреляций")
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".1f", cmap="coolwarm")
    st.pyplot(fig)


def write_pairwise_scatterplots(df: pd.DataFrame):
    st.write("## Диаграммы рассеяния для наиболее скореллированных пар признаков")
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
    axs = axs.flatten()

    axs[0].set_title("Общее число кредитов к числу закрытых")
    sns.regplot(data=df, x="loan_num_total", y="loan_num_closed", ax=axs[0])

    axs[1].set_title("Пенсионный статус к статусу занятости")
    sns.regplot(data=df, x="socstatus_pens_fl", y="socstatus_work_fl", ax=axs[1])

    axs[2].set_title("Возраст к статусу занятости")
    sns.regplot(data=df, x="age", y="socstatus_work_fl", ax=axs[2])

    axs[3].set_title("Возраст к пенсионному статусу")
    sns.regplot(data=df, x="age", y="socstatus_pens_fl", ax=axs[3])

    axs[4].set_title("Возраст к количеству иждивенцев")
    sns.regplot(data=df, x="age", y="dependants", ax=axs[4])

    axs[5].set_title("Возраст к количеству детей")
    sns.regplot(data=df, x="age", y="child_total", ax=axs[5])

    plt.tight_layout()
    st.pyplot(fig)


def write_featers_target_correlations(df: pd.DataFrame):
    st.write("## Диаграммы отношения значений признаков к целевой переменной")
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
    axs = axs.flatten()

    axs[0].set_title("Количество иждивенцев к целевой переменной")
    sns.barplot(x="dependants", y="target", errorbar=None, data=df, ax=axs[0])

    axs[1].set_title("Возраст к целевой переменной")
    sns.regplot(data=df, x="age", y="target", ax=axs[1])

    axs[2].set_title("Количество закрытых кредитов к целевой переменной")
    sns.barplot(x="loan_num_closed", y="target", errorbar=None, data=df, ax=axs[2])

    axs[3].set_title("Доход к целевой переменной")
    sns.regplot(x="personal_income", y="target", data=df, ax=axs[3])

    axs[4].set_title("Статус занятости к целевой переменной")
    sns.barplot(x="socstatus_work_fl", y="target", data=df, ax=axs[4])

    axs[5].set_title("Пенсионный статус к целевой переменной")
    sns.barplot(x="socstatus_pens_fl", y="target", data=df, ax=axs[5])

    plt.tight_layout()
    st.pyplot(fig)


def process_main_page():
    image = Image.open("data/img.png")

    st.set_page_config(
        layout="centered",
        page_title="Bank clients classification",
    )

    st.write("# Классификация клиентов по склонности к отклику на предложения банка")
    st.image(image)

    df = load_data()

    write_feature_distribution_graphs(df)
    write_df_correlations(df)
    write_pairwise_scatterplots(df)
    write_featers_target_correlations(df)

    st.write("## Статистические характеристики набора данных")
    st.write(df.describe())


if __name__ == "__main__":
    process_main_page()
