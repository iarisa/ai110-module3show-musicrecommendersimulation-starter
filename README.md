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

```
# e.g.:
# User profile: Lofi Chill
# favorite_genre=lofi, favorite_mood=chill, target_energy=0.3, target_valence=0.7, target_danceability=0.6

Top recommendations:

1. Library Rain by Paper Lanterns — Score: 5.91
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.05 (+0.66)
     - valence diff 0.10 (+0.45)
     - danceability diff 0.02 (+0.29)

2. Midnight Coding by LoRoom — Score: 5.84
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.12 (+0.62)
     - valence diff 0.14 (+0.43)
     - danceability diff 0.02 (+0.29)

3. Focus Flow by LoRoom — Score: 4.38
     - genre match (+3.0)
     - mood mismatch (+0.0)
     - energy diff 0.10 (+0.63)
     - valence diff 0.11 (+0.45)
     - danceability diff 0.00 (+0.30)

4. Spacewalk Thoughts by Orbit Bloom — Score: 2.90
     - genre mismatch (+0.0)
     - mood match (+1.5)
     - energy diff 0.02 (+0.69)
     - valence diff 0.05 (+0.48)
     - danceability diff 0.19 (+0.24)

5. Coffee Shop Stories by Slow Stereo — Score: 1.43
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.07 (+0.65)
     - valence diff 0.01 (+0.49)
     - danceability diff 0.06 (+0.28)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

### Different User Profiles

#### High-Energy Pop

```
Top recommendations:

1. Gym Hero by Max Pulse — Score: 5.96
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.03 (+0.68)
     - valence diff 0.03 (+0.48)
     - danceability diff 0.03 (+0.29)

2. Sunrise City by Neon Echo — Score: 4.41
     - genre match (+3.0)
     - mood mismatch (+0.0)
     - energy diff 0.08 (+0.64)
     - valence diff 0.04 (+0.48)
     - danceability diff 0.06 (+0.28)

3. Storm Runner by Voltline — Score: 2.78
     - genre mismatch (+0.0)
     - mood match (+1.5)
     - energy diff 0.01 (+0.69)
     - valence diff 0.32 (+0.34)
     - danceability diff 0.19 (+0.24)

4. Pulse Horizon by Kinetic Sol — Score: 1.41
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.05 (+0.67)
     - valence diff 0.08 (+0.46)
     - danceability diff 0.05 (+0.28)

5. Rooftop Lights by Indigo Parade — Score: 1.39
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.14 (+0.60)
     - valence diff 0.01 (+0.49)
     - danceability diff 0.03 (+0.29)
```

#### Mellow Acoustic

```
Top recommendations:

1. Moonlight Fragments by Elena Voss — Score: 5.97
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.02 (+0.69)
     - valence diff 0.00 (+0.50)
     - danceability diff 0.05 (+0.28)

2. Spacewalk Thoughts by Orbit Bloom — Score: 1.21
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.08 (+0.64)
     - valence diff 0.35 (+0.32)
     - danceability diff 0.21 (+0.24)

3. Wildflower Roads by Callum Hart — Score: 1.14
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.25 (+0.52)
     - valence diff 0.25 (+0.38)
     - danceability diff 0.20 (+0.24)

4. Library Rain by Paper Lanterns — Score: 1.13
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.15 (+0.59)
     - valence diff 0.30 (+0.35)
     - danceability diff 0.38 (+0.19)

5. Focus Flow by LoRoom — Score: 1.09
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.20 (+0.56)
     - valence diff 0.29 (+0.35)
     - danceability diff 0.40 (+0.18)
```

#### Dance Party

```
Top recommendations:

1. Pulse Horizon by Kinetic Sol — Score: 5.99
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.00 (+0.70)
     - valence diff 0.02 (+0.49)
     - danceability diff 0.00 (+0.30)

2. Gym Hero by Max Pulse — Score: 1.42
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.02 (+0.69)
     - valence diff 0.13 (+0.43)
     - danceability diff 0.02 (+0.29)

3. Sunrise City by Neon Echo — Score: 1.35
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.13 (+0.61)
     - valence diff 0.06 (+0.47)
     - danceability diff 0.11 (+0.27)

4. Rooftop Lights by Indigo Parade — Score: 1.30
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.19 (+0.57)
     - valence diff 0.09 (+0.46)
     - danceability diff 0.08 (+0.28)

5. Concrete Throne by Kilo Vance — Score: 1.23
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.17 (+0.58)
     - valence diff 0.28 (+0.36)
     - danceability diff 0.05 (+0.28)
```

#### Conflicting Lofi (chill mood, high energy target)

```
Top recommendations:

1. Midnight Coding by LoRoom — Score: 5.59
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.48 (+0.36)
     - valence diff 0.14 (+0.43)
     - danceability diff 0.02 (+0.29)

2. Library Rain by Paper Lanterns — Score: 5.56
     - genre match (+3.0)
     - mood match (+1.5)
     - energy diff 0.55 (+0.31)
     - valence diff 0.10 (+0.45)
     - danceability diff 0.02 (+0.29)

3. Focus Flow by LoRoom — Score: 4.09
     - genre match (+3.0)
     - mood mismatch (+0.0)
     - energy diff 0.50 (+0.35)
     - valence diff 0.11 (+0.45)
     - danceability diff 0.00 (+0.30)

4. Spacewalk Thoughts by Orbit Bloom — Score: 2.48
     - genre mismatch (+0.0)
     - mood match (+1.5)
     - energy diff 0.62 (+0.27)
     - valence diff 0.05 (+0.48)
     - danceability diff 0.19 (+0.24)

5. Storm Runner by Voltline — Score: 1.36
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.01 (+0.69)
     - valence diff 0.22 (+0.39)
     - danceability diff 0.06 (+0.28)
```

#### Sad + High Energy (conflicting)

```
Top recommendations:

1. Iron Cathedral by Grimhold — Score: 4.34
     - genre match (+3.0)
     - mood mismatch (+0.0)
     - energy diff 0.07 (+0.65)
     - valence diff 0.22 (+0.39)
     - danceability diff 0.00 (+0.30)

2. Moonlight Fragments by Elena Voss — Score: 2.35
     - genre mismatch (+0.0)
     - mood match (+1.5)
     - energy diff 0.68 (+0.22)
     - valence diff 0.20 (+0.40)
     - danceability diff 0.25 (+0.22)

3. Storm Runner by Voltline — Score: 1.22
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.01 (+0.69)
     - valence diff 0.38 (+0.31)
     - danceability diff 0.26 (+0.22)

4. Night Drive Loop by Neon Echo — Score: 1.10
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.15 (+0.59)
     - valence diff 0.39 (+0.30)
     - danceability diff 0.33 (+0.20)

5. Concrete Throne by Kilo Vance — Score: 1.02
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.12 (+0.62)
     - valence diff 0.52 (+0.24)
     - danceability diff 0.45 (+0.17)
```

#### Nonexistent Category (opera/furious)

```
Top recommendations:

1. Wildflower Roads by Callum Hart — Score: 1.41
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.05 (+0.66)
     - valence diff 0.05 (+0.47)
     - danceability diff 0.10 (+0.27)

2. Midnight Coding by LoRoom — Score: 1.38
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.08 (+0.64)
     - valence diff 0.06 (+0.47)
     - danceability diff 0.12 (+0.26)

3. Velvet Static by Nadia Cole — Score: 1.37
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.00 (+0.70)
     - valence diff 0.18 (+0.41)
     - danceability diff 0.12 (+0.26)

4. Focus Flow by LoRoom — Score: 1.35
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.10 (+0.63)
     - valence diff 0.09 (+0.46)
     - danceability diff 0.10 (+0.27)

5. Library Rain by Paper Lanterns — Score: 1.32
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy diff 0.15 (+0.59)
     - valence diff 0.10 (+0.45)
     - danceability diff 0.08 (+0.28)
```

### Weight Change: Genre Halved (3.0 → 1.5), Energy Doubled (0.7 → 1.4)

Ran all 7 profiles with `genre` weight cut in half and `energy` weight doubled (max possible raw score dropped from 6.0 to 5.2). 

Effects:
- "Nonexistent Category" profile (`opera`/`furious`, neither of which exist in the catalog): since every song already loses all categorical points regardless of weight, the ranking is purely numeric. Wildflower Roads and Velvet Static landed in a near-tie at the top (~2.07 each) since they had the closest energy values to the 0.5 target. With the original weights energy had less pull relative to valence/danceability.

- Top picks for cleanly-matched profiles (Lofi Chill, High-Energy Pop, Mellow Acoustic, Dance Party) didn't change rank order, since the #1 song in each already matched both genre and mood. Halving genre's weight just compressed the score gap between the runner-ups.

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



