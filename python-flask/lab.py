import requests
import json


def get(url, verify=True):
    """
    GET API client function that performs HTTP GET when passed appropriate arguments
    :param url: - the full URL of target and URI
    :param headers: - JSON representation of header dictionary object
    :param verify: Boolean value to perform strict certificate checks
    :return: returns the payload of the request
    """
    data = requests.get(url=url, verify=verify)
    if data.status_code == 200:
        return data


def post(url, data={}, verify=True):
    """
    POST API client function that performs HTTP POST when passed appropriate arguments
    :param url: - the full URL of target and URI
    :param headers: - JSON representation of header dictionary object
    :param data: - JSON representation of payload dictionary object
    :param verify: Boolean value to perform strict certificate checks
    :return: returns the payload of the request
    """
    data = requests.post(url=url, data=json.dumps(data), verify=verify)
    if data.status_code == 201:
        return data


def put(url, data={}, verify=True):
    """
    PUT API client function that performs HTTP PUT when passed appropriate arguments
    :param url: - the full URL of target and URI
    :param headers: - JSON representation of header dictionary object
    :param data: - JSON representation of payload dictionary object
    :param verify: Boolean value to perform strict certificate checks
    :return: returns the payload of the request
    """
    data = requests.put(url=url, data=data, verify=verify)
    if data.status_code == 200:
        return data


def delete(url, verify=True):
    """
    DELETE API client function that performs HTTP DELETE when passed appropriate arguments
    :param url: - the full URL of target and URI
    :param headers: - JSON representation of header dictionary object
    :param verify: Boolean value to perform strict certificate checks
    :return: returns the payload of the request
    """
    data = requests.delete(url=url, verify=verify)
    if data.status_code == 200:
        return data


new_user = {
    'id': 11,
    'name': 'Sandeep Seeram',
    'email': '*******@microsoft.com'
}


update_user = {
    'id': 4,
    'phone': '1-9550-486-4571',
}


if __name__ == '__main__':
    """
     Simple logic to determine if this script is being run directly, will not execute if imported by another script
    """
    full_url = 'https://jsonplaceholder.typicode.com/users'
    get_resp = get(full_url)
    get_data = json.loads(get_resp.content)
    for g in get_data:
        if g['id'] == 4:
            print(str(g))
            break
    print(post(full_url, data=new_user).json())
    print(put(full_url + '/4', data=update_user).json())
    print(delete(full_url + '/6').json())