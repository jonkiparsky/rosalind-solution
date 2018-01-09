from rosalind_solution import RosalindSolution


symbols = ["A", "C", "G", "T"]
def symbol_count(dna_string):
    return " ".join(map(str, [dna_string.count(symbol) for symbol in symbols]))


class RosalindDNA(RosalindSolution):
    problem_name = "dna"

    def solve(self, dataset):
        return symbol_count(dataset)
