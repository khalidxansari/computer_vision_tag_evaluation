
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import numpy as np

def calculate_metrics(y_true, y_pred):
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    accuracy = accuracy_score(y_true, y_pred)
    return {
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1,
        'Accuracy': accuracy
    }

def evaluate_category(category, ai_tags, controlled_vocab_dict):
    category_vocab = controlled_vocab_dict.get(category, [])
    y_true = [1 if tag in category_vocab else 0 for tag in category_vocab]
    y_pred = [1 if tag in ai_tags else 0 for tag in category_vocab]
    return calculate_metrics(y_true, y_pred)

def plot_performance_heatmap(performance_data, categories, metrics):
    plt.figure(figsize=(12, 8))
    sns.heatmap(performance_data, annot=True, cmap='YlGnBu',
                xticklabels=categories, yticklabels=metrics)
    plt.title('AI Service Performance Across Image Categories')
    plt.tight_layout()
    plt.show()

def plot_category_performance(category, metrics_dict):
    plt.figure(figsize=(10, 6))
    plt.bar(metrics_dict.keys(), metrics_dict.values())
    plt.title(f'Performance Metrics for {category}')
    plt.ylabel('Score')
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.show()

def create_tag_network(ai_tags, controlled_vocab):
    G = nx.Graph()
    for ai_tag in ai_tags:
        for cv_tag in controlled_vocab:
            if ai_tag.lower() in cv_tag.lower():
                G.add_edge(ai_tag, cv_tag)
    return G

def plot_tag_network(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=3000, font_size=8, font_weight='bold')
    plt.title('AI-Generated Tags vs. Controlled Vocabulary')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
