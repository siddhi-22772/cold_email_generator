import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+?>', '', text)

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)

    # Trim leading and trailing whitespace
    text = text.strip()

    # Remove extra whitespace
    text = ' '.join(text.split())

    return text


# # Example
# text = "<p>Hello! Visit https://example.com for more information.</p>"
# cleaned_text = clean_text(text)

# print(cleaned_text)