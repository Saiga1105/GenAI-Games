---
layout: single
title: Tasks
classes: wide
---

<section class="section">
  <div class="container">
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
</section>