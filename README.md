# chart-pattern-analyser

Algorithm that scans candlestick data across multiple equities, finds popular candlestick patterns and tracks the outcome.

## Data

 we will start by using the One Minute Data from OANDA for EUR/USD and based on our results might move on to Bitcoin Data

## Patterns

There are lots of patterns available online, i will integrate one after the other, the goal would be to have incorporated most of the following:

![patterns](/Ressources/Chart%20Patterns.png)


## 1. Rectangle Continuations

As they are easiest we will start by adding Rectangle Continuations, these are defined by multiple highs and lows hitting the same price area and then an outbreak into one of either direction, ideally into the direction we were coming from previously.
