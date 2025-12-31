
# main.py
# This file orchestrates the entire system

import sys
sys.path.insert(0, 'src')

from data_fetcher import DataFetcher
from agents.fundamental_agent import FundamentalAgent
from agents.technical_agent import TechnicalAgent
from agents.sentiment_agent import SentimentAgent
from agents.synthesis_agent import SynthesisAgent

import json

def analyze_stock(ticker: str) -> dict:
    """
    Complete analysis workflow for a single stock
    
    Flow:
    1. Fetch data from all APIs
    2. Run fundamental analysis
    3. Run technical analysis
    4. Run sentiment analysis
    5. Synthesize all three into final recommendation
    6. Return results
    """
    
    print(f"\n{'='*60}")
    print(f"ANALYZING {ticker}")
    print(f"{'='*60}\n")
    
    # STEP 1: Fetch data (Librarian goes to 4 libraries)
    print(f"1. Fetching data from 4 sources...")
    fetcher = DataFetcher(ticker)
    data = fetcher.fetch_all()
    print(f"   ✓ Got price data")
    print(f"   ✓ Got financial statements")
    print(f"   ✓ Got technical indicators")
    print(f"   ✓ Got sentiment data")
    
    # STEP 2: Fundamental Analysis (Detective #1 analyzes)
    print(f"\n2. Running fundamental analysis...")
    fund_agent = FundamentalAgent()
    fundamental_analysis = fund_agent.analyze(ticker, data['fundamentals'], data['technicals'])
    fundamental_score = fundamental_analysis.get('overall_fundamental_score', 50)
    print(f"   ✓ Fundamental Score: {fundamental_score}/100")
    
    # STEP 3: Technical Analysis (Detective #2 analyzes)
    print(f"3. Running technical analysis...")
    tech_agent = TechnicalAgent()
    technical_analysis = tech_agent.analyze(ticker, data['technicals'])
    technical_score = technical_analysis.get('technical_score', 50)
    print(f"   ✓ Technical Score: {technical_score}/100")
    
    # STEP 4: Sentiment Analysis (Detective #3 analyzes)
    print(f"4. Running sentiment analysis...")
    sent_agent = SentimentAgent()
    sentiment_analysis = sent_agent.analyze(ticker, data.get('sentiment', {}))
    sentiment_score = sentiment_analysis.get('sentiment_score', 50)
    print(f"   ✓ Sentiment Score: {sentiment_score}/100")
    
    # STEP 5: Synthesize (Head Detective combines all three)
    print(f"5. Synthesizing final recommendation...")
    syn_agent = SynthesisAgent()
    recommendation = syn_agent.synthesize(
        ticker, 
        fundamental_score, 
        technical_score, 
        sentiment_score,
        {
            'fundamental': fundamental_analysis,
            'technical': technical_analysis,
            'sentiment': sentiment_analysis
        }
    )
    
    # STEP 6: Compile final output
    result = {
        'ticker': ticker,
        'timestamp': data['timestamp'],
        'current_price': data['price'].get('current_price') if data['price'] else None,
        'scores': {
            'fundamental': fundamental_score,
            'technical': technical_score,
            'sentiment': sentiment_score,
            'final_confidence': recommendation.get('confidence', 50)
        },
        'recommendation': recommendation.get('recommendation'),
        'thesis': recommendation.get('thesis'),
        'risk_reward_ratio': recommendation.get('risk_reward_ratio'),
        'detailed_analysis': {
            'fundamental': fundamental_analysis,
            'technical': technical_analysis,
            'sentiment': sentiment_analysis,
            'synthesis': recommendation
        }
    }
    
    # Print final recommendation
    print(f"\n{'='*60}")
    print(f"FINAL RECOMMENDATION: {recommendation.get('recommendation')}")
    print(f"Confidence: {recommendation.get('confidence')}%")
    print(f"Thesis: {recommendation.get('thesis')}")
    print(f"{'='*60}\n")
    
    return result


if __name__ == "__main__":
    # Analyze 3 stocks as examples
    tickers = ["AAPL", "MSFT", "TSLA"]
    
    all_results = []
    
    for ticker in tickers:
        try:
            result = analyze_stock(ticker)
            all_results.append(result)
        except Exception as e:
            print(f"❌ Error analyzing {ticker}: {e}")
    
    # Save all results to a JSON file
    with open('analysis_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n✓ Analysis complete!")
    print(f"✓ Results saved to analysis_results.json")
