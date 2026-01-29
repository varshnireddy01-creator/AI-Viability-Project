import pandas as pd

class AIProjectEvaluator:
    def __init__(self, labor_rate_hr=45, ai_token_cost=0.05):
        self.labor_rate = labor_rate_hr
        self.ai_cost = ai_token_cost

    def analyze_automation_value(self, task_name, volume, manual_time_mins, implementation_fee):
        # Calculate Manual Costs
        manual_hours = (manual_time_mins * volume) / 60
        manual_total_cost = manual_hours * self.labor_rate
        
        # Calculate AI Costs
        ai_total_cost = (volume * self.ai_cost) + implementation_fee
        
        # ROI Calculation
        net_savings = manual_total_cost - ai_total_cost
        roi_pct = (net_savings / ai_total_cost) * 100
        
        return {
            "Task": task_name,
            "Manual Cost": f"${manual_total_cost:,.2f}",
            "AI Cost": f"${ai_total_cost:,.2f}",
            "Net Savings": f"${net_savings:,.2f}",
            "ROI": f"{roi_pct:.2f}%"
        }

if __name__ == "__main__":
    # Example Case: Automating Construction Site Daily Log Summaries
    evaluator = AIProjectEvaluator()
    report = evaluator.analyze_automation_value(
        task_name="Daily Site Log Synthesis",
        volume=1200,          # Reports per year
        manual_time_mins=30,  # Time a PM takes per report
        implementation_fee=5000 # Cost to build/test the prompt pipeline
    )

    print("--- EXECUTIVE SUMMARY: AI VIABILITY REPORT ---")
    for key, value in report.items():
        print(f"{key:15}: {value}")
