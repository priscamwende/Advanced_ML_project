import streamlit as st
import pandas as pd
import joblib
from io import BytesIO
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAXResults



# MODEL LOADING (cached so files are only read once)


@st.cache_resource
def load_models():
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
    kpca = joblib.load("kpca.pkl")
    sarima_model = SARIMAXResults.load("sarima_model.pkl")
    return kmeans, scaler, kpca, sarima_model


kmeans, scaler, kpca, sarima_model = load_models()

TRAINING_COLUMNS = [
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

# Maps the raw KMeans cluster label -> consumption regime name
# (matches the mapping used during training in the notebook)
CLUSTER_MAPPING = {
    0: "Very Low",
    2: "Low",
    4: "Low-Medium",
    3: "Medium",
    5: "Medium-High",
    1: "High"
}


CLUSTER_DETAILS = {
    0: {
        "name": "Very Low",
        "interpretation": (
            "This household belongs to the Very Low Consumption cluster. "
            "Electricity usage is minimal compared to other households."
        ),
        "advice": (
            "• Keep up your energy-saving habits.\n"
            "• Monitor consumption periodically.\n"
            "• Ensure appliances and the meter are functioning properly."
        ),
    },
    1: {
        "name": "High",
        "interpretation": (
            "This household belongs to the High Consumption cluster. "
            "It has the highest electricity usage among all households."
        ),
        "advice": (
            "• Switch off unused appliances.\n"
            "• Use energy-efficient appliances and LED lighting.\n"
            "• Monitor daily electricity consumption.\n"
            "• Consider renewable energy options such as solar."
        ),
    },
    2: {
        "name": "Low",
        "interpretation": (
            "This household belongs to the Low Consumption cluster. "
            "Electricity usage is relatively low and efficient."
        ),
        "advice": (
            "• Continue practicing energy-saving habits.\n"
            "• Avoid unnecessary standby power.\n"
            "• Monitor monthly electricity usage."
        ),
    },
    3: {
        "name": "Medium",
        "interpretation": (
            "This household belongs to the Medium Consumption cluster. "
            "Electricity usage is around the average level."
        ),
        "advice": (
            "• Continue using electricity efficiently.\n"
            "• Monitor high-power appliances.\n"
            "• Schedule routine electrical maintenance."
        ),
    },
    4: {
        "name": "Low-Medium",
        "interpretation": (
            "This household belongs to the Low-Medium Consumption cluster. "
            "Electricity usage is slightly below average."
        ),
        "advice": (
            "• Identify appliances with higher energy use.\n"
            "• Reduce standby power.\n"
            "• Continue monitoring electricity bills."
        ),
    },
    5: {
        "name": "Medium-High",
        "interpretation": (
            "This household belongs to the Medium-High Consumption cluster. "
            "Electricity usage is above average but not the highest."
        ),
        "advice": (
            "• Reduce unnecessary appliance usage.\n"
            "• Consider energy-efficient alternatives.\n"
            "• Track consumption to identify savings opportunities."
        ),
    },
}



# PDF REPORT FUNCTION 

def create_pdf(owner_name, household_id, data, cluster_name, interpretation, advice):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>HOUSEHOLD POWER CONSUMPTION CLUSTERING REPORT</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Date Generated: {datetime.now().strftime('%d %B %Y %H:%M')}", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>Owner Name:</b> {owner_name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Household ID:</b> {household_id}", styles["Normal"]))
    story.append(Spacer(1, 15))

    story.append(Paragraph("<b>Input Measurements</b>", styles["Heading2"]))
    table_data = [["Feature", "Value"]]
    for column in data.columns:
        table_data.append([column, str(data.iloc[0][column])])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>Prediction Result</b>", styles["Heading2"]))
    story.append(Paragraph(f"Predicted Cluster: <b>{cluster_name}</b>", styles["Normal"]))
    story.append(Paragraph(f"Interpretation: {interpretation}", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(advice.replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 25))

    story.append(Paragraph("Generated by Household Power Consumption Clustering System", styles["Italic"]))

    doc.build(story)
    buffer.seek(0)
    return buffer


# PAGE 1: CLUSTER PREDICTION


def cluster_prediction_page():
    st.title("🏠 Household Power Consumption Clustering")
    st.write(
        "Enter the household power consumption measurements below "
        "to predict the household energy consumption cluster."
    )

    st.subheader("Household Information")
    household_id = st.text_input("Household ID", key="household_id")
    owner_name = st.text_input("Owner Name", key="owner_name")

    st.subheader("Power Consumption Measurements")
    gap = st.number_input("Global Active Power (kW)", min_value=0.0, format="%.3f", key="gap")
    grp = st.number_input("Global Reactive Power (kW)", min_value=0.0, format="%.3f", key="grp")
    voltage = st.number_input("Voltage (V)", min_value=0.0, format="%.2f", value=240.0, key="voltage")
    intensity = st.number_input("Global Intensity (A)", min_value=0.0, format="%.2f", key="intensity")
    sm1 = st.number_input("Sub Metering 1 (Wh)", min_value=0.0, format="%.2f", key="sm1")
    sm2 = st.number_input("Sub Metering 2 (Wh)", min_value=0.0, format="%.2f", key="sm2")
    sm3 = st.number_input("Sub Metering 3 (Wh)", min_value=0.0, format="%.2f", key="sm3")

    data = pd.DataFrame({
        "Global_active_power": [gap],
        "Global_reactive_power": [grp],
        "Voltage": [voltage],
        "Global_intensity": [intensity],
        "Sub_metering_1": [sm1],
        "Sub_metering_2": [sm2],
        "Sub_metering_3": [sm3]
    })[TRAINING_COLUMNS]

    st.subheader("Input Features")
    st.dataframe(data)

    if st.button("Predict", key="predict_button"):
        if not household_id or not owner_name:
            st.warning("Please enter both Household ID and Owner Name before predicting.")
            return

        if gap == 0 and grp == 0 and intensity == 0 and sm1 == 0 and sm2 == 0 and sm3 == 0:
            st.warning(
                "All power readings are 0 - this doesn't represent a realistic "
                "measurement and will not produce a meaningful cluster. "
                "Please enter actual readings."
            )
            return

        input_data = data.values
        scaled = scaler.transform(input_data)
        reduced = kpca.transform(scaled)
        cluster = int(kmeans.predict(reduced)[0])

        details = CLUSTER_DETAILS.get(cluster)
        if details is None:
            cluster_name = "Unknown"
            interpretation = "Unable to determine the household consumption pattern."
            advice = "Please verify the entered values and try again."
        else:
            cluster_name = details["name"]
            interpretation = details["interpretation"]
            advice = details["advice"]

        st.success(f"Predicted Cluster: {cluster}")
        st.subheader("Consumption Regime")
        st.write(f"**{cluster_name}**")
        st.subheader("Interpretation")
        st.info(interpretation)
        st.subheader("Recommendation")
        st.write(advice)

        pdf = create_pdf(owner_name, household_id, data, cluster_name, interpretation, advice)
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name=f"{household_id}_Cluster_Report.pdf",
            mime="application/pdf",
            key="download_pdf"
        )



# PAGE 2: ELECTRICITY FORECAST


def forecast_page():
    st.title("📈 Household Electricity Consumption Forecast")
    st.write(
        """
        Forecast future household electricity consumption
        using the trained SARIMA model.
        """
    )

    st.subheader("Forecast Settings")
    forecast_hours = st.slider(
        "Forecast Horizon (Hours)",
        min_value=24,
        max_value=720,
        value=168,
        step=24,
        key="forecast_hours"
    )

    if st.button("Generate Forecast", key="forecast_button"):
        forecast = sarima_model.forecast(steps=forecast_hours)

        forecast_df = pd.DataFrame({
            "Hour": range(1, forecast_hours + 1),
            "Forecasted Global Active Power (kW)": forecast.values
        })

        st.success("Forecast generated successfully!")

        st.subheader("Forecast Table")
        st.dataframe(forecast_df)

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(
            forecast_df["Hour"],
            forecast_df["Forecasted Global Active Power (kW)"],
            color="red",
            linewidth=2
        )
        ax.set_title("Future Household Electricity Consumption")
        ax.set_xlabel("Forecast Hour")
        ax.set_ylabel("Global Active Power (kW)")
        ax.grid(True)
        st.pyplot(fig)

        st.subheader("Forecast Summary")
        st.metric("Average Forecast", f"{forecast_df['Forecasted Global Active Power (kW)'].mean():.2f} kW")
        st.metric("Maximum Forecast", f"{forecast_df['Forecasted Global Active Power (kW)'].max():.2f} kW")
        st.metric("Minimum Forecast", f"{forecast_df['Forecasted Global Active Power (kW)'].min():.2f} kW")

        csv = forecast_df.to_csv(index=False)
        st.download_button(
            "⬇ Download Forecast CSV",
            csv,
            file_name="Electricity_Forecast.csv",
            mime="text/csv",
            key="download_csv"
        )



# NAVIGATION


page = st.sidebar.radio("Navigation", ["Cluster Prediction", "Electricity Forecast"])

if page == "Cluster Prediction":
    cluster_prediction_page()
elif page == "Electricity Forecast":
    forecast_page()
