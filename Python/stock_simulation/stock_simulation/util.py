import random
import string
import matplotlib.pyplot as plt

def generate_random_word(length):
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    word = ""
    
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    
    return word.capitalize()

def generate_company_name():
    prefix_length = random.randint(2, 4)
    suffix_length = random.randint(3, 5)
    
    prefix = generate_random_word(prefix_length)
    suffix = generate_random_word(suffix_length)
    
    suffixes = ["Tech", "Corp", "Solutions", "Systems", "Industries", "Enterprises", "Dynamics", "Holdings", "Ventures", "Innovations"]
    suffix_choice = random.choice(suffixes)
    
    company_name = f"{prefix}{suffix} {suffix_choice}"
    return company_name

def company_lists(n):
    res = []
    while len(res) < n:
        cand = generate_company_name()
        if cand not in res:
            res.append(cand)

    return res 

def plot_line_graph(data, save_to = 'sample.png', title="Line Graph", x_label="X-axis", y_label="Y-axis"):
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.savefig(save_to)
    plt.close()

if __name__ == '__main__':
    plot_line_graph(range(100))