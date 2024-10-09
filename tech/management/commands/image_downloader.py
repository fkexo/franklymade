
from django.core.files.base import ContentFile
import requests



def save_image_from_url(image_url, model_instance):
    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        if response.status_code == 200:
            # Extract a valid filename from the URL
            image_name = image_url.split("/")[-1]
            if len(image_name) > 200:  # Handle long image names
                image_name = image_name[:49]

            # Save the file to the S3 bucket using the ImageField
            model_instance.news_image.save(image_name, ContentFile(response.content), save=False)
        else:
            print(f"Failed to retrieve image from {image_url}")
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None







# def save_image_from_url(image_url, model_instance):
#     try:
#         # Fetch the image
#         image_response = requests.get(image_url)

#         if image_response.status_code == 200:
#             # Extract filename from the URL (or generate one if too long)
#             image_name = image_url.split("/")[-1]
#             if len(image_name) > 200:
#                 image_name = image_name[:200]  # Truncate if necessary
            
#             # Convert to file-like object
#             image_content = ContentFile(image_response.content)
            
#             # Save image to model's image field (use your model field for images)
#             model_instance.news_image.save(image_name, image_content, save=True)
#         else:
#             print(f"Failed to retrieve image from {image_url}")
#     except Exception as e:
#         print(f"Error saving image: {e}")

# # Call this function in your scraping code where you're handling image URLs
# # save_image_from_url(image_url, news_instance)
