import os
import requests
from urllib.parse import urlparse

def download_images(query, num_images, folder):
    # Cria a pasta se ela não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # URL da API do Unsplash
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={num_images}"

    # Substitua YOUR_ACCESS_KEY pelo seu próprio access key do Unsplash
    headers = {
        "Authorization": "Client-ID 7tGmCuu6nyd1nZd0WZdXM84nvzTRa1EH_9ziL4MNkCw"
    }

    # Faz a requisição à API
    response = requests.get(url, headers=headers)
    data = response.json()

    # Baixa as imagens
    for i, img in enumerate(data['results']):
        img_url = img['urls']['regular']
        img_extension = os.path.splitext(urlparse(img_url).path)[1]
        img_path = os.path.join(folder, f"{query}_{i+1}{img_extension}")

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(img_path, 'wb') as file:
                file.write(img_response.content)
            print(f"Downloaded: {img_path}")
        else:
            print(f"Failed to download: {img_url}")

# Baixa 50 imagens de gatos
download_images("cat", 50, "dataset/cat")