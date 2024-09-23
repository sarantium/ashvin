import streamlit as st
import sqlite3
import pandas as pd

# Database setup
conn = sqlite3.connect('startups.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS startups
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              category TEXT NOT NULL,
              funding REAL,
              description TEXT)''')
conn.commit()

def add_startup(name, category, funding, description):
    c.execute("INSERT INTO startups (name, category, funding, description) VALUES (?, ?, ?, ?)",
              (name, category, funding, description))
    conn.commit()

def search_startups(query):
    c.execute("SELECT * FROM startups WHERE name LIKE ? OR category LIKE ?",
              ('%'+query+'%', '%'+query+'%'))
    return c.fetchall()

def get_all_startups():
    c.execute("SELECT * FROM startups")
    return c.fetchall()

# Streamlit UI
st.title("Startup Directory")

# Sidebar for adding startups
st.sidebar.header("Add New Startup")
new_name = st.sidebar.text_input("Name")
new_category = st.sidebar.text_input("Category")
new_funding = st.sidebar.number_input("Funding", min_value=0.0)
new_description = st.sidebar.text_area("Description")
if st.sidebar.button("Add Startup"):
    add_startup(new_name, new_category, new_funding, new_description)
    st.sidebar.success("Startup added successfully!")

# Search functionality
search_query = st.text_input("Search startups")
if search_query:
    results = search_startups(search_query)
    st.write(f"Found {len(results)} results:")
    for startup in results:
        st.write(f"- {startup[1]} ({startup[2]}): ${startup[3]} million")

# Market Map Grid
st.header("Market Map")
all_startups = get_all_startups()
if all_startups:
    df = pd.DataFrame(all_startups, columns=['id', 'name', 'category', 'funding', 'description'])
    categories = df['category'].unique()
    
    # Create a grid layout
    cols = st.columns(len(categories))
    
    for idx, category in enumerate(categories):
        with cols[idx]:
            st.subheader(category)
            category_startups = df[df['category'] == category]
            for _, startup in category_startups.iterrows():
                with st.container():
                    st.write(f"**{startup['name']}**")
                    st.write(f"Funding: ${startup['funding']} million")
                    st.write(startup['description'])
                st.markdown("---")
else:
    st.write("No startups in the database yet.")

# Close the database connection
conn.close()