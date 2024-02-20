import requests

def search_google_images(api_key, cse_id, search_query, num_results=1):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_query,
        'cx': cse_id,
        'key': api_key,
        'searchType': 'image',
        'num': num_results
    }

    response = requests.get(search_url, params=params)

    # 할당량 초과 에러 처리
    if response.status_code == 429:
        print("Error: 사용량이 할당량을 초과하였습니다.")
        return []
    elif response.status_code != 200:
        print(f"Error: 요청 처리 중 오류가 발생하였습니다. (HTTP 상태 코드: {response.status_code})")
        return []

    result = response.json()

    images = []
    if 'items' in result:
        for item in result['items']:
            images.append(item['link'])

    return images