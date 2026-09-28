import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualization(df, output_path):
    """
    Seaborn / matplotlib se charts generate karke file save karta hai
    """
    plt.figure(figsize=(12, 5))

    # charts 1: Gender vs Survival
    plt.subplot(1, 2, 1)
    sns.barplot(x='Sex', y='Survived', data=df, errorbar=None, palette='Set2')
    plt.title('Survival rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Survivel Rate')

    # chart 2: Pclass vs Survival by Gender
    plt.subplot(1, 2, 2)
    sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df, errorbar=None, palette='Set1')
    plt.title('Survival Rate by Class & Gender')
    plt.xlabel('Passenger')
    plt.ylabel('Survival Rate')

    plt.tight_layout()
    plt.savefig(output_path)
    print(f"\n== CHAART SAVE AT '{output_path}' ===")
    plt.show()