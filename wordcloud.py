from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Retrieve entries from the database
rows = self.db.get_entries_by_date(start_date_str, end_date_str)

# Concatenate all the text from the entries into a single string
all_text = ""
for row in rows:
    all_text += row[1] + " "  # Concatenate dreams text
    all_text += row[2] + " "  # Concatenate thoughts text
    all_text += row[3] + " "  # Concatenate positive affirmation text
    all_text += row[4] + " "  # Concatenate one thing to get done text

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
