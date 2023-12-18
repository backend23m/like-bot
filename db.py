import json

def read() -> dict:
    with open('db.json') as f:
        try:
            return json.load(f)
        except json.decoder.JSONDecodeError:
            return {}

def save(data: dict):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

def is_user(chat_id: str) -> bool:
    data = read()
    return chat_id in data.keys()

def get_user(chat_id: str) -> bool:
    data = read()
    if not is_user(chat_id):
        return False
    
    return data[chat_id]

def add(chat_id: str) -> bool:
    data = read()
    data.setdefault(chat_id, {'likes': 0, 'dislikes': 0, 'inline_likes': 0, 'inline_dislikes': 0}) 
    save(data)

def update_db(chat_id: str, is_like=False, is_dislike=False, clear=False) -> bool:
    if not is_user(chat_id):
        return False

    data = read()

    if is_like:
        data[chat_id]['likes'] += 1
    elif is_dislike:
        data[chat_id]['dislikes'] += 1
    elif clear:
        data[chat_id]['likes'] = 0
        data[chat_id]['dislikes'] = 0

    save(data)
    return data[chat_id]

