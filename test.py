import re
import math
from math import log2
from catboost import CatBoostClassifier
from urllib.parse import urlparse
import pandas as pd
import streamlit as st
import pandas as pd
from features import *



class URLSafetyAssessor:
    def __init__(self, model):
        """
        Initialize the URLSafetyAssessor with a trained model.
        
        Args:
            model: A trained CatBoost model for phishing detection.
        """
        self.model = CatBoostClassifier().load_model(model)

    @staticmethod
    def is_valid_url(url):
        """Checks if the given URL is valid and accessible."""
        try:
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ['http', 'https']:
                return False, "Invalid URL scheme"
            if parsed_url.hostname in ['localhost', '127.0.0.1']:
                return False, "Invalid or local URL"
            return True, "Valid URL"
        except ValueError:
            return False, "Invalid URL format"

    # Add all previously defined feature functions here...

    @staticmethod
    def extract_url_features(url):
        """Extracts features from a URL for phishing detection."""
        
        features = {
            'url_length': url_length(url),
            'number_of_dots_in_url': number_of_dots_in_url(url),
            'having_repeated_digits_in_url': int(having_repeated_digits_in_url(url)),
            'number_of_digits_in_url': number_of_digits_in_url(url),
            'number_of_special_char_in_url': number_of_special_char_in_url(url),
            'number_of_hyphens_in_url': number_of_hyphens_in_url(url),
            'number_of_underline_in_url': number_of_underline_in_url(url),
            'number_of_slash_in_url': number_of_slash_in_url(url),
            'number_of_questionmark_in_url': number_of_questionmark_in_url(url),
            'number_of_equal_in_url': number_of_equal_in_url(url),
            'number_of_at_in_url': number_of_at_in_url(url),
            'number_of_dollar_in_url': number_of_dollar_sign_in_url(url),
            'number_of_exclamation_in_url': number_of_exclamation_in_url(url),
            'number_of_hashtag_in_url': number_of_hashtag_in_url(url),
            'number_of_percent_in_url': number_of_percent_in_url(url),
            'domain_length': domain_length(url),
            'number_of_dots_in_domain': number_of_dots_in_domain(url),
            'number_of_hyphens_in_domain': number_of_hyphens_in_domain(url),
            'having_special_characters_in_domain': int(having_special_characters_in_domain(url)),
            'number_of_special_characters_in_domain': number_of_special_characters_in_domain(url),
            'having_digits_in_domain': int(having_digits_in_domain(url)),
            'number_of_digits_in_domain': number_of_digits_in_domain(url),
            'having_repeated_digits_in_domain': int(having_repeated_digits_in_domain(url)),
            'number_of_subdomains': number_of_subdomains(url),
            'having_dot_in_subdomain': int(having_dot_in_subdomain(url)),
            'having_hyphen_in_subdomain': int(having_hyphen_in_subdomain(url)),
            'average_subdomain_length': average_subdomain_length(url),
            'average_number_of_dots_in_subdomain': average_number_of_dots_in_subdomain(url),
            'average_number_of_hyphens_in_subdomain': average_number_of_hyphens_in_subdomain(url),
            'having_special_characters_in_subdomain': int(having_special_characters_in_subdomain(url)),
            'number_of_special_characters_in_subdomain': number_of_special_characters_in_subdomain(url),
            'having_digits_in_subdomain': int(having_digits_in_subdomain(url)),
            'number_of_digits_in_subdomain': number_of_digits_in_subdomain(url),
            'having_repeated_digits_in_subdomain': int(having_repeated_digits_in_subdomain(url)),
            'having_path': int(having_path(url)),
            'path_length': path_length(url),
            'having_query': int(having_query(url)),
            'having_fragment': int(having_fragment(url)),
            'having_anchor': int(having_anchor(url)),
            'entropy_of_url': entropy_of_url(url),
            'entropy_of_domain': entropy_of_domain(url),
            'protocol_of_url': check_protocol(url),
            'presence_of_html': is_html_url(url),
            'unusual_tld': has_unusual_tld(url),
            'unusual_words': contains_suspicious_words(url)
        }
        return pd.DataFrame([features])

    def assess_url_safety(self, url):
        """
        Assess the safety of a URL by analyzing its Full URL, Domain, and Path.
        
        Args:
            url (str): The URL to assess.

        Returns:
            dict: A dictionary with the weighted phishing score, safety message, and breakdown.
        """
        # Parse URL components
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        path = parsed_url.path if parsed_url.path else "/"

        # URL components for evaluation
        iterations = [
            ("Full URL", url),
            ("Domain", domain),
            ("Path", path)
        ]

        probabilities = []

        for step, url_part in iterations:
            feature_df = self.extract_url_features(url_part)
            prediction = self.model.predict(feature_df, prediction_type="Probability")
            probabilities.append({
                "step": step,
                "url_part": url_part,
                "probabilities": prediction
            })

        # Define weights
        weights = {"Full URL": 0.3, "Domain": 0.60, "Path": 0.1}
        assert math.isclose(sum(weights.values()), 1, rel_tol=1e-9), "Weights must sum to 1."

        # Weighted phishing score
        weighted_phishing_score = sum(
            weights[prob["step"]] * prob["probabilities"][0, 1] for prob in probabilities
        )
        legitimate_score = 1 - weighted_phishing_score
        phishing_percentage = weighted_phishing_score * 100
        legitimate_percentage = legitimate_score * 100

        # Switch-like logic for safety message
        ranges = [
            (0, 10, "Extremely safe! This URL is as legitimate as it gets. 🌟"),
            (10, 20, "Very safe! Almost no signs of phishing. 😊"),
            (20, 30, "Mostly safe. Legitimate with minimal risk. 😌"),
            (30, 40, "Somewhat safe. Could have minor risks. Proceed cautiously. 🤔"),
            (40, 50, "Neutral zone. Not clearly safe or unsafe. Stay alert! ⚖️"),
            (50, 60, "Slightly suspicious. Could be phishing. Be careful. 🧐"),
            (60, 70, "Moderately suspicious. Likely phishing. Avoid if possible. 🚨"),
            (70, 80, "High risk of phishing! Do not trust this URL. ⚡"),
            (80, 90, "Severely suspicious. This URL screams danger. ❌"),
            (90, 100, "Extremely dangerous! Definitely phishing. Stay away at all costs! 🔥"),
        ]

        # Determine message based on phishing percentage
        message = "Unknown risk level."
        for min_range, max_range, msg in ranges:
            if min_range <= phishing_percentage <= max_range:
                message = msg
                break

        # Determine the label and percentage dynamically
        if phishing_percentage > legitimate_percentage:
            label = "Risk Percentage"
            percentage = phishing_percentage
        else:
            label = "Safety Percentage"
            percentage = legitimate_percentage

        return message, label, round(percentage, 2)
        
url_identifier = URLSafetyAssessor(model="cat_url.cbm")

# Streamlit app
def main():
    st.title("URL Safety Assessment")

    st.write(
        "Enter a URL to assess its safety. The app will analyze the URL and provide a safety message along with the associated percentage."
    )

    # URL input
    url = st.text_input("Enter URL", "")

    # Add a button to trigger URL safety assessment
    if st.button('Assess URL'):
        if url:
            # Assess URL safety
            message, label, percentage = url_identifier.assess_url_safety(url)

            # Display results
            st.write(f"**Safety Message:** {message}")
            st.write(f"**{label}:** {percentage}%")
        else:
            st.write("Please enter a valid URL.")

# Run the Streamlit app
if __name__ == "__main__":
    main()