import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):     
    def __init__(self, prob=.5, size=20):
        Distribution.__init__(self, self.calculate_mean, self.calculate_stdev)
        self.p = prob
        self.n = size
    
    def calculate_mean(self):
        mean = self.p * self.n
        self.mean = mean
        return self.mean

    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p *(1 - self.p))
        return self.stdev
        
    def replace_stats_with_data(self):
        self.n = len(self.data)
        self.p = 1.0 * (sum(self.data) / len(self.data))
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev
        return self.p, self.n
        
    def plot_bar(self):
        plt.hist(['0', '1'], height= [(1 - self.p) * self.n, self.p * self.n])
        plt.title("Bar chart of data")
        plt.xlabel('outcome')
        plt.ylabel('count')
        
    def pdf(self, k):        
        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        
        return a * b 
    
    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
                
    def __add__(self, other):
        binomial_object = Binomial()
        binomial_object.n = self.n + other.n
        binomial_object.p = self.p
        binomial_object.calculate_mean()
        binomial_object.calculate_stdev()
        return binomial_object
        
        
    def __repr__(self):
        return ('mean {}, standard deviation {}, p {}, n {}'.format(self.mean, self.stdev, self.p, self.n))
