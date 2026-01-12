import difflib
import streamlit as st

st.set_page_config(page_title="Hinta-arvio", page_icon="🏠")

unit = "hinta-arvio: "

PRICES = {
    "töölö": 6315,
    "ullanlinna": 8135,
    "kallio": 5590,
    "punavuori": 7780,
    "pasila": 5360,
    "lauttasaari": 6550,
    "herttoniemi": 4695,
    "munkkiniemi": 6460,
    "meilahti": 5850,
    "vallila": 5520,
    "kamppi": 7450,
    "eira": 10885,
    "kruunuhaka": 7456,
}

def calc_price(sq: float, sqprice: float) -> float:
    return sq * sqprice

def normalize_location(user_input: str, valid_locations) -> str | None:
    user_input = (user_input or "").strip().lower()
    if not user_input:
        return None
    if user_input in valid_locations:
        return user_input
    match = difflib.get_close_matches(user_input, list(valid_locations), n=1, cutoff=0.7)
    return match[0] if match else None

st.title("🏠 Asunnon hinta-arvio")
st.caption("Syötä alue (esim. Kamppi / kamppi / KAMPI) ja neliöt.")

area_input = st.text_input("Asuinalue", placeholder="esim. Kamppi")
sqm = st.number_input("Neliömäärä (m²)", min_value=1, value=50, step=1)

if st.button("Laske", type="primary"):
    location = normalize_location(area_input, PRICES.keys())
    if not location:
        st.error("Sijaintia ei tunnistettu")
    else:
        price = calc_price(float(sqm), PRICES[location])
        st.success(f"{unit} {price:,.0f} €".replace(",", " "))
        if area_input.strip().lower() != location:
            st.info(f"Tulkitsin alueeksi: **{location}**")

st.divider()
st.subheader("Käytetyt hinnat (€/m²)")
st.write(PRICES)

