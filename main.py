import argparse

from ComplexPrefixSpan.Builder import Builder
from ComplexPrefixSpan.ComplexPrefixSpan import ComplexPrefixSpan
from ComplexPrefixSpan.Sequence import *

if __name__ == "__main__":

    # Add a command line parser
    parser = argparse.ArgumentParser(description='Run Complex prefix span over database')
    parser.add_argument('dataset_path', nargs="?", type=str, default="./datasets/test_sample.csv",
                        help='Path to the csv file which holds the sequence dataset.')
    parser.add_argument('--min_support', type=int, default=2, help="Min support value which can be used.")
    parser.add_argument('--structure_type', type=str, default="binary_tree",
                        help="Specify which complex structure is contained in the sequences.")
    parser.add_argument('--max_length_sequence', type=int, default=3, help="Maximal length of the frequent sequences.")

    parser.add_argument('--iterative', action="store_true", default=False, help="Run using the iterative approach.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Build the dataset
    dataset = Builder.create_dataset(args.dataset_path)

    database = [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(9)]),
        Sequence([SequenceItem(3), SequenceItem(3), SequenceItem(3)]),
    ]

    seqs =  [
        Sequence([SequenceItem(1), SequenceItem(2), SequenceItem(3)]),
        Sequence([SequenceItem(3), SequenceItem(3)])]

    # Find complex sequences
    finder = ComplexPrefixSpan(dataset)
    result = finder.compute(args.min_support, args.max_length_sequence, args.iterative)
    print(result)
