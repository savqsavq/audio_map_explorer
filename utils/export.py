import json

def save_feature_json(results, filename):
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    print(f"saved {filename}")
    
