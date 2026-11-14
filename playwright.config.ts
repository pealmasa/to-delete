import { defineConfig, devices } from "@playwright/test";

/**
 * Playwright configuration — Helo Studio template
 * Docs: https://playwright.dev/docs/test-configuration
 *
 * E2e tests run against staging after deploy — not on every PR.
 * See studio-best-practices/playwright.md for conventions.
 */
export default defineConfig({
  testDir: "./tests/e2e",
  testMatch: "**/*.spec.ts",

  // Fail fast — stop after first failure in CI
  maxFailures: process.env.CI ? 1 : undefined,

  // Retry on CI to reduce flakiness
  retries: process.env.CI ? 2 : 0,

  // Parallel in CI, sequential locally for easier debugging
  workers: process.env.CI ? 4 : 1,

  // Reporter
  reporter: [
    ["html", { outputFolder: "playwright-report", open: "never" }],
    ["list"],
  ],

  use: {
    // Base URL — override via env var in CI
    baseURL: process.env.BASE_URL ?? "http://localhost:3000",

    // Keep trace on retry for debugging
    trace: "on-first-retry",

    // Screenshot on failure
    screenshot: "only-on-failure",

    // Video on retry
    video: "on-first-retry",
  },

  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
    // Uncomment to add more browsers when needed
    // { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    // { name: "webkit", use: { ...devices["Desktop Safari"] } },
    // { name: "mobile-chrome", use: { ...devices["Pixel 5"] } },
  ],

  // Dev server — only used when running locally against dev
  // Comment out when running against staging/prod
  // webServer: {
  //   command: "pnpm dev",
  //   url: "http://localhost:3000",
  //   reuseExistingServer: !process.env.CI,
  // },
});
