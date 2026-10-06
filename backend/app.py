from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

from utils.feature_extraction import extract_features


app = Flask(__name__)
CORS(app)


# --------------------------------------------------
# Load trained ML model
# --------------------------------------------------

model = joblib.load("model/model.pkl")

print("ML model loaded successfully!")


# --------------------------------------------------
# Feature order used during model training
# --------------------------------------------------

FEATURE_COLUMNS = [
    "having_IP_Address",
    "URL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
    "SSLfinal_State",
    "Domain_registeration_length",
    "Favicon",
    "port",
    "HTTPS_token",
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
    "age_of_domain",
    "DNSRecord",
    "web_traffic",
    "Page_Rank",
    "Google_Index",
    "Links_pointing_to_page",
    "Statistical_report"
]


# --------------------------------------------------
# Generate understandable reasons
# --------------------------------------------------

def generate_reasons(features):

    reasons = []

    # Suspicious URL features

    if features["having_IP_Address"] == -1:
        reasons.append(
            "URL contains an IP address instead of a normal domain"
        )

    if features["URL_Length"] == -1:
        reasons.append(
            "URL is unusually long"
        )

    if features["Shortining_Service"] == -1:
        reasons.append(
            "URL shortening service detected"
        )

    if features["having_At_Symbol"] == -1:
        reasons.append(
            "URL contains an @ symbol"
        )

    if features["double_slash_redirecting"] == -1:
        reasons.append(
            "Suspicious double-slash redirection detected"
        )

    if features["Prefix_Suffix"] == -1:
        reasons.append(
            "Domain contains a suspicious hyphen pattern"
        )

    if features["having_Sub_Domain"] == -1:
        reasons.append(
            "Multiple subdomains detected"
        )

    # Security features

    if features["SSLfinal_State"] == -1:
        reasons.append(
            "Website does not use HTTPS"
        )

    if features["port"] == -1:
        reasons.append(
            "Suspicious or non-standard port detected"
        )

    if features["HTTPS_token"] == -1:
        reasons.append(
            "Suspicious HTTPS token found in the domain"
        )

    # Page behaviour

    if features["Request_URL"] == -1:
        reasons.append(
            "High proportion of external resources detected"
        )

    if features["URL_of_Anchor"] == -1:
        reasons.append(
            "Many links point to external domains"
        )

    if features["Links_in_tags"] == -1:
        reasons.append(
            "Suspicious external links found in page tags"
        )

    if features["SFH"] == -1:
        reasons.append(
            "Suspicious form submission handler detected"
        )

    if features["Submitting_to_email"] == -1:
        reasons.append(
            "Form submits information to an email address"
        )

    # Browser behaviour

    if features["Redirect"] == -1:
        reasons.append(
            "Multiple redirects detected"
        )

    if features["on_mouseover"] == -1:
        reasons.append(
            "Suspicious mouse-over behavior detected"
        )

    if features["RightClick"] == -1:
        reasons.append(
            "Right-click appears to be disabled"
        )

    if features["popUpWidnow"] == -1:
        reasons.append(
            "Suspicious popup behavior detected"
        )

    if features["Iframe"] == -1:
        reasons.append(
            "Iframe detected on the webpage"
        )

    # If nothing suspicious was found

    if len(reasons) == 0:

        reasons.append(
            "No major suspicious indicators were detected"
        )

    return reasons


# --------------------------------------------------
# Home route
# --------------------------------------------------

@app.route("/")
def home():

    return "ShopShield AI Backend is Running!"


# --------------------------------------------------
# Analyze website
# --------------------------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "error": "No data received"
        }), 400

    url = data.get("url")

    if not url:

        return jsonify({
            "success": False,
            "error": "URL is required"
        }), 400

    try:

        # ------------------------------------------
        # Extract features
        # ------------------------------------------

        features = extract_features(url)

        print("\nExtracted Features:")
        print(features)


        # ------------------------------------------
        # Convert to DataFrame
        # ------------------------------------------

        feature_data = pd.DataFrame(
            [[features[column] for column in FEATURE_COLUMNS]],
            columns=FEATURE_COLUMNS
        )


        # ------------------------------------------
        # ML prediction
        # ------------------------------------------

        prediction = model.predict(feature_data)[0]


        # ------------------------------------------
        # Prediction probabilities
        # ------------------------------------------

        probabilities = model.predict_proba(
            feature_data
        )[0]

        classes = model.classes_

        phishing_probability = probabilities[
            list(classes).index(-1)
        ]

        legitimate_probability = probabilities[
            list(classes).index(1)
        ]


        # ------------------------------------------
        # Convert prediction
        # ------------------------------------------

        if prediction == -1:

            result = "Phishing"

        else:

            result = "Legitimate"


        # ------------------------------------------
        # Risk score
        # ------------------------------------------

        risk_score = round(
            float(phishing_probability) * 100,
            2
        )


        # ------------------------------------------
        # Risk level
        # ------------------------------------------

        if risk_score <= 30:

            risk_level = "Low Risk"

        elif risk_score <= 60:

            risk_level = "Medium Risk"

        else:

            risk_level = "High Risk"


        # ------------------------------------------
        # Generate reasons
        # ------------------------------------------

        reasons = generate_reasons(features)


        # ------------------------------------------
        # Final response
        # ------------------------------------------

        return jsonify({

            "success": True,

            "url": url,

            "prediction": result,

            "risk_score": risk_score,

            "risk_level": risk_level,

            "phishing_probability":
                round(
                    float(phishing_probability) * 100,
                    2
                ),

            "legitimate_probability":
                round(
                    float(legitimate_probability) * 100,
                    2
                ),

            "reasons": reasons,

            "features": features

        })


    except Exception as e:

        print("\nERROR:")
        print(e)

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


# --------------------------------------------------
# Run Flask server
# --------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)