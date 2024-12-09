from bing_image_downloader import downloader

def download_images(query, limit, output_dir):
    downloader.download(query, limit=limit, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)

# Baixar imagens de cães
download_images("dog", 200, "dataset")

# Baixar imagens de gatos
download_images("cat", 200, "dataset")

print("Download concluído!")