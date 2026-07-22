# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**PutMeOn 1.0**  


## 2. Intended Use  

**PutMeOn 1.0** recommends songs that match your taste. Give it your favorite genre and mood, plus how energetic, positive, and danceable you like your music. This recommender will score each song and give you the top 5 songs you should listen to next! This recommender is used on a sample predefined song catalog and is intended for classroom exploration only.


## 3. How the Model Works  

Every song gets scored against what you're looking for, and the recommendations show the top 5 songs ranked. 

The score uses genre, mood, energy, valence (song's upbeatness/positivity), and danceability. If a song's genre matches your favorite genre exactly, it gets 3 points. If a song's mood matches your favorite mood exactly, it gets 1.5 points. Otherwise, the song gets 0 points each.

Energy, valence, and danceability don't use exact matches, but instead use how close they are to your preferences. The number of points a song earns is determined by how far off it is from your preference value (absolute not raw). Energy can add up to 0.7 points, valence up to 0.5, and danceability up to 0.3.

All these points get added together into one final score. Songs are sorted from highest score to lowest, and the top 5 songs are recommended.


## 4. Data  

The catalog has 18 songs, each tagged with one genre, one mood, and four numeric traits: energy, tempo, valence (positivity), danceability, and acousticness.

There are 15 genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, hip hop, folk, edm, country, r&b, metal, reggae.

There are 14 moods: happy, chill, intense, relaxed, moody, focused, melancholy, confident, nostalgic, euphoric, hopeful, romantic, aggressive, playful.

The original dataset had 10 songs, but 8 more were added to introduce more variety. The dataset does not include the following parts of musical taste: vocals/instrumental distinction, lagnuage, era, or potential genre ovelaps. 

## 5. Strengths 

The recommender works best for users with clear, well-defined preferences that map onto genres already in the catalog. The weighted scoring system also captures a pattern that seems right: when a user's energy preference contradicts their genre, the recommender still leans toward genre/mood match. Since genre (3.0) and mood (1.5) outweigh energy (0.7), a user's stated genre/mood identity reliably wins out over a slightly-off numeric target, which feels like the right priority.

## 6. Limitations and Bias 

I noticed that my system does not give some sort of adjacency credit when considering the user's favorite genre. For example, if a user's favorite genre is "rap" and the song's genre is "hip hop," it would not get any genre match points even though these are similar. The same thing would happen if someone's favorite genre is "indie pop" and a song's genre is "pop"; my recommender doesn't consider the substring match.

## 7. Evaluation  

I tested the following user profiles: Lofi Chill, High-Energy Pop, Mellow Acoustic, Dance Party, Conflicting Lofi, Sad + High Energy (conflicting), and Nonexistent Category (opera/furious). I was most surprised about the Nonexistent Category user because the scores for each song were very low and the top 5 songs were within 0.09 points of each other (1.32-1.41).

Lofi Chill vs. High-Energy Pop: Lofi Chill prefers low-energy lofi/chill tracks; High-Energy Pop shifts toward high-energy, intense pop tracks. This makes sense because both profiles have opposite target_energy values.

Mellow Acoustic vs. Dance Party: Mellow Acoustic prefers quiet, highly acoustic classical tracks; Dance Party prefers loud, highly danceable EDM. This makes sense since they have opposite energy and danceability targets.

Conflicting Lofi vs. Sad + High Energy (conflicting): Both conflicting profiles still get pulled toward their genre/mood match despite a poor energy fit. This makes sense because genre (+3.0) and mood (+1.5) outweigh energy (+0.7) in the scoring weights.

Nonexistent Category (opera/furious) vs. High-Energy Pop: High-Energy prefers pop songs with higher energy; Nonexistent Category has no genre or mood matches at all, so scores flatten into a near-tie. This makes sense since removing the categorical bonus removes the main source of separation between songs.

## 8. Future Work  

I would improve the model to enable detecting and considering genre overlaps rather than only giving points for exact genre matches. I would also provide a more reliable way to rank songs in the case that both genre and mood score low, possibly by adjusting weights for that situation only. Another improvement would be adding additional song features to the catalog such as vocal/instrumental distinction and era.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems don't always stick with one method in isolation. Many use collaborative filtering to also add songs based on the behaviors of similar listeners. AI tools helped me understand how to write Pythonic code and also how to consider implementing the weight-based scoring system. I had to double-check the output when it generated code that was unnecessarily complicated or obscure. I will definitely consider the way recommendation systems work when I'm using Spotify, and I will also consider the methods that they employ to recommend songs that I may enjoy if they are outside my typical genre or mood preferences. 
