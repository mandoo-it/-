from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_list = defaultdict(int)
    genre_list = defaultdict(list)
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        play_list[genre] += play
        genre_list[genre].append([index, play])
  
    play_list = sorted(play_list, key = lambda x : -play_list[x] )
    print(genre_list)
    
    for item in play_list:
        genre_list[item] = sorted(genre_list[item], key = lambda x : (-x[1], x[0]))
        # answer.extend([song[0] for song in genre_list[genre][:2]])
        answer.extend([song[0] for song in genre_list[item][:2]])
    
    
    return answer
