"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    lofi_chill_user = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.3,
        "target_valence": 0.7,
        "target_danceability": 0.6,
    }
    
    high_energy_pop_user = {
        "favorite_genre": "pop",
        "favorite_mood": "intense",
        "target_energy": 0.9,
        "target_valence": 0.8,
        "target_danceability": 0.85,
    }

    mellow_acoustic_user = {
        "favorite_genre": "classical",
        "favorite_mood": "melancholy",
        "target_energy": 0.2,
        "target_valence": 0.3,
        "target_danceability": 0.2,
    }

    dance_party_user = {
        "favorite_genre": "edm",
        "favorite_mood": "euphoric",
        "target_energy": 0.95,
        "target_valence": 0.9,
        "target_danceability": 0.9,
    }

    conflicting_lofi_user = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.9,
        "target_valence": 0.7,
        "target_danceability": 0.6,
    }

    sad_high_energy_user = {
        "favorite_genre": "metal",
        "favorite_mood": "melancholy",
        "target_energy": 0.9,
        "target_valence": 0.1,
        "target_danceability": 0.4,
    }

    nonexistent_category_user = {
        "favorite_genre": "opera",
        "favorite_mood": "furious",
        "target_energy": 0.5,
        "target_valence": 0.5,
        "target_danceability": 0.5,
    }

    user_profiles = {
        "Lofi Chill": lofi_chill_user,
        "High-Energy Pop": high_energy_pop_user,
        "Mellow Acoustic": mellow_acoustic_user,
        "Dance Party": dance_party_user,
        "Conflicting Lofi (chill mood, high energy target)": conflicting_lofi_user,
        "Sad + High Energy (conflicting)": sad_high_energy_user,
        "Nonexistent Category (opera/furious)": nonexistent_category_user,
    }

    for profile_name, profile in user_profiles.items():
        recommendations = recommend_songs(profile, songs, k=5)

        print(f"\n=== {profile_name} ===")
        print("\nTop recommendations:\n")
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} by {song['artist']} — Score: {score:.2f}")
            for reason in explanation.split(", "):
                print(f"     - {reason}")
            print()


if __name__ == "__main__":
    main()
