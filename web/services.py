import requests


def retrieve_starships(url):
    """Calls API to retrieve starships

    Args:
        url:

    Returns:
        (tuple):
            starships (list): A list of starships
            next_page (str): Next page to retrieve
        False if not successful
    """
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        starships = data["results"]
        next_page = data["next"]
        return starships, next_page
    return False
