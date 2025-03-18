text = """
In the fast-paced world of business, it’s easy to get caught up in the day-to-day and lose sight of the bigger picture.
But I want to take a moment today to remind us all of the incredible power we have as a team.Every one of you brings unique skills, perspectives, and experiences to the table. 
When we harness that diversity and work together towards a common goal, there’s nothing we can’t achieve.
I’ve seen firsthand the incredible things this team is capable of when we support each other, challenge each other, and push ourselves to be better.
  
"""

print(len(text.split()))

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1 

print(word_count)