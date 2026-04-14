---
layout: default
---

<div class="nav-bar">
    <a href="../index.html" class="nav-btn">Home</a>
    <a href="tasks.html" class="nav-btn">Tasks</a>
    <a href="../leaderboard/leaderboard.html" class="nav-btn">Leaderboard</a>
</div>

<div class="content-section">
    <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
        <div>
            <h2 style="margin: 0;">Task 7: And Then There Was Light</h2>
            <p style="margin: 5px 0 0 0;"><strong>Type:</strong> Coding + Visualization</p>
        </div>
        <img src="assignment7/logo.png" alt="Task 7 Logo" style="width: 200px; height: auto; flex-shrink: 0;">
    </div>
    
    <h3>Problem Statement</h3>
    <p>You have a 3-sensor grid in a small office. Occupied period is 08:00–16:00 over 2 weekdays → 16 occupied hours total.</p>
    
    <h4>Workplane Illuminance (lux) at each hour:</h4>
    <ul>
        <li><strong>Sensor A:</strong> 120, 180, 260, 310, 410, 520, 610, 480, 220, 190, 280, 330, 390, 450, 510, 470</li>
        <li><strong>Sensor B:</strong> 90, 140, 210, 240, 290, 310, 360, 340, 130, 110, 200, 260, 300, 320, 330, 310</li>
        <li><strong>Sensor C:</strong> 40, 60, 80, 110, 150, 180, 210, 190, 50, 70, 90, 120, 140, 160, 180, 170</li>
    </ul>
    
    <h4>Questions to Solve:</h4>
    <ol>
        <li><strong>Compute sDA300/50%:</strong> A sensor "passes" if it has ≥300 lux for ≥50% of occupied hours; sDA is the percentage of sensors that pass.</li>
        <li><strong>Compute ASE1000,250:</strong> Using the dataset, what percentage of sensors experience ≥1000 lux for ≥250 occupied hours? (Note: for this small dataset, this threshold is not met, requiring thoughtful interpretation.)</li>
        <li><strong>Create a Floor-Plan Map:</strong> Produce a visual map showing which sensor points pass or fail the sDA300/50% criterion.</li>
    </ol>
    
    <h3>Goal</h3>
    <p>Compute two daylight metrics and create a simple visual pass/fail floor-plan map.</p>
    
    <h3>Brief</h3>
    <p>Use the simplified office sensor dataset to:</p>
    <ul>
        <li>Compute sDA300/50%</li>
        <li>Compute ASE1000,250h</li>
        <li>Create a floor-plan style map showing which sensor points pass or fail the sDA criterion</li>
    </ul>
    
    <h3>Rules</h3>
    <ul>
        <li>Use any method: code, spreadsheet, notebook, or simple HTML/SVG</li>
        <li>Visualization does not need to be fancy, but it should be understandable</li>
        <li>Focus on correct logic and clear output</li>
    </ul>
    
    <h3>Deliverables</h3>
    <ul>
        <li>Computed sDA300/50%</li>
        <li>Computed ASE1000,250h</li>
        <li>Visual map of pass/fail sensors</li>
        <li>Code or workflow used</li>
        <li>"How we did it" documentation</li>
    </ul>
    
    <h3>Scoring Criteria</h3>
    <ul>
        <li><strong>Correctness:</strong> Are the metrics computed correctly?</li>
        <li><strong>Clarity:</strong> Is the metric calculation clear?</li>
        <li><strong>Visual Quality:</strong> How effective is the visualization?</li>
        <li><strong>Reproducibility:</strong> Can the logic be followed and reproduced?</li>
    </ul>
    
    <h3>What It Teaches</h3>
    <ul>
        <li>AI as a coding assistant</li>
        <li>AI for data analysis</li>
        <li>AI for visualizing technical outcomes</li>
        <li>Translating definitions into computational logic</li>
    </ul>
    
    <h3>Submission</h3>
    <a href="https://kuleuven-my.sharepoint.com/:f:/g/personal/maarten_bassier_kuleuven_be/IgDWXqXngeB1RZ41G5HnvCG-AY9Z1YX5woyZBmJXPOpawkw?e=IKLclh" class="submit-btn" target="_blank" rel="noopener noreferrer">Submit Solution & Report</a>
</div>
