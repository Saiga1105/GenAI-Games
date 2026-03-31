---
layout: single
title: Leaderboard
classes: wide
---

<section class="section">
  <div class="container">
    <h1>Live Leaderboard</h1>
    <p>Track the progress of teams during the GenAI Games.</p>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">Team</th>
          <th scope="col">Score</th>
        </tr>
      </thead>
      <tbody>
        {% assign leaderboard = site.data.leaderboard | sort: "score" | reverse %}
        {% for item in leaderboard %}
        <tr>
          <th scope="row">{{ forloop.index }}</th>
          <td>{{ item.name }}</td>
          <td>{{ item.score }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</section>