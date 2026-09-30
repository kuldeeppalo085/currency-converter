# Problem Statement: Currency Exchange Converter

## Problem
Those who travel, shop online or send money abroad face the ever-present task of determining how much an amount in a currency is worth in a different currency. With volatile exchange rates, static or memorized values quickly go out-of-date, and manually looking up rates and performing the arithmetic is both tedious and error-prone (not that floating-point arithmetic is particularly precise).

## Aim
A python command-line app that converts an amount between two currencies by utilizing current exchange rates, and continues working (albeit perhaps with less accurate data) when there is no network connectivity.

## Scope (in)
- Convert an amount in one currency to another
- Current exchange rates from a free public api
- Local caching of rates to reduce number of network calls
- Input validation and error messaging
- Ability to fall back to cached, or default rates on network failure
- Unit tests for the currency conversion logic

## Scope (out)
- Actual money transfers or payment processing
- Handling of bank or card fees and margins
- Historical rates, visualizations, or forecasting
- Graphical or web-based user interface
- User account management or database

## Inputs and Outputs
Input: amount to be converted, source currency code, target currency code (example: `100 USD INR`)
Output: The converted value, rounded to two decimals along with the source of the exchange rate used (`live`, `cache`, `stale-cache`, or `fallback` )

## Constraints and Assumptions
- Python 3.8+, but only standard libraries
- The exchange rates are obtained from a third-party public source and represent mid-market rates, not actual buy/sell rates
- Internet access is required to get the live exchange rates

## Success Criteria
1. Correct conversions between any two currencies
2. Invalid input, negative amount or unrecognized currency results in a human-readable error message
3. Application continues to work (although with potentially out-of-date rates) when there is no network connectivity, and warns the user
4. All tests pass

## Demo Video 
<video width="640" height="360" autoplay muted loop>
  <source src="C:\Users\gover\OneDrive\Desktop\project\demo\Screen Recording.mp4" type="video/mp4">
</video>