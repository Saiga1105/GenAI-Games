# GenAI Games

A Jekyll-based website for GenAI tasks, subscriptions, and leaderboard.

## Features

- **Subscription Tab**: Users can subscribe by filling out a form (sends via email).
- **Tasks Tab**: Displays tasks with descriptions, downloadable data, and submission forms (sends via email).
- **Leaderboard Tab**: Shows current scores in a table.

## Technology

- Built with Jekyll
- Uses Minimal Mistakes theme
- Bootstrap for styling and tabs
- Static site deployed on GitHub Pages

## Local Development

1. Install Ruby (version 2.5 or higher)
2. Install Jekyll: `gem install jekyll bundler`
3. Clone the repository
4. Run `jekyll serve` to start the local server
5. Visit `http://localhost:4000`

## Deployment

The site is deployed from the `main` branch on GitHub Pages.

To enable:
1. Go to your repository settings
2. Navigate to Pages
3. Set source to "Deploy from a branch"
4. Select `main` branch and `/ (root)` folder
5. Save

## Forms

Forms use `mailto:` to send submissions via email. Update the email address in `index.md` and `_config.yml` as needed.

For production, consider using a service like Formspree or Netlify Forms for better handling.

## Updating Content

- Tasks: Edit `_data/tasks.yml`
- Leaderboard: Edit `_data/leaderboard.yml`
- Site config: Edit `_config.yml`