import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_features(url):

    # --------------------------------------------------
    # Download webpage
    # --------------------------------------------------

    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    soup = BeautifulSoup(response.text, "html.parser")

    parsed_url = urlparse(url)

    domain = parsed_url.netloc.lower()
    page_domain = domain

    # Remove www.
    clean_domain = domain.replace("www.", "")

    hostname = parsed_url.hostname or ""

    # --------------------------------------------------
    # 1. IP Address
    # --------------------------------------------------

    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}"

    has_ip = bool(re.match(ip_pattern, hostname))

    # --------------------------------------------------
    # 2. URL Length
    # --------------------------------------------------

    url_length = len(url)

    # --------------------------------------------------
    # 3. URL Shortening Service
    # --------------------------------------------------

    shortening_services = [
        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co",
        "is.gd",
        "ow.ly",
        "buff.ly",
        "rebrand.ly",
        "cutt.ly"
    ]

    is_shortened = any(
        service in domain
        for service in shortening_services
    )

    # --------------------------------------------------
    # 4. @ Symbol
    # --------------------------------------------------

    has_at = "@" in url

    # --------------------------------------------------
    # 5. Double Slash Redirecting
    # --------------------------------------------------

    path = parsed_url.path

    double_slash = "//" in path

    # --------------------------------------------------
    # 6. Prefix / Suffix
    # --------------------------------------------------

    has_prefix_suffix = "-" in clean_domain

    # --------------------------------------------------
    # 7. Sub Domain
    # --------------------------------------------------

    domain_parts = clean_domain.split(".")

    subdomain_count = max(
        len(domain_parts) - 2,
        0
    )

    if subdomain_count == 0:
        subdomain_feature = 1

    elif subdomain_count == 1:
        subdomain_feature = 0

    else:
        subdomain_feature = -1

    # --------------------------------------------------
    # 8. HTTPS / SSL
    # --------------------------------------------------

    uses_https = parsed_url.scheme.lower() == "https"

    ssl_feature = 1 if uses_https else -1

    # --------------------------------------------------
    # 9. Domain Registration Length
    # --------------------------------------------------
    # Requires WHOIS/domain registration information.
    # We will implement this later.

    domain_registration_length = 0

    # --------------------------------------------------
    # 10. Favicon
    # --------------------------------------------------

    favicon = soup.find(
        "link",
        rel=lambda value:
        value and "icon" in value
    )

    favicon_feature = 1 if favicon else -1

    # --------------------------------------------------
    # 11. Port
    # --------------------------------------------------

    port = parsed_url.port

    if port is None:
        port_feature = 1

    elif port in [80, 443]:
        port_feature = 1

    else:
        port_feature = -1

    # --------------------------------------------------
    # 12. HTTPS Token
    # --------------------------------------------------

    https_token = "https" in clean_domain

    https_token_feature = (
        -1 if https_token
        else 1
    )

    # --------------------------------------------------
    # Get webpage elements
    # --------------------------------------------------

    links = soup.find_all("a")

    forms = soup.find_all("form")

    iframes = soup.find_all("iframe")

    page_source = response.text.lower()

    # --------------------------------------------------
    # 13. Request URL
    # --------------------------------------------------

    resources = []

    for tag in soup.find_all(
        ["img", "audio", "video", "source"]
    ):

        src = tag.get("src")

        if src:
            resources.append(src)

    external_resources = 0

    for resource in resources:

        if resource.startswith(
            ("http://", "https://")
        ):

            resource_domain = (
                urlparse(resource)
                .netloc
                .lower()
            )

            if (
                resource_domain
                and resource_domain != page_domain
            ):
                external_resources += 1

    if len(resources) == 0:

        request_url = 1

    elif (
        external_resources / len(resources)
        > 0.5
    ):

        request_url = -1

    else:

        request_url = 1

    # --------------------------------------------------
    # 14. URL of Anchor
    # --------------------------------------------------

    external_anchors = 0

    for anchor in links:

        href = anchor.get("href")

        if href and href.startswith(
            ("http://", "https://")
        ):

            anchor_domain = (
                urlparse(href)
                .netloc
                .lower()
            )

            if (
                anchor_domain
                and anchor_domain != page_domain
            ):

                external_anchors += 1

    if len(links) == 0:

        url_of_anchor = 1

    elif (
        external_anchors / len(links)
        > 0.5
    ):

        url_of_anchor = -1

    else:

        url_of_anchor = 1

    # --------------------------------------------------
    # 15. Links in Meta, Script and Link tags
    # --------------------------------------------------

    tags = soup.find_all(
        ["meta", "script", "link"]
    )

    external_tag_links = 0
    total_tag_links = 0

    for tag in tags:

        link = (
            tag.get("href")
            or tag.get("src")
            or tag.get("content")
        )

        if link and link.startswith(
            ("http://", "https://")
        ):

            total_tag_links += 1

            tag_domain = (
                urlparse(link)
                .netloc
                .lower()
            )

            if (
                tag_domain
                and tag_domain != page_domain
            ):

                external_tag_links += 1

    if total_tag_links == 0:

        links_in_tags = 1

    elif (
        external_tag_links / total_tag_links
        > 0.5
    ):

        links_in_tags = -1

    else:

        links_in_tags = 1

    # --------------------------------------------------
    # 16. Server Form Handler (SFH)
    # --------------------------------------------------

    suspicious_forms = 0

    for form in forms:

        action = form.get(
            "action",
            ""
        ).strip()

        if action == "":
            suspicious_forms += 1

        elif action.lower() == "about:blank":
            suspicious_forms += 1

        elif action.startswith(
            ("http://", "https://")
        ):

            form_domain = (
                urlparse(action)
                .netloc
                .lower()
            )

            if (
                form_domain
                and form_domain != page_domain
            ):

                suspicious_forms += 1

    if len(forms) == 0:

        sfh = 1

    elif suspicious_forms > 0:

        sfh = -1

    else:

        sfh = 1

    # --------------------------------------------------
    # 17. Submitting Information to Email
    # --------------------------------------------------

    email_submission = False

    for form in forms:

        action = form.get(
            "action",
            ""
        ).lower()

        if "mailto:" in action:

            email_submission = True

    submitting_to_email = (
        -1 if email_submission
        else 1
    )

    # --------------------------------------------------
    # 18. Abnormal URL
    # --------------------------------------------------
    # Requires additional domain/WHOIS information.
    # We will improve this later.

    abnormal_url = 0

    # --------------------------------------------------
    # 19. Redirect
    # --------------------------------------------------

    redirect_count = len(
        response.history
    )

    if redirect_count >= 4:

        redirect_feature = -1

    else:

        redirect_feature = 1

    # --------------------------------------------------
    # 20. onMouseOver
    # --------------------------------------------------

    mouseover = (
        "onmouseover" in page_source
    )

    on_mouseover = (
        -1 if mouseover
        else 1
    )

    # --------------------------------------------------
    # 21. Right Click
    # --------------------------------------------------

    right_click_disabled = (
        "event.button==2" in page_source
        or "event.button == 2" in page_source
        or "contextmenu" in page_source
    )

    right_click = (
        -1 if right_click_disabled
        else 1
    )

    # --------------------------------------------------
    # 22. Pop-up Window
    # --------------------------------------------------

    popup = (
        "window.open" in page_source
        or "alert(" in page_source
    )

    popup_feature = (
        -1 if popup
        else 1
    )

    # --------------------------------------------------
    # 23. IFrame
    # --------------------------------------------------

    iframe_feature = (
        -1 if iframes
        else 1
    )

    # --------------------------------------------------
    # 24. Age of Domain
    # --------------------------------------------------
    # Requires WHOIS information.

    age_of_domain = 0

    # --------------------------------------------------
    # 25. DNS Record
    # --------------------------------------------------

    dns_record = 0

    # --------------------------------------------------
    # 26. Web Traffic
    # --------------------------------------------------
    # Requires external traffic information.

    web_traffic = 0

    # --------------------------------------------------
    # 27. Page Rank
    # --------------------------------------------------
    # Requires external information.

    page_rank = 0

    # --------------------------------------------------
    # 28. Google Index
    # --------------------------------------------------
    # Requires search engine information.

    google_index = 0

    # --------------------------------------------------
    # 29. Links Pointing to Page
    # --------------------------------------------------
    # Requires external backlink information.

    links_pointing_to_page = 0

    # --------------------------------------------------
    # 30. Statistical Report
    # --------------------------------------------------
    # Requires phishing database information.

    statistical_report = 0

    # ==================================================
    # FINAL 30 FEATURES
    # ==================================================

    features = {

        "having_IP_Address":
            -1 if has_ip else 1,

        "URL_Length":
            -1 if url_length >= 54 else 1,

        "Shortining_Service":
            -1 if is_shortened else 1,

        "having_At_Symbol":
            -1 if has_at else 1,

        "double_slash_redirecting":
            -1 if double_slash else 1,

        "Prefix_Suffix":
            -1 if has_prefix_suffix else 1,

        "having_Sub_Domain":
            subdomain_feature,

        "SSLfinal_State":
            ssl_feature,

        "Domain_registeration_length":
            domain_registration_length,

        "Favicon":
            favicon_feature,

        "port":
            port_feature,

        "HTTPS_token":
            https_token_feature,

        "Request_URL":
            request_url,

        "URL_of_Anchor":
            url_of_anchor,

        "Links_in_tags":
            links_in_tags,

        "SFH":
            sfh,

        "Submitting_to_email":
            submitting_to_email,

        "Abnormal_URL":
            abnormal_url,

        "Redirect":
            redirect_feature,

        "on_mouseover":
            on_mouseover,

        "RightClick":
            right_click,

        "popUpWidnow":
            popup_feature,

        "Iframe":
            iframe_feature,

        "age_of_domain":
            age_of_domain,

        "DNSRecord":
            dns_record,

        "web_traffic":
            web_traffic,

        "Page_Rank":
            page_rank,

        "Google_Index":
            google_index,

        "Links_pointing_to_page":
            links_pointing_to_page,

        "Statistical_report":
            statistical_report
    }

    return features