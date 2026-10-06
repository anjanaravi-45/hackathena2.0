import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [scanning, setScanning] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [showPopup, setShowPopup] = useState(false);

  // =====================================================
  // ANALYZE WEBSITE
  // =====================================================

  const analyzeWebsite = async () => {
    // Clear previous error
    setError("");

    // Check empty input
    if (!url.trim()) {
      setShowPopup(true);

      setTimeout(() => {
        setShowPopup(false);
      }, 2500);

      return;
    }

    // Start scanning
    setScanning(true);

    // Remove previous result
    setResult(null);

    try {
      // =================================================
      // SEND URL TO FLASK BACKEND
      // =================================================

      const response = await fetch(
        "http://127.0.0.1:5000/analyze",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            url: url.trim(),
          }),
        }
      );

      // Convert backend response to JSON
      const data = await response.json();

      // =================================================
      // HANDLE BACKEND ERROR
      // =================================================

      if (!response.ok || !data.success) {
        throw new Error(
          data.error || "Website analysis failed."
        );
      }

      // =================================================
      // STORE REAL BACKEND RESULT
      // =================================================

      setResult(data);

    } catch (err) {

      console.error("Backend Error:", err);

      setError(
        err.message ||
        "Unable to connect to ShopShield AI backend."
      );

    } finally {

      // Stop scanning
      setScanning(false);

    }
  };


  // =====================================================
  // HANDLE ENTER KEY
  // =====================================================

  const handleKeyDown = (e) => {

    if (e.key === "Enter" && !scanning) {
      analyzeWebsite();
    }

  };


  // =====================================================
  // CLEAR RESULT WHEN USER EDITS URL
  // =====================================================

  const handleUrlChange = (e) => {

    const value = e.target.value;

    setUrl(value);

    setResult(null);

    setError("");

  };


  // =====================================================
  // RESULT STATUS CLASS
  // =====================================================

  const getRiskClass = () => {

    if (!result) {
      return "";
    }

    if (result.risk_level === "High Risk") {
      return "high-risk";
    }

    if (result.risk_level === "Medium Risk") {
      return "medium-risk";
    }

    return "low-risk";

  };


  return (

    <div className="app">

      {/* =================================================
          CYBER SECURITY BACKGROUND
      ================================================= */}

      <div className="background-grid"></div>

      <div className="cyber-scan-line"></div>

      <div className="glow glow-one"></div>
      <div className="glow glow-two"></div>

      <div className="threat-orb orb-one"></div>
      <div className="threat-orb orb-two"></div>

      <div className="breach-warning">
        <span></span>
        THREAT MONITOR ACTIVE
      </div>


      {/* =================================================
          NAVBAR
      ================================================= */}

      <nav className="nav">

        <div className="nav-left">

          <div className="shield-logo">

            <div className="shield-outline">
              <span>◆</span>
            </div>

          </div>


          <div className="online">

            <i></i>

            AI ONLINE

          </div>

        </div>

      </nav>


      {/* =================================================
          MAIN
      ================================================= */}

      <main>

        {/* =================================================
            HERO
        ================================================= */}

        <section className="hero">

          <div className="hero-badge">

            <span>●</span>

            AI-POWERED E-COMMERCE SECURITY

          </div>


          <h1>
            SHOPSHIELD <span>AI</span>
          </h1>


          <h2>
            Shop smarter. <strong>Check first.</strong>
          </h2>


          <p>
            Protect yourself from suspicious online stores.
            ShopShield AI analyzes website signals and
            helps you understand the risk before you shop.
          </p>

        </section>


        {/* =================================================
            SCANNER
        ================================================= */}

        <section className="scanner-card">

          <div className="scanner-header">

            <div>

              <small>
                01 / WEBSITE SECURITY CHECK
              </small>

              <h3>
                Check a website before you buy.
              </h3>

            </div>


            <div className="ai-icon">
              AI
            </div>

          </div>


          {/* URL INPUT */}

          <div className="input-row">

            <input
              type="text"
              value={url}
              onChange={handleUrlChange}
              onKeyDown={handleKeyDown}
              placeholder="Paste an e-commerce website URL..."
              disabled={scanning}
            />


            <button
              onClick={analyzeWebsite}
              disabled={scanning}
            >

              {scanning
                ? "SCANNING..."
                : "ANALYZE →"}

            </button>

          </div>


          <div className="scanner-note">

            <span>●</span>

            URL · DOMAIN · THREAT SIGNALS

          </div>

        </section>


        {/* =================================================
            SCANNING ANIMATION
        ================================================= */}

        {scanning && (

          <section className="scan-card">

            <div className="scan-visual">

              <div className="loader"></div>

              <div className="loader-ring"></div>

            </div>


            <div className="scan-content">

              <small>
                LIVE THREAT ANALYSIS
              </small>

              <h3>
                Scanning website...
              </h3>

              <p>
                ShopShield AI is analyzing the website
                and checking its security characteristics.
              </p>


              <div className="scan-status">

                <span className="status-dot"></span>

                ML THREAT ENGINE ACTIVE

              </div>

            </div>

          </section>

        )}


        {/* =================================================
            ERROR
        ================================================= */}

        {error && !scanning && (

          <section className="error-card">

            <div className="error-icon">
              !
            </div>


            <div>

              <small>
                ANALYSIS ERROR
              </small>

              <h3>
                Unable to analyze website
              </h3>

              <p>
                {error}
              </p>

            </div>

          </section>

        )}


        {/* =================================================
            REAL BACKEND RESULT
        ================================================= */}

        {result && !scanning && !error && (

          <section className="result-card">

            {/* LEFT SIDE */}

            <div className="result-content">

              <small>
                SECURITY VERDICT
              </small>


              <div className="verdict-row">

                <h2 className={getRiskClass()}>
                  {result.prediction}
                </h2>

                <span className={`risk-badge ${getRiskClass()}`}>
                  {result.risk_level}
                </span>

              </div>


              <p className="analyzed-url">
                <span>ANALYZED URL</span>

                {result.url}

              </p>


              <p className="result-message">

                {result.prediction === "Phishing"

                  ? "This website shows characteristics associated with phishing websites. Avoid entering sensitive information or making payments until it is verified."

                  : "This website appears legitimate according to the current ML model analysis. However, no automated system can guarantee that a website is completely safe."}

              </p>


              {/* =================================================
                  THREAT INDICATORS
              ================================================= */}

              <div className="signals-title">
                DETECTED INDICATORS
              </div>


              <div className="signals">

                {result.reasons &&
                result.reasons.length > 0 ? (

                  result.reasons.map((reason, index) => (

                    <div
                      className="signal threat"
                      key={index}
                    >

                      <b>
                        !
                      </b>

                      <span>
                        {reason}
                      </span>

                    </div>

                  ))

                ) : (

                  <div className="signal neutral">

                    <b>
                      •
                    </b>

                    <span>
                      No major suspicious indicators
                      were detected.
                    </span>

                  </div>

                )}

              </div>

            </div>


            {/* =================================================
                SCORE
            ================================================= */}

            <div className="score-container">

              <div
                className={`score-ring ${getRiskClass()}`}
                style={{
                  "--score":
                    `${result.risk_score * 3.6}deg`,
                }}
              >

                <strong>
                  {result.risk_score}
                </strong>

                <span>
                  /100
                </span>

              </div>


              <small>
                RISK SCORE
              </small>


              {/* PROBABILITIES */}

              <div className="probabilities">

                <div>

                  <span>
                    Phishing
                  </span>

                  <strong>
                    {result.phishing_probability}%
                  </strong>

                </div>


                <div>

                  <span>
                    Legitimate
                  </span>

                  <strong>
                    {result.legitimate_probability}%
                  </strong>

                </div>

              </div>

            </div>

          </section>

        )}

      </main>


      {/* =================================================
          EMPTY URL POPUP
      ================================================= */}

      {showPopup && (

        <div className="popup-overlay">

          <div className="popup">

            <div className="popup-icon">
              !
            </div>


            <div>

              <h3>
                Please Enter The Code
              </h3>

              <p>
                Enter the website URL before
                starting the analysis.
              </p>

            </div>


            <button
              className="popup-close"
              onClick={() => setShowPopup(false)}
            >
              ×
            </button>

          </div>

        </div>

      )}


      {/* =================================================
          FOOTER
      ================================================= */}

      <footer>

        <strong>
          SHOPSHIELD <span>AI</span>
        </strong>

        <span>
          Digital trust, simplified.
        </span>

      </footer>

    </div>

  );
}

export default App;