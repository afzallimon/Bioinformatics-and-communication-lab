import difflib
import os

def load_reference_sequence(filepath):
    """Load the reference sequence from a .fna file."""
    with open(filepath, 'r') as file:
        lines = file.readlines()
    # Ignore the first line (header) and join the rest into a single sequence
    reference_sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return reference_sequence

def calculate_similarity(seq1, seq2):
    """Calculate the similarity percentage between two sequences."""
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    return matcher.ratio() * 100

def check_infection(reference, user_input):
    """Compare user input sequence to reference and determine infection status."""
    similarity = calculate_similarity(reference, user_input)
    is_infected = similarity < 95.0  # Adjusted threshold for determining infection
    return is_infected, similarity

def main():
    print("Bioinformatics: Papaya Leaf Curl Virus Detection")
    print("================================================")

    # Load reference sequence
    filepath = "papaya_leaf_virus.fna"
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found in the current directory.")
        print("Ensure the file is present and try again.")
        return

    try:
        reference_sequence = load_reference_sequence(filepath)
        print("Reference sequence loaded successfully!")
    except Exception as e:
        print(f"Error: Unable to load the reference sequence. Details: {e}")
        return

    # Get user input sequence
    user_sequence = input("Enter the DNA sequence to check: ").strip().upper()

    # Validate user input
    if not all(base in "ATGC" for base in user_sequence):
        print("Error: Invalid DNA sequence. Only A, T, G, and C are allowed.")
        return

    # Check infection status
    is_infected, similarity = check_infection(reference_sequence, user_sequence)

    # Output results
    print("\nResults:")
    print(f"Similarity with reference: {similarity:.2f}%")
    if is_infected:
        print("Status: Infected (Significant deviation detected)")
    else:
        print("Status: Not Infected (Sequence matches reference closely)")

if __name__ == "__main__":
    main()
