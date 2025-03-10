# Appendix F: Economic Analysis Implementation
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

class EconomicAnalyzer:
    def __init__(self, amm_models):
        self.models = amm_models  # Dictionary of initialized AMM instances
        self.results = {}
        
    def run_impermanent_loss_analysis(self, price_range=(0.1, 10), steps=100):
        """F.1 Impermanent Loss Comparison"""
        results = {'prices': [], 'il': {name: [] for name in self.models}}
        
        prices = np.linspace(price_range[0], price_range[1], steps)
        for price in prices:
            for name, model in self.models.items():
                # Calculate impermanent loss
                initial_x = model.x0
                initial_y = model.y0
                current_value = initial_x * price + initial_y
                
                # Get current pool value
                pool_value = model.get_pool_value(price)
                
                il = (pool_value - current_value) / current_value
                results['il'][name].append(il)
            results['prices'].append(price)
        
        self.results['impermanent_loss'] = results
        return self
    
    def calculate_liquidity_efficiency(self, trade_volume=1e6, steps=100):
        """F.2 Liquidity Efficiency Metrics"""
        results = {'efficiency': {name: [] for name in self.models}}
        
        for _ in range(steps):
            for name, model in self.models.items():
                # Simulate random trades
                size = np.random.uniform(0.1, 0.5) * trade_volume
                direction = np.random.choice(['buy', 'sell'])
                
                # Execute trade and measure impact
                before_value = model.get_pool_value()
                model.execute_trade(size, direction)
                after_value = model.get_pool_value()
                
                # Calculate efficiency metric
                efficiency = (after_value - before_value) / size
                results['efficiency'][name].append(efficiency)
        
        self.results['liquidity_efficiency'] = results
        return self
    
    def analyze_market_impact(self, trade_sizes=np.logspace(3, 6, 50)):
        """F.3 Market Impact Analysis"""
        results = {'sizes': trade_sizes, 'impact': {name: [] for name in self.models}}
        
        for size in trade_sizes:
            for name, model in self.models.items():
                # Measure price impact
                initial_price = model.get_price()
                model.execute_trade(size, 'buy')
                new_price = model.get_price()
                impact = (new_price - initial_price) / initial_price
                results['impact'][name].append(impact)
                model.reset()  # Reset to initial state
        
        self.results['market_impact'] = results
        return self
    
    def visualize_results(self):
        """Generate publication-quality visualizations"""
        plt.figure(figsize=(15, 10))
        
        # Impermanent Loss Plot
        plt.subplot(2, 2, 1)
        for name in self.models:
            il = self.results['impermanent_loss']['il'][name]
            prices = self.results['impermanent_loss']['prices']
            plt.plot(prices, il, label=name)
        plt.xscale('log')
        plt.title('Impermanent Loss Comparison')
        plt.xlabel('Price Ratio')
        plt.ylabel('Impermanent Loss')
        plt.legend()
        
        # Liquidity Efficiency Histogram
        plt.subplot(2, 2, 2)
        efficiencies = [self.results['liquidity_efficiency']['efficiency'][name] 
                      for name in self.models]
        plt.hist(efficiencies, bins=30, label=list(self.models.keys()))
        plt.title('Liquidity Efficiency Distribution')
        plt.xlabel('Efficiency Metric')
        plt.ylabel('Frequency')
        plt.legend()
        
        # Market Impact Analysis
        plt.subplot(2, 2, 3)
        for name in self.models:
            impact = self.results['market_impact']['impact'][name]
            sizes = self.results['market_impact']['sizes']
            plt.loglog(sizes, np.abs(impact), label=name)
        plt.title('Market Impact Analysis')
        plt.xlabel('Trade Size (log)')
        plt.ylabel('Price Impact (log)')
        plt.legend()
        
        # Statistical Analysis Table
        plt.subplot(2, 2, 4)
        stats_data = []
        for name in self.models:
            il = np.mean(self.results['impermanent_loss']['il'][name])
            eff = np.mean(self.results['liquidity_efficiency']['efficiency'][name])
            impact = np.polyfit(np.log(self.results['market_impact']['sizes']), 
                              np.log(self.results['market_impact']['impact'][name]), 1)[0]
            stats_data.append([name, il, eff, impact])
        
        plt.table(cellText=stats_data,
                 colLabels=['Model', 'Avg IL', 'Avg Eff', 'Impact Slope'],
                 loc='center')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        return self

# Usage Example
if __name__ == "__main__":
    # Initialize AMM models with sample parameters
    amm_models = {
        'HYDRA': HydraAMM(x0=1e6, y0=1e6),
        'Uniswap V2': ConstantProductAMM(x0=1e6, y0=1e6),
        'Uniswap V3': ConcentratedAMM(x0=1e6, y0=1e6, width=0.3)
    }
    
    analyzer = EconomicAnalyzer(amm_models)\
        .run_impermanent_loss_analysis()\
        .calculate_liquidity_efficiency()\
        .analyze_market_impact()\
        .visualize_results()