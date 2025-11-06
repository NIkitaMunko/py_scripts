import requests

def main():
    url = "http://localhost:3087/commands"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print("Відповідь сервера:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Помилка при запиті: {e}")

if __name__ == "__main__":
    main()
