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

The `sky` command supports two main ways of posting:

### Direct Posting

```bash
# Basic text post
sky "Hello from Bluesky!"

# Post with mentions and hashtags
sky "Hey @alice.bsky.social check out this #awesome tool!"

# Multi-word hashtags
sky "Having fun at #BuildingInPublic today"

# URLs are automatically detected
sky "Check out this cool project: https://github.com/you/skycli"

# Combine mentions, tags, and URLs
sky "Thanks @bob.bsky.social for sharing https://example.com #opensource"
```

### Pipe Input

You can pipe any command output directly to Bluesky:

```bash
# Simple echo
echo "Hello world!" | sky

# System information
date | sky
uptime | sky
hostname | sky

# File contents
cat announcement.txt | sky

# Command output
fortune | sky  # Share random quotes
weather-cli | sky  # Share weather updates

# Filter and transform
ps aux | grep python | sky  # Share running Python processes
journalctl -n 5 | sky  # Share recent system logs

# Chain multiple commands
echo "Current time and load:" | cat - <(uptime) | sky
```

### Tips

- When using direct posting, remember to quote your message to handle spaces
- Mentions (@user) are automatically resolved to Bluesky handles
- URLs are detected and properly linked
- Hashtags can be single-word (#tag) or multi-word (#ThisIsATag)
- Pipe any command output that might be interesting to share

## Features
- Two input methods: direct command or pipe
- Smart handling of mentions (@user) and hashtags (#tag)
- Automatic URL detection and linking
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
