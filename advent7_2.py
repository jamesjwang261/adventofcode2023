from collections import defaultdict

f = open('advent7_input.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def sort_key(pair):
  deal, bet = pair
  res = []
  card_freq = defaultdict(int)
  for c in deal:
    card_freq[c] += 1
    res.append(cards.index(c))
    
  j_freq = card_freq['J']
  card_freq['J'] = 0
  freqs = list(card_freq.values())
  
  # 5 of a kind
  if 5-j_freq in freqs:
    res.insert(0, 0)
  
  # 4 of a kind
  elif 4-j_freq in freqs:
    res.insert(0, 1)
    
  # full house
  elif (3 in freqs and 2 in freqs) or (j_freq == 1 and freqs.count(2) == 2):
    res.insert(0, 2)
  
  # 3 of a kind
  elif 3-j_freq in freqs:
    res.insert(0, 3)
  
  # 2 pair
  elif freqs.count(2) == 2 or (j_freq == 1 and 2 in freqs):
    res.insert(0, 4)
    
  # 1 pair
  elif 2 in freqs or j_freq == 1:
    res.insert(0, 5)
    
  # high card
  else:
    res.insert(0, 6)

  return res


pairs = []
for line in lines:
  deal, bet = line.split()
  pairs.append((deal, int(bet)))
  
pairs.sort(key=sort_key, reverse=True)

res = 0
for i, pair in enumerate(pairs):
  _, bet = pair
  res += (i+1)*bet
  
print(res)
