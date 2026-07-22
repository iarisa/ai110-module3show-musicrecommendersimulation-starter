import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: float = 0.5
    target_danceability: float = 0.5

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads song data from a CSV file into a list of dicts with numeric fields converted to int/float."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences using weighted genre/mood matches and numeric feature closeness."""
    weights = {
        "genre": 3.0,
        "mood": 1.5,
        "energy": 0.7,
        "valence": 0.5,
        "danceability": 0.3,
    }

    score = 0.0
    reasons = []

    categorical_features = [
        ("genre", "favorite_genre"),
        ("mood", "favorite_mood"),
    ]
    for feature, pref_key in categorical_features:
        if song[feature] == user_prefs.get(pref_key):
            reasons.append(f"{feature} match (+{weights[feature]:.1f})")
            score += weights[feature]
        else:
            reasons.append(f"{feature} mismatch (+0.0)")

    numeric_features = [
        ("energy", "target_energy", None),
        ("valence", "target_valence", 0.5),
        ("danceability", "target_danceability", 0.5),
    ]
    for feature, target_key, default in numeric_features:
        target = user_prefs[target_key] if default is None else user_prefs.get(target_key, default)
        diff = abs(song[feature] - target)
        points = weights[feature] * (1 - diff)
        reasons.append(f"{feature} diff {diff:.2f} (+{points:.2f})")
        score += points

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, sorted by score descending."""
    scored_songs = ((song, *score_song(user_prefs, song)) for song in songs)
    songs_with_joined_reasons = [(song, score, ", ".join(reasons)) for song, score, reasons in scored_songs]
    return sorted(songs_with_joined_reasons, key=lambda entry: entry[1], reverse=True)[:k]
