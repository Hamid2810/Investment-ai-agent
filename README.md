 Investment Research AI Agent

## What Is This?

This is an AI-powered system that analyzes stocks using multiple data sources and AI agents. It's like having 4 investment analysts working in parallel:
- **Fundamental Analyst**: Analyzes financial health
- **Technical Analyst**: Analyzes price trends
- **Sentiment Analyst**: Analyzes market mood
- **Head Analyst**: Combines all three for final recommendation

## How It Works

```
Stock Ticker Input
        ↓
   Data Fetcher (Gets data from 4 APIs)
        ↓
   Parallel Analysis (4 detectives work at same time)
        ↓
   Synthesis (Head detective combines reports)
        ↓
   Output (BUY / HOLD / SELL recommendation)
```

## What You Get

- **Investment Recommendation**: BUY, HOLD, or SELL with confidence level
- **Investment Thesis**: 2-3 sentence explanation of the recommendation
- **Risk/Reward Ratio**: Upside potential vs downside risk
- **Detailed Analysis**: Full reports from all 4 detectives

## How to Use

### 1. Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### 2. Create .env File
Create a `.env` file with your API keys:
```
FINNHUB_API_KEY=your_key_here
FMP_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

### 3. Run It
```bash
python main.py
```

### 4. Check Results
Open `analysis_results.json` to see the recommendations

## System Architecture

### 1. Data Fetcher
Collects data from 4 sources:
- **Finnhub**: Current prices, news sentiment
- **FMP**: Financial statements (income, balance sheet, cash flow)
- **Alpha Vantage**: Historical prices, technical indicators
- **NewsAPI**: Recent news articles

### 2. Fundamental Agent
- Analyzes: Revenue, profit, debt, equity
- Calculates: ROE, debt-to-equity, margins
- Scores: 0-100 based on financial health

### 3. Technical Agent
- Analyzes: Price trends, momentum, support/resistance
- Indicators: RSI, moving averages, volatility
- Scores: 0-100 based on technical strength

### 4. Sentiment Agent
- Analyzes: News sentiment, market mood
- Counts: Positive vs negative articles
- Identifies: Key themes and catalysts

### 5. Synthesis Agent
- Combines three scores with weighted formula:
  - 60% Fundamental (most important)
  - 25% Technical (timing matters)
  - 15% Sentiment (psychology matters)
- Produces: Final recommendation with thesis

## Sample Output

```json
{
  "ticker": "AAPL",
  "current_price": 246.50,
  "recommendation": "BUY",
  "confidence": 82,
  "thesis": "Apple demonstrates strong fundamentals with expanding margins. Technical trend is bullish. Market sentiment is constructive.",
  "risk_reward_ratio": 2.5
}
```

## Files and Folders

```
investment-ai-agent/
├── .env                          (your secret API keys)
├── .gitignore                    (tells Git to ignore .env)
├── requirements.txt              (list of Python tools)
├── README.md                     (this file)
├── main.py                       (orchestration script)
├── analysis_results.json         (output file)
└── src/
    ├── data_fetcher.py          (gets data from APIs)
    └── agents/
        ├── fundamental_agent.py
        ├── technical_agent.py
        ├── sentiment_agent.py
        └── synthesis_agent.py
```

## Technologies Used

- **Python 3.9+**: Programming language
- **Anthropic Claude**: AI brain for analysis
- **Finnhub, FMP, Alpha Vantage, NewsAPI**: Data sources
- **Pandas**: Data processing
- **Requests**: API calls

## How to Customize

### Change the Stocks
Edit `main.py`, line with `tickers = ["AAPL", "MSFT", "TSLA"]`

### Adjust the Weighting
In `synthesis_agent.py`, change this line:
```python
final_score = (fundamental_score * 0.60) + (technical_score * 0.25) + (sentiment_score * 0.15)
```

### Add More Analysis
Each agent can be extended with more sophisticated analysis

## Troubleshooting

**Error: "Invalid API key"**
- Check your .env file for typos
- Make sure you copied the full API key

**Error: "Rate limit exceeded"**
- You hit an API's rate limit
- Wait a few minutes before trying again

**Error: "ModuleNotFoundError"**
- Run: `pip install -r requirements.txt`

## Future Extensions

- Add backtesting framework (test if recommendations work)
- Add portfolio comparison (compare multiple stocks)
- Add earnings call analysis (parse company earnings calls)
- Add macro factor analysis (correlation with market factors)
- Create web dashboard (make it interactive)
- Deploy to cloud (make it accessible online)

## License

This project is for educational purposes.

