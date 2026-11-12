# Requirements traceability

Each row follows one clause of a requirement from issue to design to code to test.
A marker should be able to pick any row and find every link.

| Req | Clause | Issue | Design section | Code file | Test name | Status |
|-----|--------|-------|----------------|-----------|-----------|--------|
| R1 | Full array of invaders, three alien types | # | [Design R1](Design-R1-Fleet) | `game/fleet/fleet.py` | `test_...` | To do |
| R1 | Side-to-side movement | # | | | | |
| R1 | Random firing at the player | # | | | | |
| R1 | Speed rises as invaders are destroyed | # | | | | |
| R2 | Continuous multiple bullets | # | [Design R2](Design-R2-Player) | `game/player/player.py` | | |
| R2 | Invaders die when shot | # | | | | |
| R2 | Player loses a life and respawns when hit | # | | | | |
| R2 | Game ends when lives run out | # | | | | |
| R3 | Four barriers | # | [Design R3](Design-R3-Barriers) | `game/barriers/barrier_row.py` | | |
| R3 | Barriers erode when hit by either side | # | | | | |
