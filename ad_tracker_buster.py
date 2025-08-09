import requests

def remove_tracking(url):
    """Remove parâmetros de rastreamento comuns de URLs"""
    tracked_params = [
        "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", 
        "fbclid", "gclid", "msclkid", "ref", "dclid"
    ]

    # Separar a URL e os parâmetros
    url_parts = url.split("?", 1)
    if len(url_parts) == 1:
        return url  # Retorna a URL sem parâmetros

    base_url, query_string = url_parts
    params = query_string.split("&")

    # Filtra os parâmetros de rastreamento
    filtered_params = [
        param for param in params if not any(param.startswith(p) for p in tracked_params)
    ]

    # Reconstruir a URL sem os parâmetros de rastreamento
    clean_url = base_url + ("?" + "&".join(filtered_params) if filtered_params else "")
    return clean_url

def test_clean_url():
    url = "https://example.com/?utm_source=google&utm_medium=cpc&gclid=abc123"
    clean = remove_tracking(url)
    print(f"URL original: {url}")
    print(f"URL limpa: {clean}")

if __name__ == "__main__":
    test_clean_url()
