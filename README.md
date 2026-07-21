# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

In the real world, music recommender systems use both collaborative filtering and content-based filtering. The collaborative filtering method involves using data (e.g. liked songs, skipped songs) from listeners with a similar music taste to generate recommendations for listeners. This helps listeners find songs that they may not have heard already but will likely enjoy. The content-based filtering method involves using a song's features in isolation (e.g. genre, tempo, energy) and recommending songs that have similar attributes. This helps when there isn't enough data to compare listening behaviors across users. My version will prioritize the content-based filtering system since the available data contains attributes about each songs rather than other users' listening behavior. It will use the following:

`Song` features:
- genre
- mood
- energy
- valence
- danceability

`UserProfile` features:
- favorite_genre
- favorite_mood
- target_energy
- target_valence
- target_danceability

My `Recommender` will use the following weight-based point system to score each song against the `UserProfile` preferences:
- genre: 3
- mood: 1.5
- energy: 0.7
- valence: 0.5
- danceability: 0.3

Genre and mood will get the full points for exact matches, while the remaining features will be computed numerically by the function `weight * (1 - abs(song_value - target_value))`. The raw score (max possible = 6) is then normalized to a 0-100 scale for display.

Some biases could occur since genre and mood make up 4.5 of the possible points, so songs that are closer in the other areas (e.g. energy, valence, danceability) do not have as much impact. This could cause listeners to only be exposed to songs within their genre and mood. Also, if a genre or mood does not match exactly, then it will lose all points instead of being weighed partially (e.g. "hip hop" doesn't equal "rap" but they are very similar).

Some prompts to answer:

- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



