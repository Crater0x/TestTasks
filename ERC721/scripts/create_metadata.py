import json, os
from random import choices

IMAGES_BASE_URL = "https://ipfs.io/ipfs/Qmb8Guy7sL3i3GWKxaP62m98r8FgMQYoxnpapTmotCDzu1/"
PROJECT_NAME = "NFT"

attributes = {
	"Clothes": {
		"values": ["Jacket", "Suit", "Military", "Empty"],
		"probabilities": [0.45, 0.25, 0.1, 0.2]
	},
	"Hair": {
		"values": ["Fade", "Mohawk", "Box", "Empty"],
		"probabilities": [0.3, 0.25, 0.35, 0.1]
	},
	"Boots": {
		"values": ["Nike", "Adidas", "New Balance", "Empty"],
		"probabilities": [0.4, 0.2, 0.1, 0.3]
	},

}

def get_attribute(trait_type):
    value = choices(attributes[trait_type]["values"], attributes[trait_type]["probabilities"])[0]
    return {
        "trait_type": trait_type,
        "value": value
    }


def generate_metadata():
    os.makedirs('./metadata')
    for token_id in range(100):
        metadata = {
            "description": "This is my firts test NFT",
            "image": f"{IMAGES_BASE_URL}bear-{token_id:04}.png",
            "name": f"{PROJECT_NAME} {token_id:04}",
            "attributes": []
        }

        for attribute in attributes:
            metadata["attributes"].append(get_attribute(attribute))
        
        with open(f'./metadata/{token_id}.json', 'w') as outfile:
            json.dump(metadata, outfile, indent=4)

def main():
    generate_metadata()