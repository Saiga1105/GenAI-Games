---
layout: default
---

<div class="nav-bar">
    <a href="../index.html" class="nav-btn">Home</a>
    <a href="../tasks/tasks.html" class="nav-btn">Tasks</a>
    <a href="leaderboard.html" class="nav-btn">Leaderboard</a>
</div>

<div class="content-section">
    <h2>Scoreboard</h2>
    <p>This page reads live score data from the Google Sheet backend.</p>
    <p><a href="https://docs.google.com/spreadsheets/d/{{ site.scoreboard_sheet_id }}/edit" target="_blank" rel="noopener noreferrer" class="download-btn">Open Score Sheet</a></p>
    <div id="scoreboard-status">Loading scoreboard...</div>
    <div id="scoreboard-content" style="display: none;"></div>
</div>

<script>
    (function () {
        const sheetId = "{{ site.scoreboard_sheet_id }}";
        const statusEl = document.getElementById("scoreboard-status");
        const contentEl = document.getElementById("scoreboard-content");
        const sheetsData = {};
        const requiredSheets = ["Teams", "Tasks", "Scores"];

        function escapeHtml(value) {
            return String(value ?? "")
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#39;");
        }

        function gvizToObjects(response) {
            const cols = response.table.cols.map(col => col.label || col.id || "");
            return response.table.rows.map(row => {
                const item = {};
                cols.forEach((col, index) => {
                    item[col] = row.c[index] ? row.c[index].v : "";
                });
                return item;
            });
        }

        function maybeRender() {
            if (!requiredSheets.every(name => Array.isArray(sheetsData[name]))) {
                return;
            }

            const teams = sheetsData.Teams
                .map(team => ({
                    name: team.team,
                    total: Number(team.total || 0)
                }))
                .filter(team => team.name)
                .sort((a, b) => b.total - a.total);

            const tasks = sheetsData.Tasks
                .map(task => ({
                    id: task.task_id,
                    name: task.task_name,
                    winner: task.winner
                }))
                .filter(task => task.id && task.name);

            const scores = sheetsData.Scores
                .map(score => ({
                    task_id: score.task_id,
                    team: score.team,
                    workflow: Number(score.workflow || 0),
                    correctness: Number(score.correctness || 0),
                    visuals: Number(score.visuals || 0),
                    verification: Number(score.verification || 0),
                    total: Number(score.total || 0)
                }))
                .filter(score => score.task_id && score.team);

            if (!teams.length) {
                statusEl.textContent = "The score sheet is reachable, but it does not contain team data yet.";
                return;
            }

            const leader = teams[0];
            const teamsTable = teams.map((team, index) => `
                <tr>
                    <td>${index + 1}</td>
                    <td><strong>${escapeHtml(team.name)}</strong></td>
                    <td>${team.total}</td>
                </tr>
            `).join("");

            const taskSections = tasks.map(task => {
                const taskScores = scores
                    .filter(score => score.task_id === task.id)
                    .sort((a, b) => b.total - a.total);

                const rows = taskScores.map((score, index) => `
                    <tr>
                        <td>${index + 1}</td>
                        <td><strong>${escapeHtml(score.team)}</strong></td>
                        <td>${score.workflow}</td>
                        <td>${score.correctness}</td>
                        <td>${score.visuals}</td>
                        <td>${score.verification}</td>
                        <td>${score.total}</td>
                    </tr>
                `).join("");

                return `
                    <div style="margin-top: 28px; padding-top: 24px; border-top: 1px solid #e1e7ef;">
                        <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; flex-wrap: wrap; margin-bottom: 14px;">
                            <h4 style="margin: 0;">${escapeHtml(task.name)}</h4>
                            <p style="margin: 0;"><strong>Winner:</strong> ${escapeHtml(task.winner || (taskScores[0] ? taskScores[0].team : ""))}</p>
                        </div>
                        <div class="leaderboard-table">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Place</th>
                                        <th>Team</th>
                                        <th>Workflow</th>
                                        <th>Correctness</th>
                                        <th>Visuals</th>
                                        <th>Verification</th>
                                        <th>Total</th>
                                    </tr>
                                </thead>
                                <tbody>${rows}</tbody>
                            </table>
                        </div>
                    </div>
                `;
            }).join("");

            contentEl.innerHTML = `
                <div style="margin-top: 24px; padding: 24px; border-radius: 16px; background: linear-gradient(135deg, #fff7d6, #ffe8a3); border: 1px solid #f0d980;">
                    <h3 style="margin-bottom: 8px;">Current Leader</h3>
                    <p style="font-size: 2rem; font-weight: bold; margin-bottom: 4px;">${escapeHtml(leader.name)}</p>
                    <p style="margin: 0; color: #5b4a00;">${leader.total} total points</p>
                </div>
                <div class="content-section" style="margin-top: 20px;">
                    <h3>Total Score Per Team</h3>
                    <div class="leaderboard-table">
                        <table>
                            <thead>
                                <tr>
                                    <th>Rank</th>
                                    <th>Team</th>
                                    <th>Total Points</th>
                                </tr>
                            </thead>
                            <tbody>${teamsTable}</tbody>
                        </table>
                    </div>
                </div>
                <div class="content-section" style="margin-top: 20px;">
                    <h3>Points Per Team Per Task</h3>
                    <p>Each task is graded on workflow, correctness, visuals, and verification.</p>
                    ${taskSections}
                </div>
            `;

            statusEl.style.display = "none";
            contentEl.style.display = "block";
        }

        function handleFailure() {
            statusEl.innerHTML = "The scoreboard could not be loaded from Google Sheets. Make sure the sheet is shared so the website can read it.";
        }

        function addSheetLoader(sheetName, callbackName) {
            const script = document.createElement("script");
            script.src = `https://docs.google.com/spreadsheets/d/${sheetId}/gviz/tq?sheet=${encodeURIComponent(sheetName)}&headers=1&tqx=responseHandler:${callbackName}`;
            script.onerror = handleFailure;
            document.head.appendChild(script);
        }

        window.handleTeamsSheet = function (response) {
            sheetsData.Teams = gvizToObjects(response);
            maybeRender();
        };

        window.handleTasksSheet = function (response) {
            sheetsData.Tasks = gvizToObjects(response);
            maybeRender();
        };

        window.handleScoresSheet = function (response) {
            sheetsData.Scores = gvizToObjects(response);
            maybeRender();
        };

        addSheetLoader("Teams", "handleTeamsSheet");
        addSheetLoader("Tasks", "handleTasksSheet");
        addSheetLoader("Scores", "handleScoresSheet");
    })();
</script>
