#!/usr/bin/env python3
from atproto import Client, client_utils
import sys
import tomli
from pathlib import Path

# Load config from TOML file
config_dir = Path.home() / ".config" / "skycli"
config_file = config_dir / "config.toml"

if not config_file.exists():
    print(f"Error: Config file not found at {config_file}", file=sys.stderr)
    print("Please create it with [auth] username and password", file=sys.stderr)
    sys.exit(1)

try:
    with open(config_file, "rb") as f:
        config = tomli.load(f)
except Exception as e:
    print(f"Error reading config file: {str(e)}", file=sys.stderr)
    sys.exit(1)

def create_post(text):
    try:
        client = Client()
        client.login(config["auth"]["username"], config["auth"]["password"])
        
        # Use TextBuilder with chaining for better text construction
        text_builder = client_utils.TextBuilder()
        
        # Split text and process each part
        words = text.split()
        for i, word in enumerate(words):
            if word.startswith('http://') or word.startswith('https://'):
                text_builder.link(word, word)
            elif word.startswith('#'):
                text_builder.tag(word, word[1:])
            elif word.startswith('@'):
                handle = word[1:]  # Remove @ for resolution
                try:
                    # Resolve handle to DID, but keep @ in display text
                    resolved = client.resolve_handle(handle)
                    text_builder.mention(word, resolved.did)  # Use word to keep @
                except Exception as e:
                    # If resolution fails, fall back to plain text
                    print(f"Warning: Could not resolve handle {handle}: {str(e)}", file=sys.stderr)
                    text_builder.text(word)
            else:
                # add the rest of the text
                text_builder.text(word)
            
            # Add space between parts, except for the last one
            if i < len(words) - 1:
                text_builder.text(' ')
        
        # Create and send the post
        response = client.send_post(text=text_builder)
        print("Post created successfully!")
        print(f"uri='{response.uri}' cid='{response.cid}'")
        return 0
    except Exception as e:
        print(f"Error creating post: {str(e)}", file=sys.stderr)
        return 1

def main():
    text = sys.stdin.read().strip()
    return_code = create_post(text)
    sys.exit(return_code)

if __name__ == "__main__":
    main()
