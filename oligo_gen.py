import random
import os

# Function to generate a random nucleotide based on the provided ratios
def generate_mixed_base(ratio):
    # Ratios are given in order A, C, G, T
    bases = ['A', 'C', 'G', 'T']
    population = []
    
    # Parse the ratio string (e.g., "50005000" becomes [50, 0, 50, 0])
    if len(ratio) != 8:  # Expecting 8 digits: 2 digits for each base ratio
        raise ValueError(f"Invalid ratio length: {ratio}. Expected 8 digits for A, C, G, T ratios.")
    
    for i in range(4):  # Expecting 4 bases (A, C, G, T)
        base_percentage = int(ratio[i*2:i*2+2])  # Extract every two digits
        if base_percentage > 0:
            population.extend([bases[i]] * base_percentage)
    
    if not population:
        raise ValueError(f"Invalid ratio: {ratio}. No bases have positive percentages.")
    
    # Return a random choice based on the provided ratios
    return random.choice(population)

# Function to generate an example sequence
def generate_sequence(oligo_sequence):
    result_sequence = []
    custom_mixes = {}
    
    i = 0
    while i < len(oligo_sequence):
        # Check if this is the start of a custom mix definition (e.g., N(50005000))
        if i + 1 < len(oligo_sequence) and oligo_sequence[i].isalpha() and oligo_sequence[i + 1] == '(':
            label = oligo_sequence[i]  # e.g., N, N1, K, etc.
            end_idx = oligo_sequence.find(')', i)
            if end_idx == -1:
                raise ValueError("Unmatched parenthesis in sequence input.")
            
            # Extract the ratio from the parentheses
            ratio = oligo_sequence[i + 2:end_idx]
            custom_mixes[label] = ratio  # Store the ratio for this label
            result_sequence.append(generate_mixed_base(ratio))  # Generate the first mixed base
            
            i = end_idx  # Move past the processed custom mix
        elif oligo_sequence[i].isalpha():
            # If this is a subsequent use of a defined label or a fixed nucleotide
            label = oligo_sequence[i]
            if label in custom_mixes:
                result_sequence.append(generate_mixed_base(custom_mixes[label]))
            elif label in ['A', 'C', 'G', 'T']:  # Fixed nucleotide
                result_sequence.append(label)
            else:
                raise ValueError(f"Unknown mix label: {label}")
        else:
            # Ignore non-alphabetic characters
            i += 1
            continue  # Skip any unexpected characters
        
        i += 1

    return ''.join(result_sequence)

# Function to generate multiple sequences and output to a text file in FASTA format
def generate_sequences_to_fasta(oligo_sequence, num_sequences=100, output_file="sequences.fasta"):
    sequences = []
    
    # Generate multiple sequences
    for seq_id in range(1, num_sequences + 1):
        sequence = generate_sequence(oligo_sequence)
        sequences.append(f">Seq_{seq_id}\n{sequence}")
    
    # Write the sequences to a text file in FASTA format
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), output_file)
    with open(output_path, "w") as f:
        f.write("\n".join(sequences))
    
    print(f"{num_sequences} sequences saved to {output_path} in FASTA format.")

# Main function to handle user input and generate the sequences
def main():
    print("Script started")  # Debugging message to confirm the script is running
    # Prompt the user to enter the oligonucleotide sequence with custom mixes
    print("Enter your oligonucleotide sequence (e.g., N(50005000)ATCGN):")
    user_input = input().strip()

    # Prompt the user for the number of sequences and output file name
    num_sequences = int(input("Enter the number of sequences to generate: "))
    output_file = input("Enter the output text file name (e.g., sequences.fasta): ").strip()

    # Generate the sequences and save to a text file in FASTA format
    try:
        print(f"Generating {num_sequences} sequences...")
        generate_sequences_to_fasta(user_input, num_sequences, output_file)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()