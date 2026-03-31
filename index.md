---
layout: home
author_profile: false
---

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

<div class="container mt-5">
  <h1>Welcome to GenAI Games</h1>
  <p>This is the front page of our website.</p>

  <ul class="nav nav-tabs" id="myTab" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="subscription-tab" data-bs-toggle="tab" data-bs-target="#subscription" type="button" role="tab" aria-controls="subscription" aria-selected="true">Subscription</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="tasks-tab" data-bs-toggle="tab" data-bs-target="#tasks" type="button" role="tab" aria-controls="tasks" aria-selected="false">Tasks</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="leaderboard-tab" data-bs-toggle="tab" data-bs-target="#leaderboard" type="button" role="tab" aria-controls="leaderboard" aria-selected="false">Leaderboard</button>
    </li>
  </ul>
  <div class="tab-content" id="myTabContent">
    <div class="tab-pane fade show active" id="subscription" role="tabpanel" aria-labelledby="subscription-tab">
      <h3>Subscribe</h3>
      <form action="mailto:contact@genaigames.com?subject=Subscription" method="post" enctype="text/plain">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input type="text" class="form-control" id="name" name="name" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" name="email" required>
        </div>
        <div class="mb-3">
          <label for="details" class="form-label">Details</label>
          <textarea class="form-control" id="details" name="details" rows="3"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Subscribe</button>
      </form>
    </div>
    <div class="tab-pane fade" id="tasks" role="tabpanel" aria-labelledby="tasks-tab">
      <h3>Tasks</h3>
      {% assign tasks = site.data.tasks %}
      {% for task in tasks %}
      <div class="card mb-3">
        <div class="card-body">
          <h5 class="card-title">Task {{ task.id }}</h5>
          <p class="card-text">{{ task.description }}</p>
          <a href="/assets/data/{{ task.data_file }}" class="btn btn-secondary" download>Download Data</a>
          <form action="mailto:contact@genaigames.com?subject=Task Submission {{ task.id }}" method="post" enctype="text/plain" class="mt-3">
            <input type="hidden" name="task_id" value="{{ task.id }}">
            <div class="mb-3">
              <label for="user_name_{{ task.id }}" class="form-label">Your Name</label>
              <input type="text" class="form-control" id="user_name_{{ task.id }}" name="user_name" required>
            </div>
            <div class="mb-3">
              <label for="result_{{ task.id }}" class="form-label">Result</label>
              <textarea class="form-control" id="result_{{ task.id }}" name="result" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
      {% endfor %}
    </div>
    <div class="tab-pane fade" id="leaderboard" role="tabpanel" aria-labelledby="leaderboard-tab">
      <h3>Leaderboard</h3>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">Name</th>
            <th scope="col">Score</th>
          </tr>
        </thead>
        <tbody>
          {% assign leaderboard = site.data.leaderboard %}
          {% for item in leaderboard %}
          <tr>
            <th scope="row">{{ item.rank }}</th>
            <td>{{ item.name }}</td>
            <td>{{ item.score }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>