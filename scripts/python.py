# import pattern.en

data = ['Amazon', 'America', 'Batman', 'Buddha', 'China', 'Dalai Lama', 'Disney', 'Facebook', 'Google', 'Hitler', 'Jesus', 'Lincoln', 'Mozart', 'Picasso', 'Seattle', 'Syria', 'account', 'achiever', 'acoustics', 'act', 'action', 'activity', 'actor', 'addition', 'adjustment', 'advertisement', 'aftermath', 'afternoon', 'afterthought', 'agreement', 'air', 'airplane', 'airport', 'alarm', 'alley', 'amount', 'amusement', 'anger', 'angle', 'animal', 'answer', 'ant', 'apparatus', 'apparel', 'apple', 'appliance', 'approval', 'arch', 'argument', 'arithmetic', 'arm', 'army', 'arrested', 'art', 'attack', 'attempt', 'attention', 'attraction', 'aunt', 'authority', 'average', 'avocado', 'awkward', 'baby', 'back', 'badge', 'bag', 'bait', 'balance', 'ball', 'balloon', 'banana', 'band', 'bare', 'base', 'baseball', 'basin', 'basket', 'basketball', 'bat', 'bath', 'battery', 'battle', 'bead', 'beam', 'bean', 'bear', 'beast', 'bed', 'bedroom', 'bee', 'beef', 'beetle', 'beggar', 'beginner', 'behavior', 'belief', 'bell', 'berry', 'best', 'bike', 'bird', 'birth', 'birthday', 'bit', 'bite', 'blackjack', 'blade', 'blood', 'blow', 'board', 'board game', 'boat', 'body', 'bomb', 'bone', 'book', 'boot', 'booty', 'border', 'bottle', 'boundary', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'break', 'breath', 'brick', 'bridge', 'brother', 'brothers', 'brunch', 'brush', 'bubble', 'bucket', 'building', 'bulb', 'bun', 'bunny', 'burn', 'burst', 'bushes', 'business', 'button', 'cabbage', 'cable', 'cactus', 'cake', 'calculator', 'calendar', 'camera', 'camp', 'can', 'cannon', 'cap', 'caption', 'car', 'card', 'care', 'carpenter', 'carriage', 'cart', 'cast', 'castle', 'cat', 'cattle', 'cause', 'cave', 'celery', 'cellar', 'cemetery', 'cent', 'cereal', 'chain', 'chair', 'chalk', 'chance', 'change', 'channel', 'cherry', 'chess', 'chicken', 'children', 'chin', 'church', 'cilantro', 'circle', 'clam', 'class', 'clock', 'cloth', 'cloud', 'clover', 'club', 'coach', 'coal', 'coast', 'coat', 'cobweb', 'coil', 'collar', 'color', 'comb', 'comfort', 'committee', 'company', 'comparison', 'competition', 'condition', 'connection', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'corn', 'cough', 'country', 'cover', 'cow', 'cows', 'crack', 'cracker', 'crate', 'crayon', 'cream', 'creator', 'creature', 'credit', 'crib', 'crime', 'crook', 'cross', 'crow', 'crowd', 'crown', 'crush', 'cry', 'cub', 'cup', 'current', 'curtain', 'curve', 'cushion', 'dad', 'daughter', 'day', 'death', 'debt', 'decision', 'degree', 'design', 'desire', 'desk', 'destruction', 'detail', 'development', 'digestion', 'dignity', 'dime', 'dinner', 'dinosaurs', 'direction', 'dirt', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'dock', 'doctor', 'dog', 'doll', 'donkey', 'door', 'downtown', 'dragon', 'drain', 'drawer', 'dress', 'drink', 'driving', 'drop', 'drug', 'drum', 'duck', 'dungeon', 'dust', 'ear', 'earth', 'earthquake', 'edge', 'education', 'effect', 'egg', 'eggnog', 'elbow', 'elephant', 'end', 'engine', 'error', 'event', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face', 'fact', 'fairies', 'fall', 'false', 'family', 'fan', 'fang', 'farm', 'farmer', 'fatal', 'father', 'faucet', 'fear', 'feast', 'feather', 'feeling', 'fiction', 'field', 'fifth', 'fight', 'finger', 'fire', 'fireman', 'fish', 'flag', 'flame', 'flavor', 'flesh', 'flight', 'flock', 'floor', 'flower', 'fly', 'fog', 'fold', 'food', 'foot', 'football', 'force', 'forever', 'fork', 'form', 'fowl', 'frame', 'friction', 'friend', 'frog', 'front', 'fuel', 'game', 'garden', 'gate', 'ghost', 'giants', 'giraffe', 'girl', 'glass', 'glove', 'glue', 'goat', 'gold', 'good-bye', 'goose', 'government', 'governor', 'grade', 'grain', 'grandfather', 'grandmother', 'grape', 'grass', 'grip', 'gross', 'ground', 'group', 'growth', 'guide', 'guitar', 'gunH', 'hair', 'haircut', 'hall', 'hammer', 'hand', 'harbor', 'harmony', 'hat', 'hate', 'head', 'health', 'hearing', 'heart', 'heat', 'help', 'hen', 'hill', 'history', 'hobbies', 'hole', 'holiday', 'home', 'honey', 'hook', 'hope', 'horn', 'horse', 'hose', 'hospital', 'hot', 'hour', 'house', 'humor', 'hydrant', 'ice', 'icicle', 'idea', 'impulse', 'income', 'increase', 'industry', 'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'island', 'jail', 'jam', 'jar', 'jeans', 'jelly', 'jewel', 'join', 'joke', 'journey', 'judge', 'juice', 'jump', 'kettle', 'key', 'kick', 'kiss', 'kite', 'kitten', 'kitty', 'knee', 'knife', 'knot', 'laborer', 'lace', 'ladybug', 'lake', 'lamp', 'land', 'language', 'laugh', 'lawyer', 'lead', 'leaf', 'learning', 'leather', 'leg', 'letter', 'lettuce', 'level', 'library', 'lift', 'light', 'limit', 'line', 'linen', 'lip', 'liquid', 'list', 'lizards', 'loaf', 'lock', 'locket', 'look', 'loss', 'low', 'lumber', 'lunchroom', 'machine', 'magic', 'maid', 'mailbox', 'man', 'manager', 'map', 'marble', 'mark', 'market', 'mask', 'mass', 'match', 'meal', 'measure', 'mediocre', 'meeting', 'memory', 'metal', 'mice', 'middle', 'milk', 'mimosa', 'mind', 'mine', 'minister', 'mint', 'minute', 'mist', 'mitten', 'mom', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'move', 'muscle', 'music', 'nail', 'name', 'nation', 'neck', 'need', 'needle', 'nerve', 'nest', 'net', 'night', 'ninja', 'noise', 'north', 'nose', 'note', 'notebook', 'number', 'nut', 'oatmeal', 'observation', 'ocean', 'offer', 'office', 'oil', 'operation', 'opinion', 'orange', 'order', 'organization', 'ornament', 'oven', 'owl', 'owner', 'page', 'pail', 'pain', 'paint', 'pan', 'pancake', 'paper', 'parcel', 'parent', 'park', 'part', 'partner', 'party', 'passenger', 'paste', 'patch', 'payment', 'peace', 'peanuts', 'pear', 'pen', 'pencil', 'person', 'pest', 'pet', 'pickle', 'picture', 'pie', 'pig', 'pin', 'pipe', 'pirate', 'pizzas', 'place', 'plane', 'plant', 'plantation', 'plastic', 'plate', 'play', 'playground', 'pleasure', 'plot', 'plough', 'pocket', 'point', 'poison', 'poker', 'police', 'polish', 'pollution', 'ponies', 'poop', 'popcorn', 'porter', 'position', 'pot', 'potato', 'powder', 'power', 'price', 'princess', 'print', 'prison', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'pull', 'pump', 'punishment', 'punt', 'purpose', 'push', 'quarter', 'quartz', 'queen', 'question', 'quicksand', 'quiet', 'quill', 'quilt', 'quince', 'quiver', 'rabbit', 'rail', 'railway', 'rain', 'rainstorm', 'rake', 'range', 'rat', 'rate', 'ray', 'reaction', 'reading', 'reason', 'receipt', 'recess', 'record', 'regret', 'relation', 'religion', 'representative', 'request', 'respect', 'rest', 'reward', 'rhythm', 'riddle', 'rifle', 'ring', 'river', 'road', 'robin', 'robot', 'rock', 'rod', 'roll', 'roof', 'room', 'root', 'rose', 'route', 'rub', 'rule', 'run', 'sack', 'sail', 'salt', 'scale', 'scarecrow', 'scarf', 'scene', 'scent', 'school', 'science', 'screw', 'sea', 'seashore', 'seat', 'secretary', 'seed', 'selection', 'self', 'sense', 'servant', 'shade', 'shake', 'shame', 'shape', 'sheet', 'shelf', 'ship', 'shirt', 'shock', 'shoe', 'shop', 'show', 'side', 'sidewalk', 'sign', 'silk', 'silver', 'sink', 'sister', 'size', 'skate', 'skin', 'skirt', 'skunk', 'sky', 'slave', 'sleep', 'sleet', 'slip', 'slope', 'smash', 'smell', 'smile', 'smoke', 'snail', 'snake', 'sneeze', 'snow', 'soap', 'soccer', 'society', 'sock', 'soda', 'sofa', 'son', 'song', 'sort', 'sound', 'soup', 'space', 'spade', 'spark', 'spicy', 'spiders', 'sponge', 'spoon', 'spot', 'spring', 'spy', 'square', 'squirrel', 'stage', 'stamp', 'star', 'start', 'statement', 'station', 'steam', 'steel', 'stem', 'step', 'stew', 'stick', 'stitch', 'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'stove', 'stranger', 'straw', 'stream', 'street', 'stretch', 'strike', 'string', 'strip', 'structure', 'substance', 'sugar', 'suggestion', 'suit', 'summer', 'sun', 'support', 'surprise', 'sweater', 'swim', 'swing', 'system', 'table', 'tail', 'talk', 'tank', 'taste', 'tax', 'teaching', 'team', 'telegraph', 'temper', 'tendency', 'tent', 'terrible', 'territory', 'test', 'texture', 'theory', 'thing', 'thought', 'thread', 'thrill', 'throat', 'throne', 'thumb', 'thunder', 'ticket', 'tiger', 'time', 'tin', 'tinder', 'title', 'toad', 'toe', 'tomatoes', 'tongue', 'tooth', 'toothbrush', 'toothpaste', 'top', 'touch', 'town', 'toy', 'trade', 'trail', 'train', 'tramp', 'transport', 'tray', 'treatment', 'tree', 'trick', 'trip', 'trouble', 'trousers', 'truck', 'truth', 'tub', 'turkey', 'turn', 'twig', 'twist', 'umbrella', 'uncle', 'underwear', 'unit', 'use', 'vacation', 'value', 'vampire', 'van', 'vase', 'vegetable', 'veil', 'vein', 'verse', 'vessel', 'vest', 'view', 'visitor', 'voice', 'volcano', 'volleyball', 'voyage', 'waffles', 'walk', 'wall', 'war', 'wash', 'waste', 'watch', 'water', 'wave', 'wax', 'way', 'wealth', 'weather', 'week', 'weight', 'weird', 'werewolf', 'wheel', 'whip', 'whistle', 'wilderness', 'wind', 'window', 'wine', 'wing', 'winter', 'wire', 'wish', 'wizard', 'woman', 'wood', 'wool', 'word', 'work', 'worm', 'worst', 'wound', 'wren', 'wrench', 'wrist', 'writer', 'writing', 'yak', 'yam', 'yard', 'yarn', 'year', 'yoke', 'zebra', 'zephyr', 'zinc', 'zipper', 'zoo']
data.sort()
print data

#
# for index, word in enumerate(data):
#     data[index] = word.strip()
#
# dataSet = set(data)
# for word in data:
#     plural = pattern.en.pluralize(word)
#     if plural in dataSet:
#         dataSet = dataSet - set([plural])
#
# # print dataSet
#
# newData = list(dataSet)
# newData.sort()
#
# print newData
