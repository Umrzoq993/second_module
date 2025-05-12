import requests

url = "https://kun.uz"

try:
    response = requests.get(url)
    html_code = response.text
    print("HTML kod yuklandi!")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

start_tag = "<title>"
end_tag = "</title>"

start_index = html_code.find(start_tag) + len(start_tag)
end_index = html_code.find(end_tag)

if start_index != -1 and end_index != -1:
    title_text = html_code[start_index:end_index]
    print("Title tegi ichidagi matn:", title_text.strip())
else:
    print("Title tegi topilmadi.")
