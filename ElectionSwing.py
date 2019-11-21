# http://fivethirtyeight.com/features/a-puzzle-will-you-yes-you-decide-the-election/

"""You are the only sane voter in a state with two candidates running for Senate.
There are N other people in the state, and each of them votes completely randomly!
 Those voters all act independently and have a 50-50 chance of voting for either candidate.
 What are the odds that your vote changes the outcome of the election toward your preferred candidate?

More importantly, how do these odds scale with the number of people in the state?
For example, if twice as many people lived in the state, how much would your chances of swinging the election change?"""

import random
import matplotlib.pyplot as plt


# Randomly assigns votes of an N-sized population
def voting(population):
    vote_a = 0
    vote_b = 0
    for voter in range(population):
        voter = random.randint(0, 1)
        if voter == 0:
            vote_a += 1
        else:
            vote_b += 1
    return vote_a, vote_b


# Repeats voting function N number of times to approximate probability of swing vote
def election_count(pop, n=10000):
    swing = 0
    for _ in range(n+1):
        vote_a, vote_b = voting(pop)
        if vote_a == vote_b:
            swing += 1

    print(pop, "You could change {0} out of {1} elections.".format(swing, n))
    return swing / n


if __name__ == '__main__':

    swing_prob = []

    for i in range(2, 100, 2):
        prob = election_count(i)
        swing_prob.append(prob)

    plt.plot([i for i in range(2, 100, 2)], swing_prob)
    plt.plot([1 / i for i in range(2, 100, 2)], label='y = 1/n')
    plt.title('Probability of Swing Vote')
    plt.xlabel("Number of voters")
    plt.legend()
    plt.show()
