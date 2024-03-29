import csv
import matplotlib.pyplot as plt

def load_data(filename, column_index):
    data = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row[column_index])
    return data

def create_subplot(ax, data, title, fontsize='medium'):
    value_counts = {}
    for value in data:
        value_counts[value] = value_counts.get(value, 0) + 1
    labels = value_counts.keys()
    counts = value_counts.values()
    ax.bar(labels, counts)
    ax.set_xlabel(title)
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=90, labelsize=6)
    ax.tick_params(axis='y', labelsize=fontsize)

def main():

    filename = 'Mental.csv'
    gender_data = load_data(filename, 1)
    country_data = load_data(filename, 2)
    occupation_data = load_data(filename, 3)
    self_employed_data = load_data(filename, 4)
    family_history_data = load_data(filename, 5)
    changes_habits_data = load_data(filename, 9)

    fig, axs = plt.subplots(3, 2, figsize=(12, 12))

    # Plot each categorical variable
    create_subplot(axs[0, 0], gender_data, 'Gender')
    create_subplot(axs[0, 1], country_data, 'Country')
    create_subplot(axs[1, 0], occupation_data, 'Occupation')
    create_subplot(axs[1, 1], self_employed_data, 'Self Employed')
    create_subplot(axs[2, 0], family_history_data, 'Family History')
    create_subplot(axs[2, 1], changes_habits_data, 'Changes Habits')  # Add subplot for Changes Habits

    # Set title for all subplots
    fig.suptitle('Distribution of Categorical Variables', fontsize=16)

    # Adjust layout
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.6)
    plt.show()

if __name__ == "__main__":
    main()
