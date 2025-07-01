from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """
    Extrait l'ID d'une vidéo YouTube à partir de son URL.
    Exemple d'URL : https://www.youtube.com/watch?v=abcdef12345
    """
    import re
    # Cherche la chaîne après "v="
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    # Cas URL courte youtu.be/abcdef12345
    match = re.search(r"youtu\.be/([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    raise ValueError("ID vidéo introuvable dans l'URL.")

def save_transcript(video_url, filename):
    video_id = get_video_id(video_url)
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # On concatène tous les textes
        full_text = ""
        for entry in transcript_list:
            full_text += entry['text'] + "\n"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Sous-titres enregistrés dans '{filename}'")
    except Exception as e:
        print("Erreur lors de la récupération des sous-titres :", e)

if __name__ == "__main__":
    url = input("Entrez l'URL de la vidéo YouTube : ")
    save_transcript(url, "transcript.txt")
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """
    Extrait l'ID d'une vidéo YouTube à partir de son URL.
    Exemple d'URL : https://www.youtube.com/watch?v=abcdef12345
    """
    import re
    # Cherche la chaîne après "v="
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    # Cas URL courte youtu.be/abcdef12345
    match = re.search(r"youtu\.be/([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    raise ValueError("ID vidéo introuvable dans l'URL.")

def save_transcript(video_url, filename):
    video_id = get_video_id(video_url)
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # On concatène tous les textes
        full_text = ""
        for entry in transcript_list:
            full_text += entry['text'] + "\n"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Sous-titres enregistrés dans '{filename}'")
    except Exception as e:
        print("Erreur lors de la récupération des sous-titres :", e)

if __name__ == "__main__":
    url = input("Entrez l'URL de la vidéo YouTube : ")
    save_transcript(url, "transcript.txt")

