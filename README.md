# skycli

A minimal command-line tool for posting to Bluesky social network.

## Installation

```bash
pipx install .
```

## Configuration

Create a `config.toml` file in `~/.config/skycli/config.toml` with your Bluesky credentials:

```toml
[auth]
username = "your-handle.bsky.social"
password = "your-password"
```

## Usage

Post by piping text to the command:

```bash
echo "Hello world!" | sky
```

You can also use it with other commands:

```bash
date | sky
cat message.txt | sky
fortune | sky  # Share random quotes
```

## Features
- Simple pipe-based interface
- Secure credential management
- Fast and lightweight
- Easy integration with other CLI tools

## Exit Codes
- 0: Success
- 1: Error (configuration or posting failed)

## Examples

Share your system uptime:
```bash
uptime | sky
```

Post the output of any command:
```bash
weather-cli | sky
```

## Tips
- Use `|` to pipe any command output to Bluesky
- URLs are automatically detected and linked
- Mentions (@user) are resolved to proper Bluesky handles
- Hashtags (#tag) are properly formatted
