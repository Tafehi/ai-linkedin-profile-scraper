import os
from dotenv import load_dotenv


from utils.linkedin import LinkedInProfileScraper 


import streamlit as st


if __name__ == "__main__":
    
    print("Starting LinkedIn profile scraping...")
    scraper = LinkedInProfileScraper(
        linkedin_url="https://www.linkedin.com/in/ehsan-tafehi/", mock=True
    )
    linked_data = scraper.scrape_linkedin_profile()
    print(linked_data)

    # Simulate a request to the LinkedIn profile (this won't work without proper headers and authentication)


# # Streamlit UI
# st.title("🔍 LinkedIn Profile Explorer USing AI")
# name = st.text_input("Enter a person's name", placeholder="e.g., Elon Musk")

# if name:
#     with st.spinner("Generating summary..."):
#         result = chain.invoke({"person": name})
#         st.subheader("📝 Summary & Facts")
#         st.write(result)

#     # Display image (example for Elon Musk)
#     if name.lower() == "elon musk":
#         st.subheader("📸 Photo")
#         st.image("https://media.gettyimages.com/photos/elon-musk-attends-the-10th-annual-breakthrough-prize-ceremony-picture-id1492022342", caption="Elon Musk", use_column_width=True)
