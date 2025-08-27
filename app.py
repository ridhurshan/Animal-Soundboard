from flask import Flask, render_template

app = Flask(__name__)

# Data for the alphabet section (single image for the full song)
alphabet_data = {
    "alphabet": {
        "image": "images/alphabet.jpg",
        "sound": "sound/alphabet.mp3"
    }
}

# Data for the rhymes section with added text content
rhymes_data = {
    "rhyme1": {
        "image": "images/rhyme1.jpeg",
        "sound": "sound/rhyme1.mp3",
        "text": "Twinkle, twinkle, little star,\nHow I wonder what you are.\nUp above the world so high,\nLike a diamond in the sky."
    },
    "rhyme2": {
        "image": "images/rhyme2.jpeg",
        "sound": "sound/rhyme2.mp3",
        "text": "Mary had a little lamb,\nIts fleece was white as snow.\nAnd everywhere that Mary went,\nThe lamb was sure to go."
    }
}

# Data for the animals section (with all the extra photos and sounds)
animals_data = {
    "bee": {
        "image": "images/Bee.jpg",
        "sound": "sound/Bee.mp3"
    },
    "bear": {
        "image": "images/Bear.jpg",
        "sound": "sound/Bear.mp3"
    },
    "bird": {
        "image": "images/Bird.jpg",
        "sound": "sound/Bird.mp3"
    },
    "camel": {
        "image": "images/Camel.webp",
        "sound": "sound/Camel.mp3"
    },
    "cat": {
        "image": "images/cat.jpeg",
        "sound": "sound/cat.mp3"
    },
    "chicken": {
        "image": "images/Chicken.jpg",
        "sound": "sound/Chicken.mp3"
    },
    "crow": {
        "image": "images/Crow.jpg",
        "sound": "sound/Crow.mp3"
    },
    "dog": {
        "image": "images/dog.jpeg",
        "sound": "sound/dog.mp3"
    },
    "dolphin": {
        "image": "images/Dolphin.webp",
        "sound": "sound/Dolphin.mp3"
    },
    "donkey": {
        "image": "images/Donkey.webp",
        "sound": "sound/Donkey.mp3"
    },
    "duck": {
        "image": "images/Duck.jpg",
        "sound": "sound/Duck.mp3"
    },
    "elephant": {
        "image": "images/elephant.jpeg",
        "sound": "sound/elephant.mp3"
    },
    "frog": {
        "image": "images/Frog.jpg",
        "sound": "sound/Frog.mp3"
    },
    "goat": {
        "image": "images/Goat.jpeg",
        "sound": "sound/Goat.mp3"
    },
    "gorilla": {
        "image": "images/Gorilla.jpg",
        "sound": "sound/Gorilla.mp3"
    },
    "hyena": {
        "image": "images/Hyena.jpg",
        "sound": "sound/Hyena.mp3"
    },
    "lion": {
        "image": "images/lion.jpeg",
        "sound": "sound/lion.mp3"
    },
    "monkey": {
        "image": "images/Monkey.jpg",
        "sound": "sound/Monkey.mp3"
    },
    "mouse": {
        "image": "images/Mouse.webp",
        "sound": "sound/Mouse.mp3"
    },
    "owl": {
        "image": "images/Owl.webp",
        "sound": "sound/Owl.mp3"
    },
    "parrot": {
        "image": "images/Parrot.jpg",
        "sound": "sound/Parrot.mp3"
    },
    "pig": {
        "image": "images/Pig.jpeg",
        "sound": "sound/Pig.mp3"
    },
    "pigeon": {
        "image": "images/Pigeon.webp",
        "sound": "sound/Pigeon.mp3"
    },
    "rhinoceros": {
        "image": "images/Rhinoceros.avif",
        "sound": "sound/Rhinoceros.mp3"
    },
    "sheep": {
        "image": "images/Sheep.jpg",
        "sound": "sound/Sheep.mp3"
    },
    "snake": {
        "image": "images/Snake.webp",
        "sound": "sound/Snake.mp3"
    },
    "tiger": {
        "image": "images/Tiger.webp",
        "sound": "sound/Tiger.mp3"
    },
    "wolf": {
        "image": "images/Wolf.webp",
        "sound": "sound/Wolf.mp3"
    },

    "hippopotamus": {
        "image": "images/Hippopotamus.jpeg",
        "sound": "sound/Hippopotamus.mp3"
    },
    "bat": {
        "image": "images/Bat.webp",
        "sound": "sound/Bat.mp3"
    },
    "koala": {
        "image": "images/Koala.jpeg",
        "sound": "sound/Koala.mp3"
    },
    "lobster": {
        "image": "images/Lobster.jpeg",
        "sound": "sound/Lobster.mp3"
    },
    "otter": {
        "image": "images/Otter.webp",
        "sound": "sound/Otter.mp3"
    },
    "seal": {
        "image": "images/Seal.jpg",
        "sound": "sound/Seal.mp3"
    },
    "alligator": {
        "image": "images/Alligator.jpg",
        "sound": "sound/Alligator.mp3"
    },
    "hawk": {
        "image": "images/Hawk.jpg",
        "sound": "sound/Hawk.mp3"
    },
    "skunk": {
        "image": "images/Skunk.jpeg",
        "sound": "sound/Skunk.mp3"
    },
    "cheetah": {
        "image": "images/cheetah.jpeg",
        "sound": "sound/cheetah.mp3"
    },
    "flamingo": {
        "image": "images/Flamingo.webp",
        "sound": "sound/Flamingo.mp3"
    },
    "peacock": {
    "image": "images/Peacock.jpg",
    "sound": "sound/Peacock.mp3"
}
}

@app.route('/')
def home():
    """Renders the main page with alphabet, rhymes, and animal data."""
    return render_template('index.html', alphabet=alphabet_data, rhymes=rhymes_data, animals=animals_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)