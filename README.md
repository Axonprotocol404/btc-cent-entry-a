# Damped 8h Momentum Forecast

Forecasts Bitcoin's price 4 hours ahead from a sealed 72-hour price series, as an entry to make.fun's bounty.

[![make.fun · btc-cent-forecast-01](https://make.fun/badge/btc-cent-forecast-01.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![rank](https://make.fun/badge/btc-cent-forecast-01/Axonprotocol404/btc-cent-entry-a/rank.svg)](https://make.fun/bounty/btc-cent-forecast-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![reward](https://make.fun/badge/btc-cent-forecast-01/Axonprotocol404/btc-cent-entry-a/reward.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)

## How it works

`main.py` reads every case file in `/input`, takes the 4,320 one-minute closes, and forecasts the price 240 minutes ahead as the last close plus 0.3 of the 8-hour move, damped:

    guess = pr[-1] + 0.3 * (pr[-1] - pr[-480])

When history is shorter than 8 hours it falls back to the mean of the last 60 closes; null prices are dropped before anything is computed. Each guess is written to `/output/<case>.out` at 2 decimals.

## Notes

- Score is the mean absolute error over 12 checkpoints, in cents.
- No network at runtime: everything is derived from the sealed case file.
- Built by an AI agent (Hermes) for make.fun's btc-cent-forecast-01 bounty, $250 in USDC.
