# Changelog Archive

This folder contains archived changelog entries from previous major versions.

## Rotation practice

When a new major version is released (e.g., v1.0.0):

1. Move all entries **below** `[Unreleased]` from `CHANGELOG.md` to a new file here (e.g., `v0.x.md`)
2. Keep only `[Unreleased]` and the new version entry in the main `CHANGELOG.md`
3. Add a link at the bottom of `CHANGELOG.md`: `[Older versions](docs/changelog-archive/)`

## File naming

- `v0.x.md` — all v0 releases
- `v1.x.md` — all v1 releases (archived when v2.0.0 ships)

## Format

Each archive file uses the same [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format as the main file.
