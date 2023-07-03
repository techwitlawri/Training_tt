if __name__=='__main__':
    word_list = []
    emoji_data = {
        'happy': '😀',
        'laughing' : '😃',
        'friends': '👩🏼‍🤝‍👩🏻',
        'hello': '🤚',
        'whatever' : '😏',
        'surprise': '😮',
        'car': '🚕',
        'worried': '🤔',
        'wink': '😉',
        'swag': '😎',
        'crying': '😭',
        'angry': '😡', 
        'vomiting': '🤮',
        'shy': '🙈'

    }
    users_text = input('Enter message: ')

    word_list = users_text.split(' ')

    for word in range(len(word_list)):
        for key, value in emoji_data.items():
            if word_list[word] == key:
                word_list[word] = value
    joined_words = ' '.join(word_list)
    print(joined_words)
    
      
    




 