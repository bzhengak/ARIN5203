# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils

def calculate_london_baseline_accuracy(filepath):
    """
    Calculates the accuracy of a baseline that predicts "London" for every example.
    """
    # Read all lines to determine the number of predictions needed
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    total = len(lines)
    
    # Create a list of "London" predictions with the same length as the number of examples
    predicted_places = ["London"] * total
    
    # Use the existing evaluation function
    total, correct = utils.evaluate_places(filepath, predicted_places)
    
    return total, correct

if __name__ == "__main__":
    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('eval_corpus_path', help="Path to the evaluation corpus")
    args = argp.parse_args()
    
    total, correct = calculate_london_baseline_accuracy(args.eval_corpus_path)
    if total > 0:
        print(f'London baseline accuracy: {correct}/{total} ({correct/total*100:.2f}%)')
    else:
        print('No evaluation data available.')