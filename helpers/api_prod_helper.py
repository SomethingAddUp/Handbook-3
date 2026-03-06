import requests
import time

def send_request(method, url, payload, timeout = 10, retries = 3, sec = 2):
    session = requests.Session()
    method = method.upper()
    for attempt in range(retries):
        try:
            response = session.request( method = method,
                                         url = url,
                                        json = payload,
                                        timeout = timeout )
            if response.status_code >= 500 and attempt < retries - 1:
                time.sleep(sec)
                continue
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(sec)
                continue
            else:
                raise e
    raise Exception(f"Failed to send {method} request to {url} after {retries} retries")

def http_error_code(response):
    http_message = {
                        400: "Bad Request\nPlease check your input",
                        401: "Unauthorized\nInvalid API key",
                        403: "Forbidden\nAccess denied",
                        404: "Not Found\nCity not found",
                        500: "Internal Server Error\nPlease try again later",
                        502: "Bad Gateway\nInvalid response from the server",
                        503: "Service Unavailable\nServer is down",
                        504: "Gateway Timeout\nNo response from the server" ,            }

    return http_message.get(response.status_code, "HTTP error occurred")

def emoji(emoji_code):
    if 200 <= emoji_code <= 232:
        return "⛈️"
    elif 300 <= emoji_code <= 321:
        return "🍃"
    elif 500 <= emoji_code <= 531:
        return "🌧️"
    elif 600 <= emoji_code <= 622:
        return "❄️"
    elif 701 <= emoji_code <= 741:
        return "🌫️"
    elif emoji_code == 762:
        return "🌋"
    elif emoji_code == 781:
        return "🌪️"
    elif emoji_code == 800:
        return "☀️"
    elif 801 <= emoji_code <= 804:
        return "☁️"
    else:
        return "🔴"