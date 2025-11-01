#!/usr/bin/env node
const { Octokit } = require('@octokit/rest')

async function run() {
  try {
    const topicsEnv = process.env.TOPICS || ''
    const token = process.env.TOKEN || process.env.GITHUB_TOKEN
    if (!token) {
      console.log('No token provided; skipping topics update')
      return
    }
    const topics = topicsEnv.split(',').map(t => t.trim()).filter(Boolean)
    if (topics.length === 0) {
      console.log('No topics provided; nothing to do')
      return
    }
    const [owner, repo] = (process.env.GITHUB_REPOSITORY || '').split('/')
    if (!owner || !repo) {
      console.log('GITHUB_REPOSITORY is not set; skipping')
      return
    }
    const octokit = new Octokit({ auth: token })
    console.log(`Setting topics: ${topics.join(', ')} on ${owner}/${repo}`)
    await octokit.rest.repos.replaceAllTopics({ owner, repo, names: topics })
    console.log('Topics updated')
  } catch (err) {
    console.error('Error updating topics:', err)
    process.exit(1)
  }
}

run()
