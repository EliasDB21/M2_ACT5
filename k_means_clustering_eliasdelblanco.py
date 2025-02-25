# -*- coding: utf-8 -*-
"""K-Means Clustering-EliasDelBlanco.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R6jTL4nnuyQy7k4MB9ZIxOB0ahY4QH1k

Yamil Elias Del Blanco Chávez - A00838610

## Lectura de Datos
"""

from google.colab import drive
drive.mount('/content/drive')

# Import necessary libraries
import pandas as pd
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Path to the Excel file
file_path = '/content/drive/MyDrive/Colab Notebooks/Mechanical Engineering Design Course (Nadeem Ahmed Sheikh/Course Evaluation (Responses).xlsx'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
df

print(df.columns)

!pip install squarify

"""## Visualización de los datos: Gráficas para las categorias por analizar"""

import pandas as pd
import squarify
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

# Titles for each graph based on column context
titles = {
    3: "Course Contents Preparedness",
    4: "Teacher Preparedness",
    5: "Student Engagement",
    6: "Course Coverage",
    7: "Discussion and Responses",
    8: "Skill/Knowledge at Start of Course",
    9: "Skill/Knowledge at End of Course",
    10: "Skill/Knowledge Required for Completion",
    11: "Course Contribution to Skill/Knowledge",
    12: "Instructor Effectiveness as Lecturer",
    13: "Clarity and Organization of Presentations",
    14: "Stimulation of Student Interest",
    15: "Effective Use of Class Time",
    16: "Instructor Availability and Helpfulness",
    17: "Grading Promptness and Feedback",
    18: "Clarity of Learning Objectives",
    19: "Organization and Planning of Course Content",
    20: "Appropriateness of Course Workload",
    21: "Inclusivity of Course Organization"
}

# Custom function for generating pastel colors
def generate_pastel_colors(num_colors):
    np.random.seed(42)  # Ensure reproducibility
    base_colors = plt.cm.Pastel1(np.linspace(0, 1, num_colors))
    return [to_rgba(color, alpha=0.9) for color in base_colors]

# Iterate over each specified column and generate a treemap
for col_index in range(3, 22):  # Columns 3 to 21 inclusive
    # Extract column data and counts
    column_name = df.columns[col_index]
    values = df[column_name].value_counts()  # Count unique values

    # Prepare labels with percentages and counts
    total = values.sum()
    labels = [
        f"{category}\n{count} ({count / total:.1%})"
        for category, count in zip(values.index, values.values)
    ]

    # Generate a pastel color palette for the current column
    colors = generate_pastel_colors(len(values))

    # Create and save the treemap
    plt.figure(figsize=(6, 6))  # Larger figure size for better visibility
    squarify.plot(
        sizes=values.values,
        label=labels,
        alpha=0.9,
        color=colors,
        text_kwargs={'fontsize': 10, 'color': 'black'},  # Removed bold from text
        linewidth=1.2  # Set border thickness
    )

    # Remove axis for a clean and professional look
    plt.axis('off')

    # Set the title with improved alignment and font styling
    plt.title(titles[col_index], fontsize=12, loc='center', pad=15, color='black')

    # Tighten the layout for better spacing
    plt.tight_layout()

    # Display the treemap
    plt.show()

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Define custom stopwords
custom_stopwords = set(STOPWORDS).union({
    "see", "lot", "able", "soon", "got", "like", "thing", "wanna", "get",
    "think", "add", "will", "make", "give", "good", "also", "even", "more",
    "one", "time", "student", "course", "help", "project", "learn", "learning",
    "would", "improve", "way", "class", "use", "used", "helped", "dfme", "things",
    "gantt", "given", "every", "certain", "us", "thier", "many", "often", "kind",
    "around", "type", "want", "go", "part", "Firstly", "related", "repeat",
    "ascept", "tart", "especially", "tod", "soft", "enough", "multiple", "trip",
    "theoritical", "Nadeem", "done", "big", "show", "clo", "donig", "durong",
    "etc", "presentation", "made", "atleast", "looks", "check", "mini", "telling",
    "Please", "note", "classes", "recommend", "show", "similar", "generally",
    "needed", "involved", "certeria"
})

# Function to generate a word cloud for a single column
def generate_word_cloud(column_data, title, filename):
    # Combine all text in the column
    text = ' '.join(column_data.dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        stopwords=custom_stopwords,
        colormap='viridis',
        max_words=150
    ).generate(text)

    # Plot the word cloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)  # Save as a high-resolution image
    plt.show()

# Generate word clouds for each column
generate_word_cloud(df["What aspects of this course were most useful or valuable?"],
                    "What Aspects of the Course Were Most Useful or Valuable?",
                    "useful_aspects_wordcloud.png")

generate_word_cloud(df["How would you improve this course?"],
                    "How Would You Improve This Course?",
                    "improve_course_wordcloud.png")

generate_word_cloud(df["Describe the experience of engagement in the project assigned in this course"],
                    "Describe the Experience of Engagement in the Project",
                    "engagement_experience_wordcloud.png")

generate_word_cloud(df["Name one skill or aspect that you gained after completing this course"],
                    "One Skill or Aspect Gained After Completing the Course",
                    "skills_gained_wordcloud.png")

df

"""Se cambian los nombres de las columnas para una mejor comprensión de los datos con los que se estan trabajando."""

# Assuming 'df' is your original DataFrame

# Make a copy of the original DataFrame
df_copy = df.copy()

# List of new column titles
new_column_titles = [
    "Timestamp",
    "Name of Student",
    "Registration Number",
    "Course Content Preparedness",
    "Teacher Preparedness",
    "Student Engagement",
    "Course Coverage",
    "Discussion and Response",
    "Skill/Knowledge at Start",
    "Skill/Knowledge at End",
    "Skill/Knowledge Required",
    "Contribution to Skill/Knowledge",
    "Instructor Effectiveness",
    "Presentation Clarity",
    "Stimulation of Interest",
    "Effective Use of Time",
    "Instructor Availability",
    "Grading and Feedback",
    "Clarity of Learning Objectives",
    "Organization and Planning",
    "Appropriateness of Workload",
    "Student Participation",
    "Course Usefulness",
    "Course Improvement Suggestions",
    "Project Engagement Experience",
    "Skills or Aspects Gained"
]

# Ensure the number of columns in the copied DataFrame matches the new column titles
if len(df_copy.columns) == len(new_column_titles):
    df_copy.columns = new_column_titles
else:
    raise ValueError("The number of columns in the DataFrame does not match the number of provided titles.")

# Display the updated DataFrame
df_copy

"""Eliminar las columnas y filas que no ayudan al análisis para mantener solamente las variables de interes."""

import pandas as pd

# Assuming 'df' is your original DataFrame

# Calculate indices of columns to remove
columns_to_remove_indices = [0, 1, 2] + list(range(df_copy.shape[1] - 3, df_copy.shape[1]))
df_copy = df_copy.drop(columns=df_copy.columns[columns_to_remove_indices])

# Display the updated DataFrame
df_copy

# Delete the last column in df_copy
df_copy = df_copy.iloc[:, :-1]

# Display the updated DataFrame
df_copy

# Delete the last row from df_copy
df_copy = df_copy.iloc[:-1]

# Display the updated DataFrame
df_copy

"""Se hace el encoding de las variables categoricas, para transformarlas en una representación numérica, y asi puedan ser utilizadas en el análisis matemático."""

import pandas as pd

# Assuming df_copy is your DataFrame

# Drop the last row (if not already removed)
df_copy = df_copy.iloc[:-1]

# Define custom mappings
custom_mappings = {
    "Course Content Preparedness": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Teacher Preparedness": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Student Engagement": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Course Coverage": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Discussion and Response": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Skill/Knowledge at Start": {"Poor": 1, "Fair": 2, "Satisfactory": 3, "Very good": 4, "Excellent": 5},
    "Skill/Knowledge at End": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Skill/Knowledge Required": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Contribution to Skill/Knowledge": {"Fair": 1, "Satisfactory": 2, "Very good": 3, "Excellent": 4},
    "Instructor Effectiveness": {"Disagree": 1, "Neutral": 2, "Agree": 3, "Strongly agree": 4},
    "Presentation Clarity": {"Disagree": 1, "Neutral": 2, "Agree": 3, "Strongly agree": 4},
    "Stimulation of Interest": {"Disagree": 1, "Neutral": 2, "Agree": 3, "Strongly agree": 4},
    "Effective Use of Time": {"Disagree": 1, "Neutral": 2, "Agree": 3, "Strongly agree": 4},
    "Instructor Availability": {"Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5},
    "Grading and Feedback": {"Disagree": 1, "Neutral": 2, "Agree": 3, "Strongly agree": 4},
    "Clarity of Learning Objectives": {"Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5},
    "Organization and Planning": {"Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5},
    "Appropriateness of Workload": {"Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5},
    "Student Participation": {"Strongly disagree": 1, "Disagree": 2, "Neutral": 3, "Agree": 4, "Strongly agree": 5},
}

# Apply custom mappings
df_encoded = df_copy.copy()
for column, mapping in custom_mappings.items():
    df_encoded[column] = df_encoded[column].map(mapping)

# Display the encoded DataFrame
print("Encoded DataFrame:")
df_encoded

# Display the mapping for verification
print("\nCustom Mappings Applied:")
for column, mapping in custom_mappings.items():
    print(f"{column}: {mapping}")

"""Se hace la normalización estandar, basicamente se re-escalan los datos para que estén dentro de un rango específico.

Se utiliza el método del codo, donde se requiere graficar la suma de los errores cuadraticos en función del número de clusters, para encontrar un punto donde la disminución de la suma empieza a ser menos pronunciada, formando un "codo" en la gráfica.

Se utiliza Silhouette Score para cada k, el cual indica qué tan bien separados están los clusters (valores más altos indican una mejor separación de los clusters).
"""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Normalize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_encoded)

# Use the elbow method and calculate Silhouette Score for each k
inertia = []
sil_scores = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

    # Only calculate silhouette score for k >= 2
    if k > 1:
        sil_score = silhouette_score(df_scaled, kmeans.labels_)
        sil_scores.append(sil_score)
    else:
        sil_scores.append(None)

# Apply minimalist styling with a clean grid
sns.set(style="darkgrid")  # Use Seaborn's darkgrid theme for a professional look
plt.figure(figsize=(8, 8))  # Set figure size

# Elbow Curve (Inertia)
plt.subplot(2, 1, 1)
plt.plot(k_range, inertia, marker='o', linestyle='-', color='steelblue', linewidth=2, markersize=6)
plt.title('Elbow Method for Optimal k', fontsize=10, pad=10)
plt.xlabel('Number of Clusters (k)', fontsize=10)
plt.ylabel('Inertia (Sum of Squared Distances)', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Silhouette Score
plt.subplot(2, 1, 2)
plt.plot(k_range[1:], sil_scores[1:], marker='o', linestyle='-', color='darkorange', linewidth=2, markersize=6)
plt.title('Silhouette Score for Each k', fontsize=10, pad=10)
plt.xlabel('Number of Clusters (k)', fontsize=10)
plt.ylabel('Silhouette Score', fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

"""Se utiliza el gráfico de radar para poder visualizar la diferencia entre clusters, tomando en cuenta que la prueba del codo indicó que lo optimo era utilizar 3 clusters. Se calcula el promedio de cada característica dentro de cada cluster, lo cual ayuda a entender qué hace único a cada grupo."""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Normalize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_encoded)

# Apply k-means clustering with k=3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df_encoded['Cluster'] = kmeans.fit_predict(df_scaled)

# Analyze each cluster by feature averages
cluster_averages = df_encoded.groupby('Cluster').mean()

# Define the features for the radar plot
features = cluster_averages.columns.tolist()
num_features = len(features)

# Add the first feature to the end to close the radar plot
angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
angles += angles[:1]

# Minimalist styling for the radar plot with polar lines
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))  # Set a square figure size

# Plot each cluster with polar lines
colors = ['steelblue', 'darkorange', 'seagreen']  # Colors for clusters
for cluster in range(cluster_averages.shape[0]):
    values = cluster_averages.iloc[cluster].tolist()
    values += values[:1]  # Close the polygon
    ax.plot(angles, values, label=f'Cluster {cluster}', linewidth=2, color=colors[cluster], linestyle='solid')
    ax.fill(angles, values, alpha=0.25, color=colors[cluster])  # Use slight transparency for the fill

# Add labels for the features
ax.set_xticks(angles[:-1])
ax.set_xticklabels(features, fontsize=10, color='black')  # Use clean, readable labels

# Customize gridlines and add polar lines
ax.tick_params(axis='y', labelsize=8, colors='black')  # Adjust radial tick labels
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='gray')  # Circular gridlines
ax.xaxis.grid(True, linestyle='-', linewidth=0.7, color='gray')  # Polar (radial) gridlines

# Add title and legend
plt.title('Cluster Analysis Radar Plot', size=14, pad=30, color='black', fontweight='bold')  # Title styling
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10, frameon=False, title='Clusters')

# Adjust layout and display
plt.tight_layout()
plt.show()

"""Se guarda el análisis de los 3 clusters en un DataFrame para poder utilizarlo posteriormente."""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Step 1: Normalize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_encoded)

# Step 2: Apply k-means clustering with k=3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df_encoded['Cluster'] = kmeans.fit_predict(df_scaled)

# Step 3: Analyze the clusters
# Display the cluster assignments
print("Cluster assignments:")
print(df_encoded['Cluster'].value_counts())

# Analyze each cluster by feature averages
cluster_analysis = df_encoded.groupby('Cluster').mean()
print("\nCluster analysis (feature averages):")
print(cluster_analysis)

# Step 4: Polar (Radar) plot for cluster analysis
# Calculate the average values for each feature in each cluster
cluster_averages = df_encoded.groupby('Cluster').mean()

# Define the features for the radar plot
features = cluster_averages.columns.tolist()
num_features = len(features)

# Add the first feature to the end to close the radar plot
angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
angles += angles[:1]

# Set up a color palette for clusters
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # List of colors for clusters

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Plot each cluster
for cluster in range(cluster_averages.shape[0]):
    values = cluster_averages.iloc[cluster].tolist()
    values += values[:1]  # Close the polygon
    ax.plot(angles, values, label=f'Cluster {cluster}', linewidth=2, color=colors[cluster])
    ax.fill(angles, values, alpha=0.2, color=colors[cluster])

# Add labels for the features
ax.set_xticks(angles[:-1])
ax.set_xticklabels(features, fontsize=8, color='darkblue')  # Set font size and color

# Customize the radar plot appearance
ax.tick_params(axis='y', labelsize=8, colors='gray')
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='gray')
ax.xaxis.grid(True, linestyle='-', linewidth=0.8, color='gray')
ax.spines['polar'].set_visible(False)  # Remove outer polar spine

# Add a title and legend with professional styling
plt.title('Cluster Analysis Radar Plot', size=10, pad=30, color='darkblue', fontweight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=8, frameon=True, title='Clusters', title_fontsize=8)

# Show the radar plot
plt.tight_layout()
plt.show()

# Step 5: Create a new DataFrame for Cluster Analysis (Feature Averages)
cluster_analysis_df = cluster_averages.reset_index()

# Display the new DataFrame containing cluster feature averages
print("\nCluster analysis DataFrame (feature averages):")
cluster_analysis_df

"""Se utiliza VADER, un diccionario de palabras con puntuaciones predefinidas, en conjunto con lexicón para poder utilizar el analizador de polaridad en un texto (ponderación de -1 a 1). Si la mayoría de los comentarios son negativos, el curso necesita mejoras. Si los comentarios son mayormente neutros, no hay opiniones fuertes. Si hay muchos comentarios positivos, el curso es bien recibido."""

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

# Ensure VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Ensure all values are strings and replace NaN or missing values with an empty string
df['How would you improve this course?'] = df['How would you improve this course?'].fillna('').astype(str)

# Analyze the sentiment for the column
def analyze_sentiment(text):
    sentiment = sid.polarity_scores(text)
    return sentiment['compound']  # Return compound score (-1 to 1)

# Apply sentiment analysis to the column
df['Improvement Sentiment Score'] = df['How would you improve this course?'].apply(analyze_sentiment)

# Categorize sentiment based on the compound score
def categorize_sentiment(score):
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['Improvement Sentiment Category'] = df['Improvement Sentiment Score'].apply(categorize_sentiment)

# Display the updated DataFrame
print(df[['How would you improve this course?', 'Improvement Sentiment Score', 'Improvement Sentiment Category']])

# Visualization: Sentiment Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Improvement Sentiment Category', palette='coolwarm', order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution for "How would you improve this course?"', fontsize=14, fontweight='bold')
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

# Ensure VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Ensure all values are strings and replace NaN or missing values with an empty string
df['How would you improve this course?'] = df['How would you improve this course?'].fillna('').astype(str)

# Analyze the sentiment for the column
def analyze_sentiment(text):
    sentiment = sid.polarity_scores(text)
    return sentiment['compound']  # Return compound score (-1 to 1)

# Apply sentiment analysis to the column
df['Improvement Sentiment Score'] = df['How would you improve this course?'].apply(analyze_sentiment)

# Filter out neutral responses
df_filtered = df[(df['Improvement Sentiment Score'] > 0.05) | (df['Improvement Sentiment Score'] < -0.05)]

# Set Seaborn theme for consistent visuals
sns.set_theme(style="darkgrid")

# Plot the distribution of filtered sentiment scores
plt.figure(figsize=(6, 4))
sns.histplot(df_filtered['Improvement Sentiment Score'], bins=20, kde=True, color='dodgerblue', edgecolor="black", linewidth=1.5)
plt.title('Distribution of Positive and Negative Sentiment Scores', fontsize=10, fontweight='bold', pad=15)
plt.xlabel('Sentiment Score (Compound)', fontsize=10, labelpad=10)
plt.ylabel('Frequency', fontsize=10, labelpad=10)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

"""Se utiliza el modelo "LatentDirichletAllocation" para mostrar las palabras más representativas de cada uno de los 3 temas y luego se muestran las palabras más represnetativas del tema."""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Combine text from relevant columns
text_data = df['What aspects of this course were most useful or valuable?'].fillna('') + ' ' + \
            df['Describe the experience of engagement in the project assigned in this course'].fillna('')

# Vectorize text
vectorizer = CountVectorizer(stop_words='english', max_features=1000)
text_matrix = vectorizer.fit_transform(text_data)

# Apply LDA
lda = LatentDirichletAllocation(n_components=3, random_state=42)  # 3 topics
lda.fit(text_matrix)

# Display top words in each topic
words = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lda.components_):
    print(f"Topic {idx + 1}:")
    print([words[i] for i in topic.argsort()[-10:]])

"""Luego de analizar a profundidad el código me pareció muy interesante las diversas tecnicas utilizadas para identificar patrones en los comentarios de los estudiantes y asi poder mejorar el contenido del curso. Lo más valioso que me llevo de este análisis fue conocer la aplicación del metodo del codo para encontrar la cantidad de clusters ideal y su representación a través del gráfico de radar."""