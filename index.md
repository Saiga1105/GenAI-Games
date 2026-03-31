---
layout: home
author_profile: false
classes: wide
---

<style>
.hero {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8)), url('https://images.unsplash.com/photo-1487958449943-2429e8be8625?w=1200&h=600&fit=crop');
  background-size: cover;
  background-position: center;
  color: white;
  padding: 100px 0;
  text-align: center;
  position: relative;
}
.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.3);
  z-index: 1;
}
.hero .container {
  position: relative;
  z-index: 2;
}
.hero h1 {
  font-size: 3em;
  margin-bottom: 0.5em;
}
.hero p {
  font-size: 1.5em;
}
.btn-hero {
  background-color: #ff6b6b;
  border: none;
  padding: 15px 30px;
  font-size: 1.2em;
  margin-top: 20px;
}
.section {
  padding: 60px 0;
}
.group-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  text-align: center;
  background: white;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.group-card h3 {
  color: #333;
}
.video-container {
  text-align: center;
  margin: 20px 0;
}
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.btn {
  border-radius: 25px;
  padding: 10px 20px;
}
.btn-primary {
  background-color: #667eea;
  border-color: #667eea;
}
.btn-primary:hover {
  background-color: #5a67d8;
  border-color: #5a67d8;
}
.btn-secondary {
  background-color: #718096;
  border-color: #718096;
}
.btn-secondary:hover {
  background-color: #5a6c7d;
  border-color: #5a6c7d;
}
</style>

<div class="hero">
  <div class="container">
    <h1>GenAI Games</h1>
    <p>A cross-disciplinary AI challenge for construction researchers</p>
    <p>17 April | 14:00–17:00 | Followed by a reception</p>
    <a href="#subscription" class="btn btn-hero">Register Now</a>
  </div>
</div>

<section class="section">
  <div class="container">
    <!-- Nav tabs -->
    <ul class="nav nav-tabs" id="genaiTabs" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Home</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="content-tab" data-bs-toggle="tab" data-bs-target="#content" type="button" role="tab" aria-controls="content" aria-selected="false">Content</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="subscription-tab" data-bs-toggle="tab" data-bs-target="#subscription" type="button" role="tab" aria-controls="subscription" aria-selected="false">Subscription</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="tasks-tab" data-bs-toggle="tab" data-bs-target="#tasks" type="button" role="tab" aria-controls="tasks" aria-selected="false">Tasks</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="leaderboard-tab" data-bs-toggle="tab" data-bs-target="#leaderboard" type="button" role="tab" aria-controls="leaderboard" aria-selected="false">Leaderboard</button>
      </li>
    </ul>

    <!-- Tab panes -->
    <div class="tab-content" id="genaiTabsContent">
      <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">

        <h2>What is it?</h2>
        <p>The GenAI Games are an experimental event designed to help researchers explore how generative AI can support their work. In mixed teams, participants will tackle short interdisciplinary challenges using AI tools for reasoning, coding, analysis, communication, and creative problem-solving. The aim is not just to compete, but to discover, test, and learn together.</p>

        <div class="video-container">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Introduction to GenAI Games" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>

        <h2>Why are we doing this?</h2>
        <p>This event was created to strengthen the uptake of generative AI across our research groups, while encouraging exchange between different domains in construction research. By working through practical challenges together, participants will discover new tools, new workflows, and new ways of thinking across disciplinary boundaries.</p>

        <h2>Meet the Research Groups</h2>
        <div class="row">
          <div class="col-md-3">
            <div class="group-card">
              <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300&h=200&fit=crop" alt="Footbridge" style="width:100%; border-radius:8px; margin-bottom:10px;">
              <h3>Dynamics of Footbridges</h3>
              <p>This group focuses on the dynamic behaviour of footbridges, including vibration performance, pedestrian-induced loading, and structural comfort and safety.</p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="group-card">
              <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=300&h=200&fit=crop" alt="Concrete" style="width:100%; border-radius:8px; margin-bottom:10px;">
              <h3>Concrete Compositions and Healing Concretes</h3>
              <p>This group works on concrete materials, including innovative mix designs and self-healing or healing-enhanced concretes.</p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="group-card">
              <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=300&h=200&fit=crop" alt="Sustainable Building" style="width:100%; border-radius:8px; margin-bottom:10px;">
              <h3>Sustainable Buildings</h3>
              <p>This group focuses on sustainable buildings, with themes including energy performance, indoor comfort, and CO2 reduction.</p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="group-card">
              <img src="https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=300&h=200&fit=crop" alt="Geomatics" style="width:100%; border-radius:8px; margin-bottom:10px;">
              <h3>Geomatics</h3>
              <p>This group works on surveying, UAV flights, spatial data capture, and point cloud processing.</p>
            </div>
          </div>
        </div>

        <h2>How it Works</h2>
        <ol>
          <li><strong>Team Formation:</strong> Mixed teams of 4-5 PhD researchers from different research groups.</li>
          <li><strong>Challenge Introduction:</strong> Short presentation of the interdisciplinary challenges.</li>
          <li><strong>AI-Powered Problem Solving:</strong> 2 hours to tackle challenges using generative AI tools.</li>
          <li><strong>Presentations:</strong> Teams present their solutions and AI workflows.</li>
          <li><strong>Discussion & Networking:</strong> Followed by reception for exchange and learning.</li>
        </ol>

        <h2>Who Should Join?</h2>
        <p>PhD researchers from the four participating research groups. No advanced AI experience required - curiosity and willingness to experiment are more important than expertise. This is a safe space to learn and explore AI applications in construction research.</p>

        <h2>Event Details</h2>
        <p><strong>Date:</strong> 17 April 2024<br>
        <strong>Time:</strong> 14:00–17:00<br>
        <strong>Location:</strong> KU Leuven<br>
        <strong>Followed by:</strong> Reception</p>

      </div>

      <div class="tab-pane fade" id="content" role="tabpanel" aria-labelledby="content-tab">

        <h2>Example Tasks</h2>
        <p>Here are some example tasks to give you an idea of what to expect. These are simplified versions of the challenges you'll face during the event.</p>

        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">Example 1: Bridge Vibration Analysis</h5>
            <p class="card-text">Given vibration data from a footbridge, use AI to identify patterns in pedestrian loading and suggest design modifications for improved comfort. Tools: Python for data analysis, ChatGPT for interpretation.</p>
            <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=250&fit=crop" alt="Bridge analysis" style="width:100%; border-radius:8px;">
          </div>
        </div>

        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">Example 2: Concrete Mix Design</h5>
            <p class="card-text">Design a self-healing concrete mix using AI to optimize material properties and sustainability metrics. Use generative AI for creative material combinations.</p>
            <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?w=400&h=250&fit=crop" alt="Concrete mix" style="width:100%; border-radius:8px;">
          </div>
        </div>

        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">Example 3: Building Energy Simulation</h5>
            <p class="card-text">Simulate and optimize energy performance of a building model using AI for predictive analysis and design recommendations.</p>
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400&h=250&fit=crop" alt="Building simulation" style="width:100%; border-radius:8px;">
          </div>
        </div>

      </div>

      <div class="tab-pane fade" id="subscription" role="tabpanel" aria-labelledby="subscription-tab">

        <h1>Register for GenAI Games</h1>
        <p>Join the first-of-its-kind event bringing together researchers from four different research domains in construction and built-environment research.</p>
        <p>No advanced AI experience is required. Curiosity matters more than expertise.</p>
        <div class="text-center">
          <a href="/google/index.html" class="btn btn-primary btn-lg me-3" target="_blank">Register with Form</a>
          <a href="https://script.google.com/macros/s/AKfycbxXrocTEDpsnn47rlsz_gpA3hxUIm0sB_3mqrPM8D_U7tx5I1tD0jlLDQtXu8-uYGZuyA/exec" class="btn btn-outline-primary btn-lg" target="_blank">Quick Register</a>
        </div>

      </div>

      <div class="tab-pane fade" id="tasks" role="tabpanel" aria-labelledby="tasks-tab">

        <h1>Challenge Tasks</h1>
        <p>During the event, teams will tackle these short challenges using generative AI tools.</p>
        {% assign tasks = site.data.tasks %}
        {% for task in tasks %}
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">{{ task.title }}</h5>
            <p class="card-text">{{ task.description }}</p>
            <a href="/assets/data/{{ task.data_file }}" class="btn btn-secondary" download>Download Data</a>
            <form action="mailto:maarten.bassier@kuleuven.be?subject=Task Submission {{ task.id }}" method="post" enctype="text/plain" class="mt-3">
              <input type="hidden" name="task_id" value="{{ task.id }}">
              <div class="mb-3">
                <label for="team_name_{{ task.id }}" class="form-label">Team Name</label>
                <input type="text" class="form-control" id="team_name_{{ task.id }}" name="team_name" required>
              </div>
              <div class="mb-3">
                <label for="result_{{ task.id }}" class="form-label">Submission</label>
                <textarea class="form-control" id="result_{{ task.id }}" name="result" rows="3" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>
        </div>
        {% endfor %}

      </div>

      <div class="tab-pane fade" id="leaderboard" role="tabpanel" aria-labelledby="leaderboard-tab">

        <h1>Live Leaderboard</h1>
        <p>Track the progress of teams during the GenAI Games.</p>
        <iframe src="https://docs.google.com/spreadsheets/d/1YOUR_SHEET_ID_HERE/pubhtml?widget=true&amp;headers=false" width="100%" height="600" frameborder="0"></iframe>
        <p><em>Note: Replace the sheet ID in the iframe src with your actual Google Sheet ID for live updates.</em></p>

      </div>
    </div>
  </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Initialize Bootstrap tabs
  var triggerTabList = [].slice.call(document.querySelectorAll('#genaiTabs button'))
  triggerTabList.forEach(function (triggerEl) {
    var tabTrigger = new bootstrap.Tab(triggerEl)
    triggerEl.addEventListener('click', function (event) {
      event.preventDefault()
      tabTrigger.show()
    })
  })

  // Handle URL hash for direct tab linking
  var hash = window.location.hash;
  if (hash) {
    var tabId = hash.substring(1);
    var tabElement = document.querySelector('button[data-bs-target="#' + tabId + '"]');
    if (tabElement) {
      var tab = new bootstrap.Tab(tabElement);
      tab.show();
    }
  }
});
</script>