#### Basics of randomness & simulation
## Poisson random variable
# Initialize seed and parameters
# Poisson distribution, which is typically used for modeling the average rate at which events occur
np.random.seed(123) 
lam, size_1, size_2 = 5, 3, 1000  

# Draw samples & calculate absolute difference between lambda and sample mean
samples_1 = np.random.poisson(lam, size_1)
samples_2 = np.random.poisson(lam, size_2)
answer_1 = abs(lam - samples_1.mean())
answer_2 = abs(lam - samples_2.mean()) 

print("|Lambda - sample mean| with {} samples is {} and with {} samples is {}. ".format(size_1, answer_1, size_2, answer_2))

# Shuffle the deck
np.random.shuffle(deck_of_cards) 

# Print out the top three cards
card_choices_after_shuffle = deck_of_cards[0:3]
print(card_choices_after_shuffle)

# Define die outcomes and probabilities
die, probabilities, throws = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 1

# Use np.random.choice to throw the die once and record the outcome
outcome = np.random.choice(die, size=throws, p=probabilities)
print("Outcome of the throw: {}".format(outcome[0]))

#def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0
    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number=np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number<p:
            n_success +=1 

    return n_success
