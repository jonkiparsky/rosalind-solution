class RosalindSolution(object):
    download_dir_path = "/Users/jpk/Downloads"
    download_filename_template = "rosalind_%s.txt"

    upload_dir_path = "/Users/jpk/code/rosalind/"
    upload_filename_template = "rosalind_%s_out.txt"
    problem_name = "NAME REQUIRED"
    
    def __init__(self):
        self.download_filename = self.download_filename_template % self.problem_name
        self.download_filepath = "%s/%s" % (self.download_dir_path, self.download_filename)
        self.upload_filename = self.upload_filename_template % self.problem_name
        self.upload_filepath = "%s/%s" % (self.upload_dir_path, self.upload_filename)        

    def dataset(self):
        f = open(self.download_filepath)
        return self.process_dataset(f)

    def process_dataset(self, f):
        '''Called by dataset. Override for the expected data format.'''
        return f.read().strip().replace("\n", "")

    def solve(self, dataset):
        '''Override with solution'''
        return dataset

    def solve_instance(self):
        return self.solve(self.dataset())

    def format_solution(self, solution):
        return solution
    
    def write_solution(self, solution, filepath=None):
        filepath = filepath or self.upload_filepath
        outfile = open(filepath, "w")
        outfile.write(self.format_solution(solution))
        outfile.close()
        
    def go(self):
        '''Open the expected file, solve the dataset, and write to the outfile'''
        dataset = self.dataset()
        solution = self.solve_instance()
        self.write_solution(solution)
        print "wrote solution to %s" % self.upload_filename
