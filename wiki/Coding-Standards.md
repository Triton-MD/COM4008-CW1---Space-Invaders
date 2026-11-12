# Coding standards

- Follow PEP 8; names in `snake_case`, classes in `PascalCase`
- Docstring on every module, class and public method
- Type hints on public methods
- No hard-coded numbers: use `settings.py`
- Only `game/assets.py` knows file paths
- Movement is multiplied by `dt`
- Game rules live in methods that need no window, so they can be tested
<!-- Add anything else the team agrees. -->
