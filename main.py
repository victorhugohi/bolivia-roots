import streamlit as st
import random

# Initialize session state
if "tokens" not in st.session_state:
    st.session_state.tokens = random.randint(0, 30)  # Random initial tokens
if "visited_communities" not in st.session_state:
    st.session_state.visited_communities = random.sample([
        "Torotoro National Park", "Noel Kempff Mercado National Park", "Sajama National Park",
        "Isiboro Sécure National Park", "Madidi National Park"
    ], random.randint(0, 3))  # Random visited communities
if "reviewed_communities" not in st.session_state:
    st.session_state.reviewed_communities = [] #Start empty

# Bolivian Communities (Non-Mainstream)
communities = [
    {"name": "Torotoro National Park", "description": "Dinosaur footprints and canyons.", "image": "images/torotoro.jpeg", "location": [-18.05, -65.75]},
    {"name": "Noel Kempff Mercado National Park", "description": "Amazonian biodiversity hotspot.", "image": "images/noelkempff.jpeg", "location": [-14.5, -61.0]},
    {"name": "Sajama National Park", "description": "Highest peak in Bolivia.", "image": "images/sajama.jpeg", "location": [-18.1, -68.9]},
    {"name": "Isiboro Sécure National Park", "description": "Lowland rainforest and indigenous communities.", "image": "images/isiboro.jpeg", "location": [-16.5, -65.0]},
    {"name": "Madidi National Park", "description": "Diverse ecosystems from Andes to Amazon.", "image": "images/madidi.jpeg", "location": [-14.0, -68.0]},
]

st.set_page_config(page_title="Bolivia Roots - User Profile", page_icon="🇧🇴")
st.title("Bolivia Roots - User Profile")

# User Information
st.header("Welcome, Explorer!")

# Token Information
st.subheader(f"Your Tokens: {st.session_state.tokens}")

# Visited Communities History
st.subheader("Your Travel History:")
if st.session_state.visited_communities:
    for community_name in st.session_state.visited_communities:
        st.write(f"- {community_name}")
else:
    st.write("You haven't visited any communities yet.")

# Available Rewards based on tokens
st.subheader("Available Rewards:")

if st.session_state.tokens >= 20:
    st.write("**Multi-Day Trek in Sajama National Park (20 Tokens)**")
    if st.button("Redeem Trek", key="redeem_trek"):
        st.session_state.tokens -= 20
        st.success("Trek redeemed! Enjoy your adventure!")
        st.experimental_rerun()

if st.session_state.tokens >= 10:
    st.write("**Guided Tour of Torotoro National Park (10 Tokens)**")
    if st.button("Redeem Tour", key="redeem_tour"):
        st.session_state.tokens -= 10
        st.success("Tour redeemed! Get ready to explore!")
        st.experimental_rerun()

elif st.session_state.tokens >= 5:
    st.write("**Local Craft Workshop in a nearby Community (5 Tokens)**")
    if st.button("Redeem Workshop", key="redeem_workshop"):
        st.session_state.tokens -= 5
        st.success("Workshop redeemed! Get creative!")
        st.experimental_rerun()

else:
    st.write("You don't have enough tokens yet. Explore more communities!")

# Community Exploration Section
st.header("Explore Bolivian Communities and Earn Tokens")
col1, col2, col3 = st.columns(3)

for i, community in enumerate(communities):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        st.image(community["image"], width=200)
        st.subheader(community["name"])
        st.write(community["description"])

        visit_key = f"visit_{community['name']}"
        review_key = f"review_{community['name']}"

        if st.button("Visit", key=visit_key, disabled=community["name"] in st.session_state.visited_communities):
            st.session_state.tokens += 5
            st.session_state.visited_communities.append(community["name"])
            st.experimental_rerun()

        if st.button("Review", key=review_key, disabled=community["name"] in st.session_state.reviewed_communities and community["name"] in st.session_state.visited_communities): #Only if visited
            st.session_state.tokens += 2
            st.session_state.reviewed_communities.append(community["name"])
            st.experimental_rerun()