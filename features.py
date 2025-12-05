import re
import numpy as np
from urllib.parse import urlparse
import urllib.parse

# F1: URL Length
def url_length(url):
    return np.int64(len(url))

# F2: Number of dots in URL
def number_of_dots_in_url(url):
    return np.int64(len(re.findall(r'\.', url)))

# F3: Having repeated digits in URL (e.g., "2233" as True)
def having_repeated_digits_in_url(url):
    return np.int64(1 if re.search(r'(\d)\1', url) else 0)

# F4: Number of digits in URL
def number_of_digits_in_url(url):
    return np.int64(len(re.findall(r'\d', url)))

# F5: Number of special characters in URL (e.g., "#", "$", "%", "&", "~")
def number_of_special_char_in_url(url):
    return np.int64(len(re.findall(r'[^\w\s]', url)))

# F6: Number of hyphens in URL
def number_of_hyphens_in_url(url):
    return np.int64(len(re.findall(r'-', url)))

# F7: Number of underscores in URL
def number_of_underline_in_url(url):
    return np.int64(len(re.findall(r'_', url)))

# F8: Number of slashes ("/" or "\") in URL
def number_of_slash_in_url(url):
    return np.int64(len(re.findall(r'[\\/]', url)))

# F9: Number of question marks in URL
def number_of_questionmark_in_url(url):
    return np.int64(len(re.findall(r'\?', url)))

# F10: Number of equal signs in URL
def number_of_equal_in_url(url):
    return np.int64(len(re.findall(r'=', url)))

# F11: Number of "@" symbols in URL
def number_of_at_in_url(url):
    return np.int64(len(re.findall(r'@', url)))

# F12: Number of dollar signs in URL
def number_of_dollar_sign_in_url(url):
    return np.int64(len(re.findall(r'\$', url)))

# F13: Number of exclamation marks in URL
def number_of_exclamation_in_url(url):
    return np.int64(len(re.findall(r'!', url)))

# F14: Number of hashtags in URL
def number_of_hashtag_in_url(url):
    return np.int64(len(re.findall(r'#', url)))

# F15: Number of percent signs in URL
def number_of_percent_in_url(url):
    return np.int64(len(re.findall(r'%', url)))

# F16: Domain length (assuming domain is extracted)
def domain_length(url):
    # Parse the URL to extract the domain
    parsed_url = urlparse(url)

    # Get the domain (netloc is the part of the URL that contains the domain)
    domain = parsed_url.netloc

    # Return the length of the domain
    return np.int64(len(domain))

# F17: Number of dots in domain
def number_of_dots_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc

    # Count dots in the domain name
    dot_count = domain_name.count('.')
    return np.int64(dot_count)

# F18: Number of hyphens in domain
def number_of_hyphens_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc

    # Count hyphens in the domain name and cast to int64
    hyphen_count = np.int64(domain_name.count('-'))
    return hyphen_count

# F19: Having special characters in domain (e.g., "*", "!", "#", "$", "%", "&", "~")
def having_special_characters_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc

    # Check for special characters in the domain and cast to int64
    has_special_chars = np.int64(any(c.isalpha() or c.isdigit() for c in domain_name))
    return has_special_chars

# F20: Number of special characters in domain
def number_of_special_characters_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc

    special_char_count = 0
    for char in domain_name:
        if not char.isalnum():  # Check if character is not alphanumeric
            special_char_count += 1
    return np.int64(special_char_count)

# F21: Having digits in domain
def having_digits_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    return np.int64(1 if any(char.isdigit() for char in domain_name) else 0)

# F22: Number of digits in domain
def number_of_digits_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    return np.int64(sum(char.isdigit() for char in domain_name))

# F23: Having repeated digits in domain
def having_repeated_digits_in_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    return np.int64(1 if any(char in domain_name for char in set(domain_name) if char.isdigit() and domain_name.count(char) > 1) else 0)

# F24: Number of subdomains (assuming splitting by dots)
def number_of_subdomains(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    subdomains = domain_name.split('.')[:-2]
    return np.int64(len(subdomains))

# F25: Having dot in subdomain
def having_dot_in_subdomain(url):
    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)

    # Split the netloc into parts (subdomain, domain, and TLD)
    netloc_parts = parsed_url.netloc.split('.')

    # If the length is greater than 2, it's likely that there is a subdomain
    # Netloc should have at least 3 parts: subdomain, domain, and TLD
    if len(netloc_parts) > 2:
        subdomain = '.'.join(netloc_parts[:-2])  # Everything before the main domain and TLD
        # Check if there is a dot in the subdomain
        return np.int64(1 if '.' in subdomain else 0)
    else:
        # No subdomain found
        return np.int64(0)

# F26: Having hyphen in subdomain
def having_hyphen_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(1 if any('-' in subdomain for subdomain in subdomains) else 0)

# F27: Average subdomain length
def average_subdomain_length(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(sum(len(subdomain) for subdomain in subdomains) / len(subdomains) if subdomains else 0)

# F28: Average number of dots in subdomain
def average_number_of_dots_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    netloc_parts = parsed_url.netloc.split('.')

    # If the length is greater than 2, we have subdomains
    if len(netloc_parts) > 2:
        subdomain = '.'.join(netloc_parts[:-2])  # Everything before domain and TLD
        dot_count = subdomain.count('.')  # Count dots in the subdomain
        return np.float64(dot_count)

    # If no subdomains, return 0
    return np.float64(0)


# F29: Average number of hyphens in subdomain
def average_number_of_hyphens_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    if subdomains:
        total_hyphens = sum(subdomain.count('-') for subdomain in subdomains)
        return np.int64(total_hyphens / len(subdomains))
    else:
        return np.int64(0)  # No subdomains, return 0

# F30: Having special characters in subdomain
def having_special_characters_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(1 if any(re.search(r'[!#$%&~]', subdomain) for subdomain in subdomains) else 0)

# F31: Number of special characters in subdomain
def number_of_special_characters_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(sum(len(re.findall(r'[!#$%&~]', subdomain)) for subdomain in subdomains))

# F32: Having digits in subdomain
def having_digits_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(1 if any(re.search(r'\d', subdomain) for subdomain in subdomains) else 0)

# F33: Number of digits in subdomain
def number_of_digits_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    subdomains = parsed_url.netloc.split('.')[:-2]
    return np.int64(sum(len(re.findall(r'\d', subdomain)) for subdomain in subdomains))

# F34: Having repeated digits in subdomain
def having_repeated_digits_in_subdomain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    return np.int64(1 if re.search(r'(\d)\1', domain_name) else 0)  # Check entire domain name

# F35: Having path
def having_path(url):
    # Check if there is a path (after the domain)
    path_part = url.split('//')[-1].split('?')[0].split('#')[0]  # Extract up to query or fragment
    return np.int64(1 if '/' in path_part and path_part != '' else 0)

# F36: Path length
def path_length(url):
    path = re.search(r'//[^/]+(/.*)', url)
    return np.int64(len(path.group(1)) if path else 0)

# F37: Having query
def having_query(url):
    return np.int64(1 if '?' in url else 0)

# F38: Having fragment
def having_fragment(url):
    return np.int64(1 if '#' in url else 0)

# F39: Having anchor
def having_anchor(url):
    return np.int64(1 if re.search(r'#.*', url) is not None else 0)

# F40: Entropy of URL (Shannon entropy calculation)
from math import log2
def entropy_of_url(url):
    if len(url) == 0:
        return np.float64(0)  # Return 0 entropy for empty URLs
    prob = [float(url.count(c)) / len(url) for c in set(url)]
    return np.float64(-sum([p * log2(p) for p in prob]))

# F41: Entropy of Domain
def entropy_of_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain_name = parsed_url.netloc
    if len(domain_name) == 0:
        return np.float64(0)  # Return 0 entropy for empty domains
    prob = [float(domain_name.count(c)) / len(domain_name) for c in set(domain_name)]
    return np.float64(-sum([p * log2(p) for p in prob]))

# F42: Protocl of a url
def check_protocol(url):
  parsed_url = urllib.parse.urlparse(url)
  if parsed_url.scheme == 'https':
    return 0
  elif parsed_url.scheme == 'http':
    return 1
  else:
    return -1  # For unknown or invalid protocols
# F43: Check if url ends with .html

def is_html_url(url):
  return 1 if url.lower().endswith('.html') or url.lower().endswith('.html/') or url.lower().endswith('.php') or url.lower().endswith('.php/') else 0

# F44: Check the presence of hihgly used phising TLDs
def has_unusual_tld(url):    
  parsed_url = urllib.parse.urlparse(url)
  tld = parsed_url.netloc.split('.')[-1]
  suspect_tlds = [".xyz", ".top", ".club", ".work", ".online", ".site", ".win", ".racing", ".date", ".space", ".download", ".link", ".pro", ".tech", ".pw", ".info", ".cc", ".tk", ".ml", ".ga", ".cf", ".gq", ".cn", ".co", ".io", ".me", ".gov"]
  return 1 if tld.lower() in suspect_tlds else 0

# F45: Check the presence of highly used suspisious words in phishing urls
def contains_suspicious_words(url):
    suspicious_words = [
    "login", "account", "secure", "update", "verify", "password", "bank", 
    "payment", "credentials", "support", "confirm", "help", "claim", 
    "customer", "service", "thanks", "app", "securelogin", "signup", 
    "activation", "confirm", "submit", "withdraw", "invoice", "receipt", 
    "paypal", "transfer", "alert", "reward", "security", "verify", 
    "check", "gift", "social", "creditcard", "webmail", "affiliate", 
    "disclaimer", "protected", "doc", "file", "important", "warning", 
    "email", "login", "verify", "promo", "free", "reward", "lottery", 
    "unsubscribe", "urgent", "download", "banking", "myaccount", 
    "confirm", "click", "offer", "clickhere", "passwordreset", 
    "serviceupdate", "newuser", "confidential", "confirms", "activation", 
    "checkyourbalance", "accountupdate", "securityalert", "logininfo", 
    "change", "systemalert", "verifyaccount", "newpassword", "securelogin"
    ]

    url = url.lower()  # Convert URL to lowercase for case-insensitive matching
    for word in suspicious_words:
        if word in url:
            return 1
    return 0
